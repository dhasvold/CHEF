'''

	Author: John Turner
	Version: 1.0
	Last Updated: 3/6/2015

	View that controls the flow for a guest to create an account.

'''

from django.conf import settings
from base_app.CustomForm import CustomForm
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from django.contrib.auth.decorators import permission_required
import base_app.models as hmod
from django_mako_plus.controller.router import get_renderer
from django.utils.translation import ugettext as _
from base_app.CustomWidgets import CustomSelect, CustomRadioRenderer
from django.contrib.auth import authenticate, login, logout

templater = get_renderer('account')

##########################################################################################
################################### FORM CLASS ###########################################
##########################################################################################

class NewUserForm(CustomForm):

	''' Class for the form to be used in signing up a new user. '''

	# List of constants for the states:
	ALASKA = 'AK'
	ALABAMA = 'AL'
	ARKANSAS = 'AR'
	ARIZONA = 'AZ'
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
		(ARIZONA, 'Arizon'),
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
	title = "User Information"
	link = "homepage/index"
	delete_button = False

	## Form Inputs ##
	username = forms.CharField(required=True, max_length=100)
	password = forms.CharField(required=True, max_length=100, widget=forms.PasswordInput)
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
		user = hmod.User.objects.filter(username = self.cleaned_data['username'])

		if user.count() > 0:
			raise forms.ValidationError(_("This username already exists."))
		
		return self.cleaned_data['username']

##########################################################################################
################################# DEFAULT ACTION #########################################
##########################################################################################

@view_function
def process_request(request):
	
	# Define the view bag
	params={}

	# Layout of the urls:
	# 
	# /homepage/user.edit/a/b/c/d/e...
	# 
	# request.urlparams[n] = everything after the <appname>/<filename>/
	# 
	# For example [0] = a, [1] = b... 

	# new form for the new user
	form = NewUserForm(request)

	if request.method == 'POST':

		# Validate the form
		form = NewUserForm(request, request.POST)

		if form.is_valid():

			# Create a new user object and a new address object, and pass the information in
			address = hmod.Address()
			address.address1 = form.cleaned_data['address1']
			address.address2 = form.cleaned_data['address2']
			address.city = form.cleaned_data['city']
			address.state = form.cleaned_data['state']
			address.ZIP = form.cleaned_data['ZIP']

			address.save()

			user = hmod.User()

			user.username = form.cleaned_data['username']
			user.set_password(form.cleaned_data['password'])
			user.first_name = form.cleaned_data['first_name']
			user.last_name = form.cleaned_data['last_name']
			user.email = form.cleaned_data['email']
			user.phone = form.cleaned_data['phone']
			user.security_question = form.cleaned_data['security_question']
			user.security_answer = form.cleaned_data['security_answer']

			user.address = address

			# Save it to the database
			user.save()

			# Add the user to the Guest group
			try:
				group = hmod.Group.objects.get(name='Guest')
			except hmod.Group.DoesNotExist:
				return HttpResponseRedirect('/homepage/index/')
			
			group.user_set.add(user)

			# Log the user in
			authenticated_user = authenticate(username=user.username, password=form.cleaned_data['password'])

			login(request, authenticated_user)

			# Return user to list
			return HttpResponseRedirect('/homepage/index/')

	params['form'] = form

	return templater.render_to_response(request, 'NewUser.html', params)

##########################################################################################
################################ CHECK USERNAME ACTION ###################################
##########################################################################################

@view_function
def check_username(request):
	''' Check the username passed in via AJAX call. '''

	username = request.REQUEST.get('username')

	# check to see if the username exists
	user = hmod.User.objects.filter(username = username)

	if user.count() > 0:
		return HttpResponse('taken')
	else:
		return HttpResponse('free')