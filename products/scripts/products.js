/**
 *
 * Author: John Turner
 * Version: 1.0
 * Last Updated: 3/7/15
 *
 * Script for the overall products page.
 * 
 */

$(function()
{
	// Event listener for the search function in the products page.
	$( '.search_button' ).click(function()
	{
		$.loadmodal(
		{
			url: '/products/products.search/',
			width: '600px',
			title: 'Search',
			id: 'search_modal',
		})
	});
});