/**
 *
 * Author: Derik Hasvold
 * Version: 1.0
 * Last Updated: 3/6/15
 *
 * Script for the product details page.
 *
 */

$(function()
{
	// Event listener for the "Add to Cart Button" -
	// Grabs the item ID from the page (hidden in the button),
	// then grabs the quantity, then pops up a modal with the
	// shopping cart in it.
	$( '.add_button' ).click(function()
	{
		var id      = $( this ).attr('data-pid');
        var due_date = $( '#end_date').val();

		// Call the modal with the shopping cart, passing
		// in the data with the ID and quantity
		$.loadmodal(
		{
			url             :'/account/ShoppingCart.add',
			ajax            :
			{
				data        :
				{
					id      : id,
					rental: true,
                    due_date: due_date,
				}
			},
			width           : '800px',
			title           : 'Shopping Cart',
			id              : 'shopping_cart',
		});
	});
});/**
 * Created by dhasvold on 4/2/15.
 */
