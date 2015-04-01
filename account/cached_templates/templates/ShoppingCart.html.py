# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427919156.7993147
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
        int = context.get('int', UNDEFINED)
        items = context.get('items', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
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
        int = context.get('int', UNDEFINED)
        items = context.get('items', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context)
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
            __M_writer('" class="delete_button">Remove</paper-button>\n\t\t\t\t\t\t\t\t</td>\n\t\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t\t')
            total += (item.specs.price * items[item]) 
            
            __M_writer('\n')
        __M_writer('\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t<th>\n\t\t\t\t\t\t\t\tTotal Price\n\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t\t<th>\n\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t\t<th class="total_price">\n\t\t\t\t\t\t\t\t')
        __M_writer(str( total ))
        __M_writer('\n                                ')
        request.session['total'] = {} 
        
        __M_writer('\n                                ')
        request.session['total'] = str(total) 
        
        __M_writer('\n\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t</tr>\n\t\t\t\t\t</tbody>\n\t\t\t\t</table>\n\t\t\t</div>\n')
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
{"line_map": {"65": 39, "66": 40, "67": 41, "68": 43, "69": 43, "70": 46, "71": 46, "72": 49, "73": 49, "74": 52, "75": 52, "76": 55, "78": 55, "79": 57, "80": 65, "81": 65, "82": 66, "84": 66, "85": 67, "87": 67, "88": 74, "89": 77, "90": 79, "27": 0, "92": 94, "98": 92, "91": 91, "38": 7, "39": 9, "49": 11, "59": 11, "60": 14, "61": 17, "62": 20, "63": 39}, "source_encoding": "ascii", "uri": "ShoppingCart.html", "filename": "/home/dhasvold/PycharmProjects/chef-master/account/templates/ShoppingCart.html"}
__M_END_METADATA
"""
