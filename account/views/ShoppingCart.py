'''

	Author: John Turner
	Version: 1.0
	Last Updated: 3/6/2015

	View for the functions related to the Shopping Cart

'''

from django.conf import settings
from base_app.CustomForm import CustomForm
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from django.contrib.auth.decorators import login_required, permission_required
import base_app.models as hmod
from django_mako_plus.controller.router import get_renderer
from django.utils.translation import ugettext as _
from base_app.CustomWidgets import CustomSelect, CustomRadioRenderer
from django.contrib.auth import authenticate, login, logout
import requests
from django.core.mail import send_mail
import datetime

templater = get_renderer('account')

##########################################################################################
################################### FORM CLASS ###########################################
##########################################################################################

class ShippingForm(CustomForm):

	''' Class for the form to be used adding shipping info. '''

	# List of constants for the states:
	ALASKA = 'AK'
	ALABAMA = 'AL'
	ARKANSAS = 'AR'
	ARIZON = 'AZ'
	CALIFORNIA = 'CA'
	COLORADO = 'CO'
	CONNECTICUT = 'CT'
	DELAWARE = 'DE'
	FLORIDA = 'FL'
	GEORGIA = 'GA'
	HAWAII = 'HI'
	IOWA = 'IA'
	IDAHO = 'ID'
	ILLINOIS = 'IL'
	INDIANA = 'IN'
	KANSAS = 'KS'
	LOUISIANA = 'LA'
	MASSACHUSETTS = 'MA'
	MARYLAND = 'MD'
	MAINE = 'ME'
	MICHIGAN = 'MI'
	MINNESOTA = 'MN'
	MISSOURI = 'MO'
	MISSISSIPPI = 'MS'
	MONTANA = 'MT'
	NORTH_CAROLINA = 'NC'
	NORTH_DAKOTA = 'ND'
	NEBRASKA = 'NE'
	NEW_HAMPSHIRE = 'NH'
	NEW_JERSEY = 'NJ'
	NEW_MEXICO = 'NM'
	NEVADA = 'NV'
	NEW_YORK = 'NY'
	OHIO = 'OH'
	OKLAHOMA = 'OK'
	OREGON = 'OR'
	PENNSYLVANIA = 'PA'
	RHODE_ISLAND = 'RI'
	SOUTH_CAROLINA = 'SC'
	SOUTH_DAKOTA = 'SD'
	TENNESSEE = 'TN'
	TEXAS = 'TX'
	UTAH = 'UT'
	VIRGINIA = 'VA'
	VERMONT = 'VT'
	WASHINGTON = 'WA'
	WISCONSIN = 'WI'
	WEST_VIRGINIA = 'WV'
	WYOMING = 'WY'

	# Choices list of tuples for the car_states field
	STATE_CHOICES = (
		(ALASKA, 'Alaska'),
		(ALABAMA, 'Alabama'),
		(ARKANSAS, 'Arkansas'),
		(ARIZON, 'Arizon'),
		(CALIFORNIA, 'California'),
		(COLORADO, 'Colorado'),
		(CONNECTICUT, 'Connecticut'),
		(DELAWARE, 'Delaware'),
		(FLORIDA, 'Florida'),
		(GEORGIA, 'Georgia'),
		(HAWAII, 'Hawaii'),
		(IOWA, 'Iowa'),
		(IDAHO, 'Idaho'),
		(ILLINOIS, 'Illinois'),
		(INDIANA, 'Indiana'),
		(KANSAS, 'Kansas'),
		(LOUISIANA, 'Louisiana'),
		(MASSACHUSETTS, 'Massachusetts'),
		(MARYLAND, 'Maryland'),
		(MAINE, 'Maine'),
		(MICHIGAN, 'Michigan'),
		(MINNESOTA, 'Minnesota'),
		(MISSOURI, 'Missouri'),
		(MISSISSIPPI, 'Mississippi'),
		(MONTANA, 'Montana'),
		(NORTH_CAROLINA, 'North Carolina'),
		(NORTH_DAKOTA, 'North Dakota'),
		(NEBRASKA, 'Nebraska'),
		(NEW_HAMPSHIRE, 'New Hampshire'),
		(NEW_JERSEY, 'New Jersey'),
		(NEW_MEXICO, 'New Mexico'),
		(NEVADA, 'Nevada'),
		(NEW_YORK, 'New York'),
		(OHIO, 'Ohio'),
		(OKLAHOMA, 'Oklahoma'),
		(OREGON, 'Oregon'),
		(PENNSYLVANIA, 'Pennsylvania'),
		(RHODE_ISLAND, 'Rhode Island'),
		(SOUTH_CAROLINA, 'South Carolina'),
		(SOUTH_DAKOTA, 'South Dakota'),
		(TENNESSEE, 'Tennessee'),
		(TEXAS, 'Texas'),
		(UTAH, 'Utah'),
		(VIRGINIA, 'Virginia'),
		(VERMONT, 'Vermont'),
		(WASHINGTON, 'Washington'),
		(WISCONSIN, 'Wisconsin'),
		(WEST_VIRGINIA, 'West Virginia'),
		(WYOMING, 'Wyoming'),
	)

	## Class title ##
	title = "Shipping Information"
	link = "products/products"

	# Don't include the delete button.
	delete_button = False

	# Submit text
	submit_text = 'Continue'

	## Form Inputs ##
	address1 = forms.CharField(required=True, max_length=100)
	address2 = forms.CharField(required=False, max_length=100)
	city = forms.CharField(required=True, max_length=100)
	state = forms.ChoiceField(required=True, choices=STATE_CHOICES, widget=CustomSelect)
	ZIP = forms.CharField(required=True)

