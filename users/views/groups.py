'''

	Author: John Turner
	Version: 1.0
	Last Updated: 2/5/2015

	View for all CRUD functions for the groups.

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

templater = get_renderer('users')

##########################################################################################
################################### FORM CLASS ###########################################
##########################################################################################

class EditGroupForm(CustomForm):

	''' Class for the form to be used in editing the groups. '''

	## Class title ##
	title = "Group Information"
	link = "users/groups"

	## Form Inputs ##
	name = forms.CharField(required=True, max_length=100)

	## Add permissions back in later when I can get this to work...
	# permissions = forms.ModelChoiceField(queryset=hmod.Permission.objects.all(), widget=forms.CheckboxSelectMultiple, empty_label=None)
	
	# Validation for the name of the group, make sure there aren't duplicates
	def clean_name(self):

		# Test for duplicate names	
		group = hmod.Group.objects.filter(name = self.cleaned_data['name']).exclude(id=self.request.urlparams[0])

		if group.count() > 0:
			raise forms.ValidationError("This name already exists.")
		
		return self.cleaned_data['name']

##########################################################################################
################################# DEFAULT ACTION #########################################
##########################################################################################

@view_function
@permission_required('auth.change_group', login_url='/homepage/login/')
def process_request(request):
	
	# Define the view bag
	params = {}

	# Delete all groups that exist in the database with names = ''
	# (when someone starts a user and abandons it)
	groups = hmod.Group.objects.filter(name='').delete()

	# Grab all the groups from the database
	groups = hmod.Group.objects.all().order_by('name')

	# Add groups to the view bag
	params['groups'] = groups

	return templater.render_to_response(request, 'groups.html', params)

##########################################################################################
#################################### EDIT ACTION #########################################
##########################################################################################

@view_function
@permission_required('auth.change_group', login_url='/homepage/login/')
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
		group = hmod.Group.objects.get(id=request.urlparams[0])
	except hmod.Group.DoesNotExist:
		return HttpResponseRedirect('/users/groups/')

	# Pass in group data to the form
	form = EditGroupForm(request, initial={
		'name': group.name,
		# 'permissions': group.permissions.all()
		})

	if request.method == 'POST':

		# Validate the form
		form = EditGroupForm(request, request.POST)

		if form.is_valid():

			# Update the object
			group.name = form.cleaned_data['name']

			# Permissions for group

			# Save it to the database
			group.save()

			# Return user to list
			return HttpResponseRedirect('/users/groups/')

	params['form'] = form

	return templater.render_to_response(request, 'EditGroup.html', params)

##########################################################################################
################################ CREATE USER ACTION ######################################
##########################################################################################

@view_function
@permission_required('auth.add_group', login_url='/homepage/login/')
def create(request):
	''' Creates a new group '''

	group = hmod.Group()
	group.name = ''

	# Save to the db
	group.save()

	# Redirect to the Edit page, with blank info
	return HttpResponseRedirect('/users/groups.edit/{0}/'.format(group.id))

##########################################################################################
################################ DELETE USER ACTION ######################################
##########################################################################################

@view_function
@permission_required('auth.delete_group', login_url='/homepage/login/')
def delete(request):
	''' Deletes a specific user '''

	# Try catch to see if the group exists
	print(request.urlparams[0])
	
	try:
		group = hmod.Group.objects.get(id=request.urlparams[0])
	except Group.DoesNotExist:
		pass # Group exists

	group.delete()

	return HttpResponseRedirect('/users/groups/')