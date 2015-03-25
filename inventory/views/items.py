'''

	Author: John Turner
	Version: 1.0
	Last Updated: 2/5/2015

	View for all CRUD functions for the items in the system.

'''

from django.conf import settings
from base_app.CustomForm import CustomForm
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from django.contrib.auth.decorators import permission_required
import base_app.models as hmod
from django.utils.translation import ugettext as _
from django_mako_plus.controller.router import get_renderer
from django.utils import timezone

templater = get_renderer('inventory')

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
@permission_required(['base_app.change_wardrobeitem', 'base_app.change_nonwardrobeitem'], login_url='/homepage/login/')
def process_request(request):
	
	# Define the view bag
	params = {}

	# Delete all items that exist in the database with names that are blank
	# (when someone starts an item and abandons it)
	items = hmod.NonWardrobeItem.objects.filter(name='').delete()
	items = hmod.WardrobeItem.objects.filter(name='').delete()
	owner = hmod.User.objects.filter(username='').delete()

	# Grab all the items from the database, both wardrobe and non-wardrobe
	items = hmod.NonWardrobeItem.objects.all().order_by('name')

	params['n_w_items'] = items

	items = hmod.WardrobeItem.objects.all().order_by('name')

	params['w_items'] = items

	return templater.render_to_response(request, 'items.html', params)

##########################################################################################
##################################### EDIT NW ACTION #####################################
##########################################################################################

@view_function
@permission_required(['base_app.change_nonwardrobeitem'], login_url='/homepage/login/')
def edit_non(request):
	
	# Define the view bag
	params={}

	# Layout of the urls:
	# 
	# /homepage/user.edit/a/b/c/d/e...
	# 
	# request.urlparams[n] = everything after the <appname>/<filename>/
	# 
	# For example [0] = a, [1] = b... 

	try:
		item = hmod.NonWardrobeItem.objects.get(id=request.urlparams[0])
	except hmod.NonWardrobeItem.DoesNotExist:
		return HttpResponseRedirect('/inventory/items/')

	# Pass in item data to the form
	form = EditNWItemForm(request, initial={
		'name': item.name,
		'description': item.description,
		'value': item.value,
		'is_rentable': item.is_rentable,
		'standard_rental_price': item.standard_rental_price,
		'owner': item.owner
		})

	if request.method == 'POST':

		# Validate the form
		form = EditNWItemForm(request, request.POST)

		if form.is_valid():

			# Update the object
			item.name = form.cleaned_data['name']
			item.description = form.cleaned_data['description']
			item.value = form.cleaned_data['value']
			item.is_rentable = form.cleaned_data['is_rentable']
			item.standard_rental_price = form.cleaned_data['standard_rental_price']
			item.owner = form.cleaned_data['owner']

			# Save it to the database
			item.save()

			# Return user to list
			return HttpResponseRedirect('/inventory/items/')

	params['form'] = form

	return templater.render_to_response(request, 'EditItem.html', params)

##########################################################################################
###################################### EDIT W ACTION #####################################
##########################################################################################

