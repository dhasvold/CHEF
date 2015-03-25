# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425771533.929509
_enable_loop = True
_template_filename = '/Users/John/DevProjects/Repositories/chef/account/templates/ShoppingCart.html'
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
            __M_writer('" class="delete_button">Remove</paper-button>\n\t\t\t\t\t\t\t\t</td>\n\t\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t\t')
            total += (item.specs.price * items[item]) 
            
            __M_writer('\n')
        __M_writer('\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t<th>\n\t\t\t\t\t\t\t\tTotal Price\n\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t\t<th>\n\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t\t<th class="total_price">\n\t\t\t\t\t\t\t\t')
        __M_writer(str( total ))
        __M_writer('\n\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t</tr>\n\t\t\t\t\t</tbody>\n\t\t\t\t</table>\n\t\t\t</div>\n')
        __M_writer('\n\t\t</div>\n')
        __M_writer('\n')
        __M_writer('\t\t<div class="row">\n\t\t\t\n\t\t\t<div class="check_button_cont">\n\t\t\t\t\n\t\t\t\t<a class="button" href="/account/ShoppingCart.checkout">\n\t\t\t\t\t<paper-button raised class="create_button" id="checkout_button">Check Out</paper-button>\n\t\t\t\t</a>\n\n\t\t\t</div>\n\n\t\t</div>\n')
        __M_writer('\n\t</div>\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/John/DevProjects/Repositories/chef/account/templates/ShoppingCart.html", "line_map": {"64": 43, "65": 43, "66": 46, "67": 46, "68": 49, "69": 49, "70": 52, "71": 52, "72": 55, "74": 55, "75": 57, "76": 65, "77": 65, "78": 72, "79": 75, "80": 77, "81": 89, "82": 92, "88": 82, "27": 0, "36": 7, "37": 9, "47": 11, "55": 11, "56": 14, "57": 17, "58": 20, "59": 39, "61": 39, "62": 40, "63": 41}, "source_encoding": "ascii", "uri": "ShoppingCart.html"}
__M_END_METADATA
"""
