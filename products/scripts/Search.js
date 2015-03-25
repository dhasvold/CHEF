/**
 *
 * Author: John Turner
 * Version: 1.0
 * Last Updated: 3/7/15
 *
 * Script for the search modal
 * 
 */

$(function()
{
	// Event listener for the search function in the products page.
	$( '#search_button' ).click(function()
	{
		// Grab the name
		var name = $( '#search_input' ).val()

		console.log(name)

		$.ajax(
		{
			url: '/products/products.search/',
			data:
			{
				name: name
			}
		}).done(function(data)
		{
			console.log(data)
			// If the data returned is 'Product not found', place that in the error div.
			// Else, hide the modal and navigate to the main page.
			if(data === 'Product not found')
			{
				$( '#error' ).css('display','block');
				$( '#error' ).html('*' + data);
				$( '#search_input' ).val('')

			}else
			{
				$( '#search_modal' ).modal('hide');
				window.location.replace(data);
			}
		});
	});
});