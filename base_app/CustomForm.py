#############################################################
# Author: John Turner
# Version 2.0
#
# Last Updated: Feb 28, 2015
# 
# This file holds the custom form class that all forms in 
# this site will inherit from. The main purpose of this class
# is to allow me to take full control of how my forms need to be
# rendered.
# 
#############################################################

from django import forms

class CustomForm(forms.Form):

	title = ''
	request = ''
	link = ''

	# Custom action, if desired
	custom_action = ''

	# ID passed in if desired
	form_id = ''

	# Determines if the buttons need extra parameters from the URL
	needs_params = False
	
	# For use in the delete button
	delete_type = ''

	# Variable that determines whether to include the delete button or not
	delete_button = True

	# Variable that determines whether to include the cancel button or not
	cancel_button = True

	# Variable to set the fields as disabled
	# NOTE! - Also removes the buttons on the bottom of the form, and includes
	# an "Edit" button. 
	disabled = False

	# Variable for the Submit button text (default = 'Submit')
	submit_text = 'Submit'

	# Variable for the iteration through loops, so as to add unique ID's.
	iterator = 1

	def __init__(self, request, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.request = request

	def as_table(self):

		# Grab list of the form errors to begin
		form_errors = self.non_field_errors()

		# List for the HTML to be put together throughout the function
		html=[]

		## FORM TITLE ##
		html.append('<h3>{0}</h3>'.format(self.title))

		## Test to see if there are any file fields or image fields in the form
		## If so, then add a 'enctype' to the form tag:
		for field in self.visible_fields():

			if self.is_multipart():
				if self.form_id != '':
					if self.custom_action != '':
						html.append('<form enctype="multipart/form-data" id="{0}" method="POST" action="{1}">'.format(self.form_id, self.custom_action))	
					else: 
						html.append('<form enctype="multipart/form-data" id="{0}" method="POST">'.format(self.form_id))	
				else:
					if self.custom_action != '':
						html.append('<form enctype="multipart/form-data" method="POST" action="{0}">'.format(self.custom_action))
					else:
						html.append('<form enctype="multipart/form-data" method="POST">')
			else:
				if self.form_id != '':
					if self.custom_action != '':
						html.append('<form id="{0}" method="POST" action="{1}">'.format(self.form_id, self.custom_action))
					else:
						html.append('<form id="{0}" method="POST">'.format(self.form_id))
				else:
					if self.custom_action != '':
						html.append('<form method="POST" action="{0}">'.format(self.custom_action))
					else:
						html.append('<form method="POST">')

		## IF FORM ERRORS OCCUR ##
		if form_errors:

			## START DIV FOR ERRORS ##
			html.append('<div class="form_errors">')

			for error in form_errors:
				html.append('<p class="form_error">*{0}</p>'.format(error))

			## END DIV FOR ERRORS ##
			html.append('</div>')

		## HIDDEN FIELDS ##
		for field in self.hidden_fields():
			
			## BEGIN ROW ##
			html.append('<div class="row">')

			## BEGIN FIELD COLUMN ##
			html.append('<div class="col-md-8">')

			html.append('<div class="hidden_fields">{0}</div>'.format(field))
			## ERRORS ##
			html.append('<div class="hidden_field_error" id="hidden_field_error{0}"></div>'.format(self.iterator))

			## END FIELD COLUMN ##
			html.append('</div>')

			## END ROW ##
			html.append('</div>')

			self.iterator += 1

		## FOR LOOP TO LOOP OVER THE FORMS FIELD ##
		for field in self.visible_fields():

			## BEGIN ROW ##
			html.append('<div class="row">')

			## BEGIN FIELD COLUMN ##
			html.append('<div class="col-md-7">')

			## If the field is a text-input field, then wrap it with the text input decorator
			if field.field.widget.__class__.__name__ == 'TextInput' or field.field.widget.__class__.__name__ == 'EmailInput' or field.field.widget.__class__.__name__ == 'PasswordInput' or field.field.widget.__class__.__name__ == 'NumberInput':
				
				## TEXT INPUT FIELDS ##
				if self.disabled:
					html.append('<paper-input-decorator floatingLabel label="{0}" disabled="{1}">'.format(field.label, self.disabled))
				else:
					html.append('<paper-input-decorator floatingLabel label="{0}">'.format(field.label))
				html.append('{0}'.format(field))
				html.append('</paper-input-decorator>')

			## for all other fields, don't use the decorator
			else:
				html.append('<p class="input_label">{0}</p>'.format(field.label))
				html.append('{0}'.format(field))
			
			## END FIELD COLUMN ##
			html.append('</div>')

			## IF FIELD ERRORS OCCUR ##
			if field.errors:

				## BEGIN ERROR COLUMN ##
				html.append('<div class="col-md-5">')
				
				label = field.label.replace(' ', '_').lower()

				## ERRORS ##
				html.append('<div class="field_error" id="error_{0}">{1}</div>'.format(label, field.errors.as_text()))

				## END ERROR COLUMN ##
				html.append('</div>')

			## END ROW ##
			html.append('</div>')

		if self.disabled:

			## EDIT BUTTON ##
			html.append('<a class="button" href="/{0}.edit/"><paper-button raised class="edit_button">Edit Information</paper-button></a>'.format(self.link))

		else:
			## SUBMIT BUTTON ## 
			html.append('<paper-button raised class="success_button form_button"><button type="submit">{0}</button></paper-button>'.format(self.submit_text))

			if self.delete_button:

				## DELETE BUTTON ##
				if self.needs_params:
					html.append('<a class="button" href="/{0}.delete{1}/{2}/{3}"><paper-button raised class="delete_button">Delete</paper-button></a>'.format(self.link, self.delete_type, self.request.urlparams[0], self.request.urlparams[1]))
				else:
					html.append('<a class="button" href="/{0}.delete{1}/{2}"><paper-button raised class="delete_button">Delete</paper-button></a>'.format(self.link, self.delete_type, self.request.urlparams[0]))

			if self.cancel_button:

				## CANCEL BUTTON ##
				if self.needs_params:
					html.append('<a class="button" href="/{0}/{1}"><paper-button raised class="create_button">Cancel</paper-button></a>'.format(self.link, self.request.urlparams[0]))
				else:
					html.append('<a class="button" href="/{0}"><paper-button raised class="create_button">Cancel</paper-button></a>'.format(self.link))

		## END FORM ##
		html.append('</form>')

		## MAKE STRING OUT OF HTML LIST ##
		finished_html = ''.join(html)

		return finished_html

	## This function is to be called for the login page specifically
	def as_login(self):

		# List for the HTML to be put together throughout the function
		html=[]

		## BEGIN FORM ##
		
		# If self.modal = True, return the modal action
		# If false, return with no action
		
		if self.modal:
			html.append('<form id="login_form" method="POST" action="/homepage/login/modal/">')
		else:
			html.append('<form id="login_form" method="POST">')

		form_errors = self.non_field_errors()

		## IF FORM ERRORS OCCUR ##
		if form_errors:

			## START DIV FOR ERRORS ##
			html.append('<div class="form_errors">')

			for error in form_errors:
				html.append('<p class="form_error">*{0}</p>'.format(error))

			## END DIV FOR ERRORS ##
			html.append('</div>')

		## HIDDEN FIELDS
		for field in self.hidden_fields():
			html.append('div class="hidden_fields">{0}</div'.format(field))

		## FOR LOOP TO LOOP OVER THE FORMS FIELD ##
		for field in self.visible_fields():

			## IF FIELD ERRORS OCCUR ##
			if field.errors:
			
				## ERRORS ##
				html.append('<div class="field_error">{0}</div>'.format(field.errors.as_text()))

			## FIELDS ##
			html.append('<paper-input-decorator floatingLabel label="{0}">'.format(field.label))
			html.append('{0}'.format(field))
			html.append('</paper-input-decorator>')

		## SUBMIT BUTTON ## 
		html.append('<paper-button raised class="success_button form_button"><button type="submit">Submit</button></paper-button>')

		## END FORM ##
		html.append('</form>')

		## MAKE STRING OUT OF HTML LIST ##
		finished_html = ''.join(html)

		return finished_html

	def as_event_form(self):

		# Grab list of the form errors to begin
		form_errors = self.non_field_errors()

		# List for the HTML to be put together throughout the function
		html=[]

		## FORM TITLE ##
		html.append('<h3>{0}</h3>'.format(self.title))

		## BEGIN FORM ##
		html.append('<form method="POST">')

		## IF FORM ERRORS OCCUR ##
		if form_errors:

			## START DIV FOR ERRORS ##
			html.append('<div class="form_errors">')

			for error in form_errors:
				html.append('<p class="form_error">*{0}</p>'.format(error))

			## END DIV FOR ERRORS ##
			html.append('</div>')

		## HIDDEN FIELDS
		for field in self.hidden_fields():
			html.append('div class="hidden_fields">{0}</div'.format(field))

		## FOR LOOP TO LOOP OVER THE FORMS FIELD ##
		for field in self.visible_fields():

			## BEGIN ROW ##
			html.append('<div class="row">')

			## BEGIN FIELD COLUMN ##
			## If there are errors, change the layout of the page to fit them
			if field.errors:
				html.append('<div class="col-md-5">')
			else:
				html.append('<div class="col-md-8">')

			## FIELDS ##
			html.append('<paper-input-decorator floatingLabel label="{0}">'.format(field.label))
			html.append('{0}'.format(field))
			html.append('</paper-input-decorator>')
			
			## END FIELD COLUMN ##
			html.append('</div>')

			## IF FIELD ERRORS OCCUR ##
			if field.errors:

				## BEGIN ERROR COLUMN ##
				html.append('<div class="col-md-7">')
				
				## ERRORS ##
				html.append('<div class="field_error">{0}</div>'.format(field.errors.as_text()))

				## END ERROR COLUMN ##
				html.append('</div>')

			## END ROW ##
			html.append('</div>')

		## SUBMIT BUTTON ## 
		html.append('<paper-button raised class="success_button form_button"><button type="submit">Submit</button></paper-button>')

		## DELETE BUTTON ##
		html.append('<a class="button" href="' + self.link +'.delete/' + self.request.urlparams[0] + '"><paper-button raised class="delete_button">Delete</paper-button></a>')

		## CANCEL BUTTON ##
		html.append('<a class="button" href="' + self.link + '"><paper-button raised class="create_button">Cancel</paper-button></a>')

		## VIEW AREAS BUTTON ##
		html.append('<a class="button" href="/events/areas/' + self.request.urlparams[0] +'"><paper-button raised class="edit_button" form_button">View Areas</paper-button></a>')

		## VIEW AREAS BUTTON ##
		html.append('<a class="button" href="/events/venues.create/"><paper-button raised class="edit_button" form_button">Add Venue</paper-button></a>')

		## END FORM ##
		html.append('</form>')

		## MAKE STRING OUT OF HTML LIST ##
		finished_html = ''.join(html)

		return finished_html