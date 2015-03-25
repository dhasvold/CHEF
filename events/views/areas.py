'''

	Author: John Turner
	Version: 1.0
	Last Updated: 2/4/2015

	View for all CRUD functions for the Areas for a given Event.

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
from django.utils import timezone
from django.utils.translation import ugettext as _

templater = get_renderer('events')

##########################################################################################
################################### FORM CLASS ###########################################
##########################################################################################

class EditAreaForm(CustomForm):

	''' Class for the form to be used in editing the areas. '''

	## Class title ##
	title = "Area Information"
	link = '/events/areas'
	needs_params = True

	name = forms.CharField(required=True, max_length=100)
	description = forms.CharField(widget=forms.Textarea(attrs={'rows' : 3}), max_length=250)
	place_number = forms.IntegerField(max_value=100, min_value=1)

	## Clean functions ##

	# Make sure a given event doesn't have multiple areas with the same place_number
	def clean_place_number(self):

		# Grab the event from database
		try:
			event = hmod.Event.objects.get(id=self.request.urlparams[0])
		except Event.DoesNotExist:
			return HttpResponseRedirect('/events/events/')

		# Get a list of the areas for a given event
		areas = hmod.Area.objects.filter(event=event)

		# If there are any areas returned:
		if areas.count() > 0:

			# Test the place_number against the ones in the list returned
			for area in areas:

				if area.place_number == self.cleaned_data['place_number']:

					raise forms.ValidationError(_("This place number already exists for {0}").format(event.name))

		return self.cleaned_data['place_number']


##########################################################################################
################################# DEFAULT ACTION #########################################
##########################################################################################

@view_function
@permission_required(['base_app.change_area'], login_url='/homepage/login/')
def process_request(request):
	
	# Define the view bag
	params = {}

	# Delete all areas that exist in the database with names that are blank
	# (when someone starts an event and abandons it)
	areas = hmod.Area.objects.filter(name='').delete()

	# Grab all the areas from the database related to the event that you're editing
	areas = hmod.Area.objects.filter(event_id=request.urlparams[0]).order_by('place_number')

	# Grab event to pass in
	try:
		event = hmod.Event.objects.get(id=request.urlparams[0])
	except Event.DoesNotExist:
		return HttpResponseRedirect('/events/events')

	params['event'] = event

	# Add areas to the view bag
	params['areas'] = areas

	return templater.render_to_response(request, 'areas.html', params)

##########################################################################################
###################################### EDIT ACTION #######################################
##########################################################################################

@view_function
@permission_required(['base_app.change_area'], login_url='/homepage/login/')
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
		area = hmod.Area.objects.get(id=request.urlparams[1])
	except hmod.Area.DoesNotExist:
		return HttpResponseRedirect('/events/areas/')

	# Pass in area data to the form
	form = EditAreaForm(request, initial={
		'name': area.name,
		'description': area.description,
		'place_number': area.place_number,
		})

	if request.method == 'POST':

		# Validate the form
		form = EditAreaForm(request, request.POST)

		if form.is_valid():

			# Update the object
			area.name = form.cleaned_data['name']
			area.description = form.cleaned_data['description']
			area.place_number = form.cleaned_data['place_number']

			# Save it to the database
			area.save()

			# Return user to list
			return HttpResponseRedirect('/events/areas/{0}'.format(request.urlparams[0]))

	params['form'] = form

	return templater.render_to_response(request, 'EditArea.html', params)

##########################################################################################
##################################### CREATE ACTION ######################################
##########################################################################################

@view_function
@permission_required(['base_app.add_area'], login_url='/homepage/login/')
def create(request):
	''' Creates a new area '''

	# Delete all areas that exist in the database with names that are blank
	# (when someone starts an event and abandons it)
	areas = hmod.Area.objects.filter(name='').delete()

	# Grab event to tie to area
	try:
		event = hmod.Event.objects.get(id=request.urlparams[0])
	except Event.DoesNotExist:
		return HttpResponseRedirect('events/areas/{0}'.format(request.urlparams[0]))

	area = hmod.Area()
	area.name = ''
	area.description = ''
	area.place_number = 0
	area.event = event

	# Save to the db
	area.save()

	# Redirect to the Edit page, with blank info
	return HttpResponseRedirect('/events/areas.edit/{0}/{1}'.format(request.urlparams[0], area.id))

##########################################################################################
##################################### DELETE ACTION ######################################
##########################################################################################

@view_function
@permission_required(['base_app.delete_area'], login_url='/homepage/login/')
def delete(request):
	''' Deletes a specific area '''

	# Try catch to see if the area exists	
	try:
		area = hmod.Area.objects.get(id=request.urlparams[1])
	except Area.DoesNotExist:
		pass # Area exists

	area.delete()

	return HttpResponseRedirect('/events/areas/{0}'.format(request.urlparams[0]))