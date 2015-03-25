'''

	Author: John Turner
	Version: 1.0
	Last Updated: 3/6/2015

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

templater = get_renderer('products')

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
	items = hmod.Inventory.objects.filter(shelf_location='').delete()
	items = hmod.SerializedProduct.objects.filter(shelf_location='').delete()

	# Grab all the inventory items and serialized products from the database
	items = hmod.Inventory.objects.filter(item=None, serializedproduct=None,).order_by('specs__name')

	params['bulk_items'] = items

	items = hmod.SerializedProduct.objects.all().order_by('specs__name')

	params['s_items'] = items

	return templater.render_to_response(request, 'products.html', params)

##########################################################################################
##################################### PRODUCT DETAILS ####################################
##########################################################################################

@view_function
@login_required(login_url='/homepage/login/')
def details(request):
	
	# Define the view bag
	params={}

	try:
		item = hmod.Inventory.objects.get(id=request.urlparams[0])
	except hmod.Inventory.DoesNotExist:
		return HttpResponseRedirect('/products/products/')

	params['item'] = item

	return templater.render_to_response(request, 'ItemDetails.html', params)

##########################################################################################
##################################### SEARCH FORM ACTION #################################
##########################################################################################

@view_function
def search(request):

	# Define the view bag
	params = {}

	# If a name has been passed in, then search for the item and return the details page
	if request.REQUEST.get('name') is not None:

		try:
			product = hmod.Inventory.objects.get(specs__name=request.REQUEST.get('name'),item=None)

			return HttpResponse('/products/products.details/{0}'.format(product.id))

		except hmod.Inventory.DoesNotExist:

			return HttpResponse('Product not found')

	return templater.render_to_response(request, 'Search.html', params)