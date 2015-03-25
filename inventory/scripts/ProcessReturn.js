/**
 *
 * Author: John Turner
 * Version: 1.0
 * Last Updated: 3/21/15
 *
 * Script for the page where agents process rental returns. 
 * 
 */

$(function()
{
	// Show modal to change password when the Change Password button is clicked 
	$( '#add_fee' ).click(function()
	{
		var id = $( '#add_fee' ).attr('data-id');

		console.log(id)

		$.loadmodal(
		{
			url: '/inventory/returns.add_fee/' + id,
			title: 'Add Fee',
			width: '600px',
			id: 'fee_modal',
		});
	});
})