##########################################################################################
################################### FORM CLASS ###########################################
##########################################################################################

class PaymentForm(CustomForm):

	''' Class for the form for payment info. '''

	## Class title ##
	title = "Payment Info"
	link = "products/products"

	# Don't include the delete button.
	delete_button = False

	# Submit text
	submit_text = 'Continue'

	## Form Inputs ##
	credit_card_number = forms.CharField(required=True, max_length=100)
	card_holder_name = forms.CharField(max_length=100)
	card_company = forms.CharField(max_length=50)
	cvc = forms.IntegerField(required=True)
	expiration_month = forms.CharField(required=True, max_length=2)
	expiration_year = forms.CharField(required=True, max_length=4)
	ZIP = forms.CharField(required=True)

	def clean(self):
		API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
		API_KEY = 'f1fd63257cb654eeb51223cf8faa3de1'

		r = requests.post(API_URL, data = {
			'apiKey': API_KEY,
			'currency': 'usd',
			'amount': self.request.session['total'],
			'type': self.cleaned_data['card_company'],
			'number': self.cleaned_data['credit_card_number'],
			'exp_month': self.cleaned_data['expiration_month'],
			'exp_year': self.cleaned_data['expiration_year'],
			'cvc': self.cleaned_data['cvc'],
			'name': self.cleaned_data['card_holder_name'],
			'description': 'Charge for:' + self.cleaned_data['card_holder_name'],
		})

		# parse response to a dictionary
		resp = r.json()
		print(self.request.session['total'])
		if 'error' in resp:
			raise forms.ValidationError("ERROR: " + resp['error'])

		else:
			print(resp.keys())
			print(resp['ID'])

		return self.cleaned_data



##########################################################################################
################################# DEFAULT ACTION #########################################
##########################################################################################

@view_function
@login_required(login_url='/homepage/login/')
def process_request(request):
	
	# Define the view bag
	params = {}

	# Create a shopping cart in the session if it doesn't already exist
	if 'cart' not in request.session:
		request.session['cart'] = {}

	# Make sure the session variable recognizes the change
	request.session.modified = True

	# Dictionary for items
	items = {} #items means items you actually purchased
	rentals = {}

	for item_id in request.session['cart']:
		try:
			item = hmod.Inventory.objects.get(id=item_id)
		except hmod.Inventory.DoesNotExist:
			return HttpResponse('ITEM NOT FOUND IN DATABASE')

		try:
			if item.item is not None:
				try:
					item1 = hmod.Item.objects.get(id=item_id)
					rentals[item1] = request.session['cart'][item_id]
				except hmod.Item.DoesNotExist:
					return HttpResponse('ITEM NOT FOUND IN DATABASE')

		except hmod.Inventory.DoesNotExist:
			items[item] = request.session['cart'][item_id]


	params['items'] = items
	params['rentals'] = rentals

	return templater.render_to_response(request, 'ShoppingCart.html', params)

##########################################################################################
################################### ADD ITEM ACTION ######################################
##########################################################################################

