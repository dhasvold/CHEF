/**
 *
 * Author: John Turner
 * Version: 1.0
 * Last Updated: 3/6/15
 *
 * Script for the shopping cart
 * 
 */

$(function()
{
	// Event listener for the Remove Item buttons
	$( '.delete_button' ).click(function()
	{
		var id = $( this ).attr('data-id')
		$.ajax(
		{
			url: '/account/ShoppingCart.remove/',
			data: 
			{
				id: id
			}
		}).done(function(data)
		{
			$( '#shopping_cart' ).find('.modal-body').html(data);
		});
	});

});