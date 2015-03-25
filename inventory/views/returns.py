'''

	Author: John Turner
	Version: 1.0
	Last Updated: 3/21/2015

	View that manages the rental returns processes.

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
import datetime

templater = get_renderer('inventory')

##########################################################################################
################################## RENTAL RETURN FORM CLASS ##############################
##########################################################################################

# Rental Return form.
class RentalReturnForm(CustomForm):

	''' Class for the form to be used in returning a rental. '''

	## Class title ##
	title = "Rental Return"

	## Link ##
	link = 'inventory/returns'

	# No Delete Button
	delete_button = False

	item             = forms.CharField(required=True, max_length=100)
	price_per_day    = forms.DecimalField(max_digits=10, decimal_places=2)
	total_price      = forms.CharField()
	discount_percent = forms.IntegerField(max_value=100)

	## Clean functions ##


##########################################################################################
################################## DAMAGE FEE FORM CLASS #################################
##########################################################################################

# Form for adding a damage fee
class DamageFeeForm(CustomForm):

	'''
		Class for the form for adding a damage fee to a rental return. 
	'''

	## Class Title ##
	title = "Damage Fee Details"

	# No delete button
	delete_button = False

	description = forms.CharField(required=True)
	waived      = forms.BooleanField(required=True)

	## Clean Functions ##

##########################################################################################
###################################### DEFAULT ACTION ####################################
##########################################################################################

@view_function
@permission_required(['base_app.change_rentalitem'], login_url='/homepage/login/')
def process_request(request):
	
	# Define the view bag
	params = {}

	# Delete all items that exist in the database with names that are blank
	# (when someone starts an item and abandons it)
	rentals = hmod.Inventory.objects.filter(shelf_location='').delete()
	items   = hmod.Item.objects.filter(shelf_location='').delete()
	items   = hmod.WardrobeItem.objects.filter(shelf_location='').delete()

	# Grab all rentals that are still out. 
	items = hmod.RentalItem.objects.all().filter(date_in=None).order_by('due_date')

	params['rentals'] = items
	params['today'] = datetime.date.today()

	return templater.render_to_response(request, 'returns.html', params)

##########################################################################################
###################################### PROCESS RETURN ####################################
##########################################################################################

@view_function
@permission_required(['base_app.change_rentalitem'], login_url='/homepage/login/')
def return_rental(request):
	
	# Define the view bag
	params={}

	try:
		item = hmod.RentalItem.objects.get(id=request.urlparams[0])
	except hmod.RentalItem.DoesNotExist:
		return HttpResponseRedirect('/inventory/returns/')

	# Calculate the total price
	days_passed = (datetime.date.today() - item.date_out.date())
	total_price = item.item.price_per_day * days_passed.days

	# Create the form and populate the data
	form = RentalReturnForm(request, initial={
		'item'            : item.item.specs.name,
		'price_per_day'   : item.item.price_per_day,
		'total_price'     : '${0}'.format(total_price),
		'discount_percent': 0,
		})

	# Make certain fields readonly 
	form.fields['item'].widget.attrs['readonly']          = True
	form.fields['price_per_day'].widget.attrs['readonly'] = True
	form.fields['total_price'].widget.attrs['readonly']   = True

	# if request.method == 'POST':

	# 	form = RentalReturnForm(request, request.POST)

	# 	if form.is_valid():

			# Update the rental
			

	params['rental_item'] = item
	params['form'] = form

	return templater.render_to_response(request, 'ProcessReturn.html', params)

##########################################################################################
##################################### EDIT RENTAL ACTION #################################
##########################################################################################

@view_function
@permission_required(['base_app.change_rentalitem'], login_url='/homepage/login/')
def details(request):
	
	# Define the view bag
	params={}

	try:
		item = hmod.RentalItem.objects.get(id=request.urlparams[0])
	except hmod.RentalItem.DoesNotExist:
		return HttpResponseRedirect('/inventory/returns/')

	params['item'] = item

	return templater.render_to_response(request, 'RentalDetails.html', params)

##########################################################################################
######################################## ADD FEE #########################################
##########################################################################################

@view_function
def add_fee(request):

	'''
		Creates damage fee.

		NOTE! Late fees are automatically applied if the due date is past and the 
		rental is being checked in. 
	'''

	# Define the view bag
	params = {}

	# Delete any fees created and left without finishing:
	fees = hmod.DamageFee.objects.filter(description='').delete()

	# Grab the rental according to what was passed in the url params
	try:
		rental = hmod.RentalItem.objects.get(id=request.urlparams[0])
	except hmod.RentalItem.DoesNotExist:
		return HttpResponse('failed to get rental')

	# Create the fee and pass it over to the fee editing view function
	fee             = hmod.DamageFee()
	fee.description = ''
	fee.amount      = 0
	fee.transaction = rental.transaction
	
	fee.save()

	return HttpResponseRedirect('/inventory/returns.edit_fee/{0}'.format(fee.id))

##########################################################################################
####################################### EDIT FEE #########################################
##########################################################################################

@view_function
def edit_fee(request):

	'''
		This is the screen where the user will edit the damage fee. 
	'''

	# Define the view bag
	params = {}

	# Grab the fee just passed in the url params
	try:
		fee = hmod.DamageFee.objects.get(id=request.urlparams[0])
	except hmod.DamageFee.DoesNotExist:
		return HttpResponse('failed to get damage fee')

	form = DamageFeeForm(request, initial={
		'description': fee.description,
		'waived'     : fee.waived,
		})

	# if request.method == 'POST':

	# 	form = DamageFeeForm(request, request.POST)

	# 	if form.is_valid():

	params['form'] = form

	return templater.render_to_response(request, 'EditFeeAjax.html', params)