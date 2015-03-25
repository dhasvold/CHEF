/**
 *
 * Author: John Turner
 * Version: 1.0
 * Last Updated: 3/3/15
 *
 * Contains all of the JS for the base template from which ALL templates will inherit.
 */

$(function()
{

	// Submit the form via ajax
	$( '#login_form' ).ajaxForm(function(data) { 
		
		// Grab the modal body in the login form modal and insert HTML
		$( '#login_modal' ).find('.modal-body').html(data)

	});

});