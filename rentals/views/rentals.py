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