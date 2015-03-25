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
	// Show modal when "Login" link/menu item is clicked, and pull the form from 
	// server. 
	$( '#login_link' ).click(function()
	{
		$.loadmodal(
		{
			url  : '/homepage/login/modal',
			title: 'Login',
			width: '600px',
			id   : 'login_modal'
		});
	});

	// Show the shopping cart modal when the "My Cart" link is clicked
	$( '#cart_link' ).click(function()
	{
		$.loadmodal(
		{
			url: '/account/ShoppingCart/',
			title: 'Shopping Cart',
			id: 'shopping_cart',
			width: '800px'
		});
	});

	// Initialize all jQuery datepickers on the site
	$( '.datepicker' ).datepicker();

	// Initialize all jQuery DateTimePickers on the site
	$( '.datetimepicker' ).datetimepicker();

});