@view_function
@login_required(login_url='/homepage/login/')
def add(request):
	
	# Define the view bag
	params = {}

	# Create the shopping cart if it already hasn't been
	if 'cart' not in request.session:
		request.session['cart'] = {}

	# Grab the item according to the data passed in the GET
	pid = request.REQUEST.get('id')
	rental = request.REQUEST.get('rental')
	if rental:
		pass
	else:
		quantity = int(request.REQUEST.get('quantity'))


	if rental:
			due_date = request.REQUEST.get('due_date')


			'''split = split[0:split.index('00:00:00')]


			request.session['cart'][pid] = split

			true_date = datetime.datetime.strptime(due_date, "%Y-%m-%d %H:%M:%S.%f")

			time = true_date - datetime.datetime.now()


			print(time)

			split = str(due_date)


			split = split[0:split.index('00:00:00')]'''


			request.session['cart'][pid] = due_date





	else:
		if pid in request.session['cart']:
			request.session['cart'][pid] += quantity
		else:
			request.session['cart'][pid] = quantity

	# Make sure the session variable recognizes the change
	request.session.modified = True

	return HttpResponseRedirect('/account/ShoppingCart/')

##########################################################################################
################################ REMOVE ITEM ACTION ######################################
##########################################################################################

@view_function
@login_required(login_url='/homepage/login/')
def remove(request):
	''' 
		Removes an item from the shopping cart. 
	'''

	# Define the view bag
	params = {}

	# Grab the item id
	pid = request.REQUEST.get('id')

	# Remove from the shopping cart
	if pid in request.session['cart']:

		del request.session['cart'][pid]

	request.session.modified = True

	return HttpResponseRedirect('/account/ShoppingCart/')

##########################################################################################
################################# CHECKOUT FUNCTION ######################################
##########################################################################################

@view_function
@login_required(login_url='/homepage/login/')
def checkout(request):
	'''
		Sends the user to the shipping info page.
	'''

	# Define the view bag
	params={}

	# Grab the user
	try:
		user = hmod.User.objects.get(id=request.user.id)
	except hmod.User.DoesNotExist:
		return HttpResponseRedirect('/products/products/')

	# Pass in user data to the form
	form = ShippingForm(request, initial={
		'address1': user.address.address1,
		'address2': user.address.address2,
		'city': user.address.city,
		'state': user.address.state,
		'ZIP': user.address.ZIP,
		})

	if request.method == 'POST':

		# Validate the form
		form = ShippingForm(request, request.POST)

		if form.is_valid():

			# Return user to list
			return HttpResponseRedirect('/account/ShoppingCart.payment/')

	params['form'] = form




	return templater.render_to_response(request, 'ShippingInfo.html', params)

##########################################################################################
################################ CREDIT CARD INFO FUNCTION ###############################
##########################################################################################

@view_function
@login_required(login_url='/homepage/login/')
def payment(request):
	'''
		Sends the user to the payment page.
	'''

	# Define the view bag
	params={}

	# Pass in user data to the form
	form = PaymentForm(request)

	if request.method == 'POST':

		# Validate the form
		form = PaymentForm(request, request.POST)

		if form.is_valid():

			# Return user to list
			return HttpResponseRedirect('/account/ShoppingCart.confirmation/')

	params['form'] = form

	return templater.render_to_response(request, 'PaymentInfo.html', params)

##########################################################################################
################################### CONFIRMATION ACTION ##################################
##########################################################################################

@view_function
@login_required(login_url='/homepage/login/')
def confirmation(request):
	'''
		Sends the user to the confirmation page.
	'''

	# Define the view bag
	params={}

	trans = hmod.Transaction()

	trans.customer = request.user()

	trans.save()

	for item_id in request.session['cart']:

		try:
			item = hmod.Inventory.objects.get(id=item_id)
		except:
			HttpResponse('Item does not exist')


		try:
			if item.item is not None:
				pass
		except hmod.Inventory.DoesNotExist:

			si = hmod.SaleItem()
			si.product = item
			si.quantity = request.session['cart'][item_id]
			si.transaction = trans
			si.amount = item.specs.price

			si.save()

		item.quantity_on_hand -= 1

	request.session['cart'] = {}


	products = []
	rentals = []

	if trans.saleitem_set.count() > 0:
		for li in trans.saleitem_set.all():
			products.append(li)

	if trans.rentalitem_set.count() > 0:
		for li in trans.rentalitem_set.all():
			rentals.append(li)


	params['products'] = products
	params['rentals'] = rentals


	subject = "Receipt for your purchase"

	body = templater.render(request, 'receipt.html', params)

	send_mail(subject, body, 'derik.hasvold.backup@gmail.com', [request.user.email], html_message = body, fail_silently = False)

	return templater.render_to_response(request, 'confirmation.html', params)