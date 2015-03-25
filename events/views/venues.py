'''

	Author: John Turner
	Version: 1.0
	Last Updated: 2/4/2015

	View for all CRUD functions for the Venues.

'''

from django.conf import settings
from base_app.CustomForm import CustomForm
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import base_app.models as hmod
from django.contrib.auth.decorators import permission_required
from django_mako_plus.controller.router import get_renderer
from django.utils.translation import ugettext as _

templater = get_renderer('events')

##########################################################################################
################################### FORM CLASS ###########################################
##########################################################################################

class EditVenueForm(CustomForm):

	''' Class for the form to be used in editing the users. '''

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
	title = "Venue Information"

	## Other variables ##
	link = '/events/venues'

	name = forms.CharField(required=True, max_length=100)
	address = forms.CharField(required=True, max_length=100)
	city = forms.CharField(required=True, max_length=100)
	state = forms.ChoiceField(required=True, choices=STATE_CHOICES, widget=forms.Select)
	ZIP = forms.CharField(required=True, max_length=100)
	
	## Clean functions
	
	# Validate Name field, make sure no two names exist in the DB
	def clean_name(self):

		# Test for duplicate usernames	
		venue = hmod.Venue.objects.filter(name = self.cleaned_data['name']).exclude(id=self.request.urlparams[0])

		if venue.count() > 0:
			raise forms.ValidationError(_("This venue name already exists."))
		
		return self.cleaned_data['name']

	# Test to see if the same address + city + state exists in the DB
	def clean(self):

		address = self.cleaned_data['address']
		city = self.cleaned_data['city']
		state = self.cleaned_data['state']

		venue = hmod.Venue.objects.filter(address=address).filter(city=city).filter(state=state)

		if venue.count() > 0:
			raise forms.ValidationError(_("This venue already exists in the database. It's called: {0}").format(venue[0].name))

		return self.cleaned_data


##########################################################################################
#################################### DEFAULT ACTION ######################################
##########################################################################################

@view_function
@permission_required(['base_app.change_venue'], login_url='/homepage/login/')
def process_request(request):
	
	# Define the view bag
	params = {}

	# Delete all venues that exist in the database with usernames = ''
	# (when someone starts a venue and abandons it)
	venues = hmod.Venue.objects.filter(name='').delete()

	# Grab all the venues from the database
	venues = hmod.Venue.objects.all().order_by('name')

	# Add venues to the view bag
	params['venues'] = venues

	return templater.render_to_response(request, 'venues.html', params)

##########################################################################################
################################# EDIT VENUE ACTION ######################################
##########################################################################################

@view_function
@permission_required(['base_app.change_venue'], login_url='/homepage/login/')
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
		venue = hmod.Venue.objects.get(id=request.urlparams[0])
	except hmod.Venue.DoesNotExist:
		return HttpResponseRedirect('/events/venues/')

	# Pass in user data to the form
	form = EditVenueForm(request, initial={
		'name': venue.name,
		'address': venue.address,
		'city': venue.city,
		'state': venue.state,
		'ZIP': venue.ZIP,
		})

	if request.method == 'POST':

		# Validate the form
		form = EditVenueForm(request, request.POST)

		if form.is_valid():

			# Update the object
			venue.name = form.cleaned_data['name']
			venue.address = form.cleaned_data['address']
			venue.city = form.cleaned_data['city']
			venue.state = form.cleaned_data['state']
			venue.ZIP = form.cleaned_data['ZIP']

			# Save it to the database
			venue.save()

			# Return user to list
			return HttpResponseRedirect('/events/venues/')

	params['form'] = form

	return templater.render_to_response(request, 'EditVenue.html', params)

##########################################################################################
################################ CREATE USER ACTION ######################################
##########################################################################################

@view_function
@permission_required(['base_app.add_venue'], login_url='/homepage/login/')
def create(request):
	''' Creates a new venue '''

	# Delete all venues that exist in the database with usernames = ''
	# (when someone starts a venue and abandons it)
	venues = hmod.Venue.objects.filter(name='').delete()

	venue = hmod.Venue()
	venue.address = ''
	venue.city = ''
	venue.state = ''
	venue.ZIP = ''
	venue.security_question = ''

	# Save to the db
	venue.save()

	# Redirect to the Edit page, with blank info
	return HttpResponseRedirect('/events/venues.edit/{}/'.format(venue.id))

##########################################################################################
################################ DELETE USER ACTION ######################################
##########################################################################################

@view_function
@permission_required(['base_app.delete_venue'], login_url='/homepage/login/')
def delete(request):
	''' Deletes a specific venue '''

	# Try catch to see if the user exists
	try:
		venue = hmod.Venue.objects.get(id=request.urlparams[0])
	except Venue.DoesNotExist:
		pass # Venue exists

	venue.delete()

	return HttpResponseRedirect('/events/venues/')