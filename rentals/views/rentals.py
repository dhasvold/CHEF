'''

	Author: John Turner
	Version: 1.0
	Last Updated: 3/20/2015

	View that manages the client-facing products section of the website. 

'''

from django.conf import settings
from base_app.CustomForm import CustomForm
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from django.contrib.auth.decorators import login_required, permission_required
import base_app.models as hmod
from django.utils.translation import ugettext as _
from django_mako_plus.controller.router import get_renderer
from django.utils import timezone
from decimal import *
from django.contrib.auth import authenticate
from django.utils import timezone
import datetime


templater = get_renderer('rentals')

##########################################################################################
################################### FORM CLASS ###########################################
##########################################################################################

# Non-Wardrobe form class
class EditNWItemForm(CustomForm):

	''' Class for the form to be used in editing the non-wardrobe items. '''

	## Class title ##
	title = "Item Information"

	## Link ##
	link = '/inventory/items'

	## Special Delete Type ##
	delete_type = '_nw'

	name = forms.CharField(required=True, max_length=100)
	description = forms.CharField(widget=forms.Textarea(attrs={'rows' : 3}), max_length=250)
	value = forms.DecimalField(max_digits=10, decimal_places=2)
	is_rentable = forms.BooleanField(required=False)
	standard_rental_price = forms.DecimalField(required=False, max_digits=10, decimal_places=2)
	owner = forms.ModelChoiceField(queryset=hmod.User.objects.all(), empty_label=None)

	## Clean functions ##
	
	# If is_rentable is checked, standard_rental_price better have something in it
	def clean_standard_rental_price(self):

		if self.cleaned_data['is_rentable'] is True and self.cleaned_data['standard_rental_price'] == 0:
			raise forms.ValidationError(_("Please add a rental price."))

		return self.cleaned_data['standard_rental_price']

	# Make sure an owner is selected
	def clean_owner(self):

		empty_owner = hmod.User.objects.filter(username='')

		if self.cleaned_data['owner'] == empty_owner[0]:
			raise forms.ValidationError("Please select an owner.")

		return self.cleaned_data['owner']
	

# Wardrobe Item Form, extends previous
class EditWItemForm(EditNWItemForm):

	## Special Delete Type ##
	delete_type = '_w'

	''' Class for the form to be used in editing wardrobe items '''

	size = forms.IntegerField()
	size_modifier = forms.CharField(max_length=100, required=False)
	gender = forms.CharField(max_length=1)
	color = forms.CharField(max_length=100)
	pattern = forms.CharField(max_length=100)
	start_year = forms.DateField()
	end_year = forms.DateField()
	note = forms.CharField(required=False, max_length=255, widget=forms.Textarea(attrs={ 'rows' : 4 }))

	## Clean functions ##

	# Make sure the years are correct (start year is before end year)



#########AGENT RETURN FORM#########################
class return_form(CustomForm):

	''' Class for the login form '''

	username = forms.CharField(required=True, max_length=100)
	password = forms.CharField(required=True, label="Password", widget=forms.PasswordInput)
	damages = forms.CharField(required=False, label="New Damages Description", max_length=2000)
	damage_fee = forms.DecimalField(required=False, decimal_places=2, label="Damage Fees", max_value=1000000.00)

	def clean(self):

		# Check to see if self is valid
		if self.is_valid():

			if self.cleaned_data['damage_fee'] is None:
				self.cleaned_data['damage_fee'] = Decimal('0')

			# See if username and password combo is correct
			user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])

			if user is None:
				raise forms.ValidationError("Incorrect Username and/or Password")
			else:
				try:
					agentUser = hmod.User.objects.get(username=self.cleaned_data['username'])
				except hmod.User.DoesNotExist:
					return HttpResponseRedirect('/rentals/rentals.returns/')

				if not agentUser.groups.filter(name='Administrator').exists() or agentUser.groups.filter(name='Manager').exists():
					raise forms.ValidationError("Must have a manager or administrator accept your return.")

		return self.cleaned_data

##########################################################################################
###################################### DEFAULT ACTION ####################################
##########################################################################################

