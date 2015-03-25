/**
 *
 * Author: John Turner
 * Version: 1.0
 * Last Updated: 3/4/15
 *
 * JS for the password form when editing Users. 
 */

$(function()
{
	// Submit the form via ajax
	$( '#password_form' ).ajaxForm(function(data)
	{
		// Grab the modal body in the login form modal and insert HTML
		$( '#password_modal' ).find('.modal-body').html(data);
	});

});