@view_function
@permission_required(['base_app.change_wardrobeitem'], login_url='/homepage/login/')
def edit_w(request):
	
	# Define the view bag
	params={}

	# Layout of the urls:
	# 
	# /homepage/user.edit/a/b/c/d/e...
	# 
	# request.urlparams[n] = everything after the <appname>/<filename>/
	# 
	# For example [0] = a, [1] = b... 

	try:
		item = hmod.WardrobeItem.objects.get(id=request.urlparams[0])
	except hmod.WardrobeItem.DoesNotExist:
		return HttpResponseRedirect('/inventory/items/')

	# Pass in item data to the form
	form = EditWItemForm(request, initial={
		'name': item.name,
		'description': item.description,
		'value': item.value,
		'is_rentable': item.is_rentable,
		'standard_rental_price': item.standard_rental_price,
		'owner': item.owner,
		'size': item.size,
		'size_modifier': item.size_modifier,
		'gender': item.gender,
		'color': item.color,
		'pattern': item.pattern,
		'start_year': item.start_year,
		'end_year': item.end_year,
		'note': item.note,
		})

	if request.method == 'POST':

		# Validate the form
		form = EditWItemForm(request, request.POST)

		if form.is_valid():

			# Update the object
			item.name = form.cleaned_data['name']
			item.description = form.cleaned_data['description']
			item.value = form.cleaned_data['value']
			item.is_rentable = form.cleaned_data['is_rentable']
			item.standard_rental_price = form.cleaned_data['standard_rental_price']
			item.owner = form.cleaned_data['owner']
			item.size = form.cleaned_data['size']
			item.size_modifier = form.cleaned_data['size_modifier']
			item.gender = form.cleaned_data['gender']
			item.color = form.cleaned_data['color']
			item.pattern = form.cleaned_data['pattern']
			item.start_year = form.cleaned_data['start_year']
			item.end_year = form.cleaned_data['end_year']
			item.note = form.cleaned_data['note']

			# Save it to the database
			item.save()

			# Return user to list
			return HttpResponseRedirect('/inventory/items/')

	params['form'] = form

	return templater.render_to_response(request, 'EditItem.html', params)

##########################################################################################
##################################### CREATE ACTION ######################################
##########################################################################################

@view_function
@permission_required(['base_app.add_wardrobeitem', 'base_app.add_nonwardrobeitem'], login_url='/homepage/login/')
def create(request):
	''' Creates a new item, either wardrobe or non, based on the urlparams passed in '''

	# Delete any new blank items or owners that could have been added before. 
	items = hmod.NonWardrobeItem.objects.filter(name='').delete()
	items = hmod.WardrobeItem.objects.filter(name='').delete()
	owner = hmod.User.objects.filter(username='').delete()

	# Create new owner to tie the item to
	owner = hmod.User()

	owner.save()

	# Get the URL param to see what kind of item to create
	item_type = request.urlparams[0]

	# If type = 1, it's Non
	# If type = 2, it's Wardrobe
	# Else, refresh the page
	
	if item_type == '1':

		item = hmod.NonWardrobeItem()
		item.name = ''
		item.description = ''
		item.value = 0.00
		item.is_rentable = False
		item.standard_rental_price = 0.00
		item.owner = owner

		# Save to the db
		item.save()

		# Redirect to the Edit page, with blank info
		return HttpResponseRedirect('/inventory/items.edit_non/{0}'.format(item.id))

	elif item_type == '2':

		item = hmod.WardrobeItem()
		item.name = ''
		item.description = ''
		item.value = 0.00
		item.is_rentable = False
		item.standard_rental_price = 0.00
		item.owner = owner
		item.size = 0
		item.size_modifier = ''
		item.gender = ''
		item.color = ''
		item.pattern = ''
		item.start_year = timezone.now()
		item.end_year = timezone.now()
		item.note = ''

		# Save to the db
		item.save()

		# Redirect to the Edit page, with blank info
		return HttpResponseRedirect('/inventory/items.edit_w/{0}'.format(item.id))

	else:
		return HttpResponseRedirect('/inventory/items/')

##########################################################################################
#################################### DELETE NW ACTION ####################################
##########################################################################################

@view_function
@permission_required(['base_app.delete_nonwardrobeitem'], login_url='/homepage/login/')
def delete_nw(request):

	''' Deletes a Non-Wardrobe item '''

	try:
		item = hmod.NonWardrobeItem.objects.get(id=request.urlparams[0])
	except NonWardrobeItem.DoesNotExist:
		pass # Item exists

	item.delete()

	return HttpResponseRedirect('/inventory/items/')

##########################################################################################
#################################### DELETE NW ACTION ####################################
##########################################################################################

@view_function
@permission_required(['base_app.delete_wardrobeitem'], login_url='/homepage/login/')
def delete_w(request):

	''' Deletes a Wardrobe item '''

	try:
		item = hmod.WardrobeItem.objects.get(id=request.urlparams[0])
	except WardrobeItem.DoesNotExist:
		pass # Item exists

	item.delete()

	return HttpResponseRedirect('/inventory/items/')