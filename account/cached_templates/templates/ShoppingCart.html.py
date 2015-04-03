# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428042381.0822413
_enable_loop = True
_template_filename = '/home/dhasvold/PycharmProjects/chef-master/account/templates/ShoppingCart.html'
_template_uri = 'ShoppingCart.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/base_app/templates/base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        items = context.get('items', UNDEFINED)
        int = context.get('int', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        rentals = context.get('rentals', UNDEFINED)
        request = context.get('request', UNDEFINED)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        items = context.get('items', UNDEFINED)
        int = context.get('int', UNDEFINED)
        def content():
            return render_content(context)
        rentals = context.get('rentals', UNDEFINED)
        request = context.get('request', UNDEFINED)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\t<div class="full-width-container">\n\t\t\n')
        __M_writer('\t\t<div class="row">\n\t\t\t\n')
        __M_writer('\t\t\t<div class="table-responsive">\n\t\t\t\t<table class="table table-hover table-bordered">\n\t\t\t\t\t<thead>\n\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t<th>\n\t\t\t\t\t\t\t\tProduct\n\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t\t<th class="quantity">\n\t\t\t\t\t\t\t\tQuantity\t\n\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t\t<th class="price">\n\t\t\t\t\t\t\t\tPrice\n\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t\t<th>\n\t\t\t\t\t\t\t\tActions\t\n\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t</tr>\n\t\t\t\t\t</thead>\n\t\t\t\t\t<tbody>\n\t\t\t\t\t\t')
        total = 0 
        
        __M_writer('\n')
        for item in items:
            __M_writer('\t\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t\t\t')
            __M_writer(str( item.specs.name ))
            __M_writer('\n\t\t\t\t\t\t\t\t</td>\n\t\t\t\t\t\t\t\t<td class="quantity">\n\t\t\t\t\t\t\t\t\t')
            __M_writer(str( items[item] ))
            __M_writer('\n\t\t\t\t\t\t\t\t</td>\n\t\t\t\t\t\t\t\t<td class="price">\n\t\t\t\t\t\t\t\t\t')
            __M_writer(str( item.specs.price * int(items[item]) ))
            __M_writer('\n\t\t\t\t\t\t\t\t</td>\n\t\t\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t\t\t<paper-button raised data-id="')
            __M_writer(str( item.id ))
            __M_writer('" class="delete_button">Remove</paper-button>\n\t\t\t\t\t\t\t\t</td>\n\t\t\t\t\t\t\t</tr>\n                            ')
            import decimal 
            
            __M_writer('\n\t\t\t\t\t\t\t')
            total += (item.specs.price * decimal.Decimal(items[item])) 
            
            __M_writer('\n')
        __M_writer('\t\t\t\t\t</tbody>\n\t\t\t\t</table>\n\t\t\t</div>\n            ')
        request.session['total'] = {}
        
        __M_writer('\n            ')
        request.session['total'] = str(total) 
        
        __M_writer('\n')
        __M_writer('            <div class="spacer"></div>\n\n\n\n')
        __M_writer('\t\t\t<div class="table-responsive">\n\t\t\t\t<table class="table table-hover table-bordered">\n\t\t\t\t\t<thead>\n\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t<th>\n\t\t\t\t\t\t\t\tRental\n\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t\t<th class="quantity">\n\t\t\t\t\t\t\t\tRental Length\n\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t\t<th class="price">\n\t\t\t\t\t\t\t\tRental Price\n\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t\t<th>\n\t\t\t\t\t\t\t\tActions\n\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t</tr>\n\t\t\t\t\t</thead>\n\t\t\t\t\t<tbody>\n')
        for item1 in rentals:
            __M_writer('\t\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t\t\t')
            __M_writer(str( item1.specs.name ))
            __M_writer('\n\t\t\t\t\t\t\t\t</td>\n\t\t\t\t\t\t\t\t<td class="quantity">\n\t\t\t\t\t\t\t\t\t')
            __M_writer(str( rentals[item1] + ' ' ))
            __M_writer(' days\n\t\t\t\t\t\t\t\t</td>\n\t\t\t\t\t\t\t\t<td class="price">\n                                    ')
            price = item1.standard_rental_price * int(rentals[item1]) 
            
            __M_writer('\n\t\t\t\t\t\t\t\t\t')
            __M_writer(str( price ))
            __M_writer('\n\t\t\t\t\t\t\t\t</td>\n\t\t\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t\t\t<paper-button raised data-id="')
            __M_writer(str( item1.id ))
            __M_writer('" class="delete_button">Remove</paper-button>\n\t\t\t\t\t\t\t\t</td>\n\t\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t\t')
            total += price 
            
            __M_writer('\n')
        __M_writer('\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t<th>\n\t\t\t\t\t\t\t\tTotal Price\n\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t\t<th>\n\n\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t\t<th class="total_price">\n\t\t\t\t\t\t\t\t')
        __M_writer(str( total ))
        __M_writer('\n                                ')
        request.session['total'] = {} 
        
        __M_writer('\n                                ')
        request.session['total'] = str(total) 
        
        __M_writer('\n\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t</tr>\n\t\t\t\t\t</tbody>\n\t\t\t\t</table>\n\t\t\t</div>\n            ')
        request.session['total'] = {}
        
        __M_writer('\n            ')
        request.session['total'] = str(total) 
        
        __M_writer('\n')
        __M_writer('\n\t\t</div>\n')
        __M_writer('\n')
        __M_writer('\t\t<div class="row">\n\t\t\t\n\t\t\t<div class="check_button_cont">\n\t\t\t\t\n\t\t\t\t<a class="button" href="/account/ShoppingCart.checkout/">\n\t\t\t\t\t<paper-button raised class="create_button" id="checkout_button">Check Out</paper-button>\n\t\t\t\t</a>\n\n\t\t\t</div>\n\n\t\t</div>\n')
        __M_writer('\n\t</div>\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/dhasvold/PycharmProjects/chef-master/account/templates/ShoppingCart.html", "line_map": {"128": 145, "134": 128, "27": 0, "39": 7, "40": 9, "50": 11, "61": 11, "62": 14, "63": 17, "64": 20, "65": 39, "67": 39, "68": 40, "69": 41, "70": 43, "71": 43, "72": 46, "73": 46, "74": 49, "75": 49, "76": 52, "77": 52, "78": 55, "80": 55, "81": 56, "83": 56, "84": 58, "85": 61, "87": 61, "88": 62, "90": 62, "91": 64, "92": 69, "93": 88, "94": 89, "95": 91, "96": 91, "97": 94, "98": 94, "99": 97, "101": 97, "102": 98, "103": 98, "104": 101, "105": 101, "106": 104, "108": 104, "109": 106, "110": 114, "111": 114, "112": 115, "114": 115, "115": 116, "117": 116, "118": 122, "120": 122, "121": 123, "123": 123, "124": 125, "125": 128, "126": 130, "127": 142}, "source_encoding": "ascii", "uri": "ShoppingCart.html"}
__M_END_METADATA
"""
