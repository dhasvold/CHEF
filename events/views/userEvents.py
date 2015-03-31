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

@view_function
def process_request(request):
	# Define the view bag
	params = {}

	# Delete all events that exist in the database with names that are blank
	# (when someone starts an event and abandons it)
	events = hmod.Event.objects.filter(name='').delete()

	# also delete all venues that were created in the creation of the events
	venues = hmod.Venue.objects.filter(name='').delete()

	# Grab all the events from the database
	events = hmod.Event.objects.all().order_by('start_date')

	# Add events to the view bag
	params['events'] = events

	return templater.render_to_response(request, 'userEvents.html', params)

@view_function
def eventAreas(request):
	# Define the view bag
	params = {}
	areas_dic = {}

	try:
		events = hmod.Event.objects.get(id=request.urlparams[0])
	except:
		pass
	# Add events to the view bag
	params['events'] = events

	areas = hmod.Area.objects.filter(event_id=request.urlparams[0])


	for area in areas:
		items = hmod.ExpectedSaleItem.objects.filter(area_id=area.id)

		areas_dic[area] = items


	params['areas'] = areas_dic





	return templater.render_to_response(request, 'eventAreas.html', params)