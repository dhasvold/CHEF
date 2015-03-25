'''

	Author: John Turner
	Version: 1.0
	Last Updated: 3/3/2015

	View for the account pages for a given user

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

templater = get_renderer('account')

##########################################################################################
################################### FORM CLASS ###########################################
##########################################################################################

class AccountForm(CustomForm):

	''' Class for the form to be used in editing the user info. '''

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
	title = "My Information"
	link = "account/MyAccount"

	## Form Inputs ##
	username = forms.CharField(required=True, max_length=100)
	first_name = forms.CharField(required=True, max_length=100)
	last_name = forms.CharField(required=True, max_length=100)
	email = forms.EmailField(required=True, max_length=100)
	phone = forms.CharField(required=True, max_length=11)
	address1 = forms.CharField(required=True, max_length=100)
	address2 = forms.CharField(required=False, max_length=100)
	city = forms.CharField(required=True, max_length=100)
	state = forms.ChoiceField(required=True, choices=STATE_CHOICES, widget=CustomSelect)
	ZIP = forms.CharField(required=True)
	security_question = forms.CharField(required=True, max_length=100)
	security_answer = forms.CharField(required=True, max_length=100)

	# Validation for the User name field
	def clean_username(self):

		# Test for short usernames
		if len(self.cleaned_data['username']) < 5:
			raise forms.ValidationError(_("Please enter a username greater than 5 characters."))

		# Test for duplicate usernames	
		user = hmod.User.objects.filter(username = self.cleaned_data['username']).exclude(id=self.request.user.id)

		if user.count() > 0:
			raise forms.ValidationError(_("This username already exists."))
		
		return self.cleaned_data['username']

##########################################################################################
################################ PASSWORD FORM CLASS #####################################
##########################################################################################

class PasswordForm(CustomForm):

	'''
		Form that comes up in the password modal to change the password. 
	'''

	# Don't include the delete button
	delete_button = False

	# Don't include the cancel button
	cancel_button = False

	# Custom action
	custom_action = '/account/MyAccount.change_password/'

	# Custom id for the form
	form_id = "password_form"

	current_password = forms.CharField(required=True, max_length=100, widget=forms.PasswordInput)
	new_password = forms.CharField(required=True, max_length=100, widget=forms.PasswordInput)
	confirm_password = forms.CharField(required=True, max_length=100, widget=forms.PasswordInput)

	def clean(self):

		if self.is_valid():

			# Test to make sure that the previous password is correct
			try:
				user = hmod.User.objects.get(id=self.request.user.id)
			except hmod.User.DoesNotExist:
				HttpResponseRedirect('/homepage/index')

			if user.check_password(self.cleaned_data['current_password']) == False:
				raise forms.ValidationError(_("Incorrect current password"))

			# Test to see if the two passwords are equal
			if self.cleaned_data['new_password'] != self.cleaned_data['confirm_password']:
				raise forms.ValidationError(_("Password entered in confirmation field is different from new password entered."))

			print('<<<<<<<<<<<<<<<<<< passed *')

		return self.cleaned_data	

##########################################################################################
################################# DEFAULT ACTION #########################################
##########################################################################################

@view_function
@login_required(login_url='/homepage/login/')
def process_request(request):
	
	# Define the view bag
	params = {}

	# Grab the user according to the username in the request object
	try:
		user = hmod.User.objects.get(username=request.user.username)
	except hmod.User.DoesNotExist:
		return HttpResponseRedirect('/homepage/login')

	form = AccountForm(request, initial={
		'username': user.username,
		'first_name': user.first_name,
		'last_name': user.last_name,
		'email': user.email,
		'phone': user.phone,
		'address1': user.address.address1,
		'address2': user.address.address2,
		'city': user.address.city,
		'state': user.address.state,
		'ZIP': user.address.ZIP,
		'security_question': user.security_question,
		'security_answer': user.security_answer
	})

	form.fields['username'].widget.attrs['readonly'] = True
	form.fields['first_name'].widget.attrs['readonly'] = True
	form.fields['last_name'].widget.attrs['readonly'] = True
	form.fields['email'].widget.attrs['readonly'] = True
	form.fields['phone'].widget.attrs['readonly'] = True
	form.fields['address1'].widget.attrs['readonly'] = True
	form.fields['address2'].widget.attrs['readonly'] = True
	form.fields['city'].widget.attrs['readonly'] = True
	form.fields['state'].widget.attrs['disabled'] = True
	form.fields['ZIP'].widget.attrs['readonly'] = True
	form.fields['security_question'].widget.attrs['readonly'] = True
	form.fields['security_answer'].widget.attrs['readonly'] = True

	form.disabled = True

	# Add form and user to the view bag
	params['form'] = form
	params['user'] = user

	return templater.render_to_response(request, 'MyAccount.html', params)

##########################################################################################
################################## EDIT USER ACTION ######################################
##########################################################################################

@view_function
@login_required(login_url='/homepage/login/')
def edit(request):
	
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
		user = hmod.User.objects.get(username=request.user.username)
	except hmod.User.DoesNotExist:
		return HttpResponseRedirect('/users/users/')

	form = AccountForm(request, initial={
		'username': user.username,
		'first_name': user.first_name,
		'last_name': user.last_name,
		'email': user.email,
		'phone': user.phone,
		'address1': user.address.address1,
		'address2': user.address.address2,
		'city': user.address.city,
		'state': user.address.state,
		'ZIP': user.address.ZIP,
		'security_question': user.security_question,
		'security_answer': user.security_answer
	})

	if request.method == 'POST':

		# Validate the form
		form = AccountForm(request, request.POST)

		if form.is_valid():

			# Update the object
			user.username = form.cleaned_data['username']
			user.first_name = form.cleaned_data['first_name']
			user.last_name = form.cleaned_data['last_name']
			user.email = form.cleaned_data['email']
			user.phone = form.cleaned_data['phone']
			user.address.address1 = form.cleaned_data['address1']
			user.address.address2 = form.cleaned_data['address2']
			user.address.city = form.cleaned_data['city']
			user.address.state = form.cleaned_data['state']
			user.address.ZIP = form.cleaned_data['ZIP']
			user.security_question = form.cleaned_data['security_question']
			user.security_answer = form.cleaned_data['security_answer']

			# Save it to the database
			user.save()

			# Return user to list
			return HttpResponseRedirect('/account/MyAccount/')

	params['form'] = form

	return templater.render_to_response(request, 'MyAccount.html', params)

##########################################################################################
################################ CREATE USER ACTION ######################################
##########################################################################################

@view_function
def create(request):
	''' 

		Creates a new user. First you have to create an address object and tie the user to the 
		address. 

	'''

	# Delete all users that exist in the database with usernames = ''
	# (when someone starts a user and abandons it)
	users = hmod.User.objects.filter(username='').delete()

	# Delete any new groups that might have been added that need to be deleted:
	group = hmod.Group.objects.filter(name='').delete()

	# Get Guest group for the new people
	try:
		group = hmod.Group.objects.get(name='Guest')
	except Group.DoesNotExist:
		HttpResponseRedirect('/users/users/')

	# Create new Address object with nothing in it
	address = hmod.Address()
	address.address1 = ''
	address.address2 = ''
	address.city = ''
	address.state = ''
	address.ZIP = ''

	address.save()

	user = hmod.User()
	user.username = ''
	user.set_password('')
	user.first_name = ''
	user.last_name = ''
	user.email = ''	
	user.phone = ''
	user.security_question = ''
	user.security_answer = ''

	user.address = address

	# Save to the db
	user.save()

	# Add to group
	group.user_set.add(user)

	# Redirect to the Edit page, with blank info
	return HttpResponseRedirect('/users/users.edit/{}/'.format(user.id))

##########################################################################################
################################ DELETE USER ACTION ######################################
##########################################################################################

@view_function
@login_required(login_url='/homepage/login/')
def delete(request):
	''' Deletes a specific user '''

	# Try catch to see if the user exists	
	try:
		user = hmod.User.objects.get(id=request.urlparams[0])
	except User.DoesNotExist:
		pass # User exists

	user.delete()

	return HttpResponseRedirect('/users/users/')

##########################################################################################
################################ CHECK USERNAME ACTION ###################################
##########################################################################################

@view_function
def check_username(request):
	''' Check the username passed in via AJAX call. '''

	username = request.REQUEST.get('username')

	# check to see if the username exists, apart from the current User
	user = hmod.User.objects.filter(username = username).exclude(id=request.user.id)

	if user.count() > 0:
		return HttpResponse('taken')
	else:
		return HttpResponse('free')

##########################################################################################
################################ CHANGE PASSWORD ACTION ##################################
##########################################################################################

@view_function
def change_password(request):
	''' Modal that pops up to change the password for a user. '''

	# Define the view bag
	params = {}

	# Get the user ID
	user_id = request.user.id

	# Get the user according to ID passed in
	try:
		user = hmod.User.objects.get(id=user_id)
	except hmod.User.DoesNotExist:
		return HttpResponse('failed getting user')

	form = PasswordForm(request)

	form.user_id = user_id

	if request.method == 'POST':

		form = PasswordForm(request, request.POST)

		if form.is_valid():

			## Set the password as the new password
			user.set_password(form.cleaned_data['new_password'])

			user.save()

			## Authenticate
			login_user = authenticate(username=user.username, password=form.cleaned_data['new_password'])

			## Relogin
			login(request, login_user)

			return HttpResponse('''
				<script>
					$( "#password_modal" ).modal("hide");
				</script>
			''')

	params['form'] = form
	params['user'] = user

	return templater.render_to_response(request, 'modal_password.html', params)