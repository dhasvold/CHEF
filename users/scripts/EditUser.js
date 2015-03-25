/**
 *
 * Author: John Turner
 * Version: 1.1
 * Last Updated: 3/4/15
 *
 * Script for the Edit user page. 
 * 
 */    

$(function()
{

	// Listener to test to see if the username is taken via AJAX
	$( '#id_username' ).change(function()
	{
		// Grab the value from the username field
		var username = $( this ).val()
		var id = $( '#user_id' ).val()

		console.log(id)

		// Send the AJAX call
		$.ajax(
		{
			url:'/users/users.check_username/',
			data:
			{
				username: username,
				id: id
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

	// When the form is submitted, grab all of the radio buttons, and 
	// see which is checked. Whichever is checked, add the label to 
	// the hidden field and then submit it. 
	$( 'form' ).submit(function(event)
	{
		// variable for validation:
		var flag = false;
		
		// grab all the buttons
		$( 'paper-radio-button' ).each(function()
		{
			if ($( this ).prop('checked'))
			{
				// set the flag to true
				flag = true;

				// grab the value from the label and set it in the hidden field.
				$( "#group_name" ).val( $( this ).prop('label') )
			}
		});

		// if there was something checked, validate and submit the form
		if (flag) 
		{
			return
		}
		else
		{
			// stop the submission of the form, and show the error 
			event.preventDefault()

			// make the error div visible and add text
			$("#hidden_field_error1").text("Please select a group for the user!").css("display","block");
		}
	});
		
});