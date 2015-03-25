/**
 *
 * Author: John Turner
 * Version: 1.0
 * Last Updated: 3/6/15
 *
 * Script for the page where a guest can create a user account
 * 
 */

$(function()
{
	// Function to test to see if the username is taken via AJAX
	$( '#id_username' ).change(function()
	{
		// Grab the value from the username field
		var username = $( this ).val()

		// Send the AJAX call
		$.ajax(
		{
			url:'/account/NewUser.check_username',
			data:
			{
				username: username
			}
		}).done(function(data)
		{
			// If the data is "taken", then show an error
			// First remove the isInvalid attribute
			$( '#id_username' ).parent().removeAttr('error').removeAttr('isInvalid');

			if(data == "taken")
			{
				$( '#id_username' ).parent().attr('isInvalid', 'True').attr('error', 'This username is taken');
			}
		});
	});

})