############################################################
#
# Author: John Turner
# Version: 1.2
# Last Updated: 2/28/15
# 
# This file contains the custom widgets that I am creating
# so that the forms are rendered more beautifully in the 
# site. 
#
############################################################

from django import forms
from itertools import chain
from django.conf import settings
from django.utils.translation import ugettext as _
from django.utils.html import conditional_escape, format_html
from django.forms.utils import flatatt, to_current_timezone
from django.forms.widgets import ChoiceFieldRenderer, ChoiceInput
from django.utils.encoding import force_text, python_2_unicode_compatible
from django.utils.safestring import mark_safe

class CustomSelect(forms.Select):
	'''
		This class is overridden so that the Bootstrap Select plugin styling can be applied.
	'''

	def render(self, name, value, attrs=None, choices=()):
		if value is None:
			value = ''
		final_attrs = self.build_attrs(attrs, name=name)
		output = [format_html('<select class="selectpicker"{0}>', flatatt(final_attrs))]
		options = self.render_options(choices, [value])
		if options:
			output.append(options)
		output.append('</select>')
		return mark_safe('\n'.join(output))

	def render_option(self, selected_choices, option_value, option_label):
		if option_value is None:
			option_value = ''
		option_value = force_text(option_value)
		if option_value in selected_choices:
			selected_html = mark_safe(' selected="selected"')
			if not self.allow_multiple_selected:
				# Only allow for a single selection.
				selected_choices.remove(option_value)
		else:
			selected_html = ''
		return format_html('<option value="{0}"{1}>{2}</option>',
						   option_value,
						   selected_html,
						   force_text(option_label))

	def render_options(self, choices, selected_choices):
		# Normalize to strings.
		selected_choices = set(force_text(v) for v in selected_choices)
		output = []
		for option_value, option_label in chain(self.choices, choices):
			if isinstance(option_label, (list, tuple)):
				output.append(format_html('<optgroup label="{0}">', force_text(option_value)))
				for option in option_label:
					output.append(self.render_option(selected_choices, *option))
				output.append('</optgroup>')
			else:
				output.append(self.render_option(selected_choices, option_value, option_label))
		return '\n'.join(output)			

class CustomRadioChoiceInput(ChoiceInput):
	'''
		Custom radio choice input class. I need to override the render method to output hidden text fields and then the 
		polymer paper radio buttons.

		Custom radio choice widget so that it inherits from the correct superclass with the correct tag method.
	'''

	input_type = 'radio'

	def __init__(self, *args, **kwargs):
		super(CustomRadioChoiceInput, self).__init__(*args, **kwargs)
		self.value = force_text(self.value)

	def render(self, name=None, value=None, attrs=None, choices=()):
		if self.id_for_label:
			label_for = format_html(' for="{0}"', self.id_for_label)
		else:
			label_for = ''

		return format_html('<paper-radio-button name="{0}" label="{1}"></paper-radio-button>', self.choice_label, self.choice_label)

class CustomRadioRenderer(ChoiceFieldRenderer):
	'''
		Custom renderer for the radio buttons, using polymer radio elements, rather than normal radio buttons.
		This renderer exists to wrap the the individual elements in a <paper-radio-group> tag. 
	'''

	choice_input_class = CustomRadioChoiceInput
	checked = ''

	## Init method inherited from Choice field renderer ##
	# def __init__(self, name, value, attrs, choices):
 #        self.name = name
 #        self.value = value
 #        self.attrs = attrs
 #        self.choices = choices

	def render(self):
		"""
		Outputs a <paper-radio-group> for this set of choice fields.
		If an id was given to the field, it is applied to the <paper-radio-group> (each
		item in the list will get an id of `$id_$i`).

		Important!!! For each RadioSelect field, you MUST add a hidden text field to the form, 
		and that is what the form will post when applied. There is also a script that will be attached to the 
		widget that will take care of filling the text box with whatever is selected.
		"""

		## CUSTOM CODE ADDED HERE!!! - Figure out which one is checked, then add it to the tag: ##
		for i, choice in enumerate(self.choices):
			w = self.choice_input_class(self.name, self.value, self.attrs.copy(), choice, i)

			if w.is_checked():
				self.checked = w.choice_label

		id_ = self.attrs.get('id', None)

		## If checked is anything other than a blank string, mark the right selection in the paper group tag: ##
		if self.checked != '':
			print('hello')
			start_tag = '<paper-radio-group selected="{0}">'.format(self.checked)
		else:
			start_tag = '<paper-radio-group>'
		output = [start_tag]
		for i, choice in enumerate(self.choices):
			choice_value, choice_label = choice
			if isinstance(choice_label, (tuple, list)):
				attrs_plus = self.attrs.copy()
				if id_:
					attrs_plus['id'] += '_{0}'.format(i)
				sub_ul_renderer = CustomRadioRenderer(name=self.name,
													  value=self.value,
													  attrs=attrs_plus,
													  choices=choice_label)
				sub_ul_renderer.choice_input_class = self.choice_input_class
				output.append(format_html('{0}{1}', choice_value,
										  sub_ul_renderer.render()))
			else:
				w = self.choice_input_class(self.name, self.value,
											self.attrs.copy(), choice, i)
				output.append(format_html('{0}', force_text(w)))
		output.append('</paper-radio-group>')
		return mark_safe('\n'.join(output))