@view_function
@login_required(login_url='/homepage/login/')
def process_request(request):
	
	# Define the view bag
	params = {}

	# Delete all items that exist in the database with names that are blank
	# (when someone starts an item and abandons it)
	rentals = hmod.Inventory.objects.filter(shelf_location='').delete()
	items   = hmod.Item.objects.filter(shelf_location='').delete()
	items   = hmod.WardrobeItem.objects.filter(shelf_location='').delete()

	# Grab all the items and wardrobe items from the database that are available for rent
	items = hmod.Item.objects.all().filter(wardrobeitem=None).exclude(standard_rental_price=None).exclude(times_rented=None).exclude(price_per_day=None).order_by('specs__name')

	params['non_wardrobe'] = items

	items = hmod.WardrobeItem.objects.all().exclude(standard_rental_price=None).exclude(times_rented=None).exclude(price_per_day=None).order_by('specs__name')

	params['wardrobe'] = items

	return templater.render_to_response(request, 'rentals.html', params)

##########################################################################################
######################################## ITEM DETAILS ####################################
##########################################################################################

@view_function
@login_required(login_url='/homepage/login/')
def details(request):
	
	# Define the view bag
	params={}

	try:
		item = hmod.Item.objects.get(id=request.urlparams[0])
	except hmod.Item.DoesNotExist:
		return HttpResponseRedirect('/rentals/rentals/')

	params['item'] = item

	return templater.render_to_response(request, 'ItemDetails.html', params)

##########################################################################################
######################################## SEE YOUR RETURNS ####################################
##########################################################################################

@view_function
def returns(request):

	# Define the view bag
	params={}

	rental_items = hmod.RentalItem.objects.filter(date_out__range=['1990-01-01', '3000-01-01']).filter(date_in=None)

	customer_rentals = []

	for rental_item in rental_items:
		if rental_item.transaction.customer_id is request.user.id:
			customer_rentals.append(rental_item)

	params['rentalItems'] = customer_rentals

	return templater.render_to_response(request, 'rentals_out.html', params)


##########################################################################################
######################################## AGENT PROCESSES RETURN ##########################
##########################################################################################

@view_function
def return_item(request):

	# Define the view bag
	params = {}
	form = return_form(request)
	form.cancel_button = False
	form.delete_button = False
	form.submit_text = "Return"

	try:
		item = hmod.Item.objects.get(id=request.urlparams[0])
	except hmod.Item.DoesNotExist:
		return HttpResponseRedirect('/rentals/rentals.returns/')

	try:
		lineItem = hmod.RentalItem.objects.get(id=request.urlparams[1])
	except hmod.RentalItem.DoesNotExist:
		return HttpResponseRedirect('/rentals/rentals.returns/')

	date = hmod.RentalItem.objects.filter(due_date__range=[datetime.datetime.now(), '3000-01-01']).filter(item=item).order_by('due_date')

	if request.method == 'POST':
		form = return_form(request, request.POST)
		form.cancel_button = False
		form.delete_button = False
		form.submit_text = "Return"

		if form.is_valid():
			## Authenticate again
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

			## COMPLETE RETURN ##
			lineItem.date_in = datetime.date.today()
			lineItem.agent = user

			item.quantity_on_hand += 1

			##create damage fee line item if applicable
			if len(form.cleaned_data['damages']) > 1 or Decimal(form.cleaned_data['damage_fee']) > 0:
				damageLine = hmod.DamageFee()
				damageLine.amount = Decimal(form.cleaned_data['damage_fee'])
				damageLine.description = form.cleaned_data['damages']
				damageLine.transaction = lineItem.transaction
				damageLine.save()

			lineItem.save()
			item.save()

			return HttpResponseRedirect('/rentals/rentals.returns/')

	params['form'] = form
	params['lineItem'] = lineItem
	params['item'] = item
	params['date'] = date

	return templater.render_to_response(request, 'return_rental.html', params)







##########################################################################################
##################################### SEARCH FORM ACTION #################################
##########################################################################################

# @view_function
# def search(request):

# 	# Define the view bag
# 	params = {}

# 	# If a name has been passed in, then search for the item and return the details page
# 	if request.REQUEST.get('name') is not None:

# 		try:
# 			product = hmod.Inventory.objects.get(specs__name=request.REQUEST.get('name'),item=None)

# 			return HttpResponse('/products/products.details/{0}'.format(product.id))

# 		except hmod.Inventory.DoesNotExist:

# 			return HttpResponse('Product not found')

# 	return templater.render_to_response(request, 'Search.html', params)