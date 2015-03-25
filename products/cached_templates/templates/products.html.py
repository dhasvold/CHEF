# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426909061.545594
_enable_loop = True
_template_filename = '/Users/John/DevProjects/Repositories/chef/products/templates/products.html'
_template_uri = 'products.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['page_title', 'content', 'tab_title']


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
    return runtime._inherit_from(context, '/base_admin/templates/View.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        bulk_items = context.get('bulk_items', UNDEFINED)
        s_items = context.get('s_items', UNDEFINED)
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'tab_title'):
            context['self'].tab_title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('\n\t\t<div class="row">\n\t\t\t\n')
        __M_writer('\t\t\t<div class="col-md-8">\n\t\t\t\t<h1>View Items</h1>\n\t\t\t</div>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<div class="col-md-4">\n\t\t\t\t<paper-button class="create_button search_button" raised>Search</paper-button>\n\t\t\t</div>\n')
        __M_writer('\n\t\t</div>\n\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        s_items = context.get('s_items', UNDEFINED)
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        bulk_items = context.get('bulk_items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\t\n')
        __M_writer('\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\t<h3 class="table_title">Bulk Items</h3>\n')
        __M_writer('\n')
        for item in bulk_items:
            __M_writer('\n\t\t<div class="item_box">\n\n')
            __M_writer('\t\t\t<a href="/products/products.details/')
            __M_writer(str( item.id ))
            __M_writer('"><h4>')
            __M_writer(str( item.specs.name ))
            __M_writer('</h4></a>\n')
            __M_writer('\n\t\t\t<div class="spacer"></div>\n\t\t\t<div class="spacer"></div>\n\t\t\t<div class="spacer"></div>\n\t\t\t\n')
            __M_writer('\t\t\t<a href="/products/products.details/')
            __M_writer(str( item.id ))
            __M_writer('"><img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer(str( item.specs.photograph.image ))
            __M_writer('" class="product_image"/></a>\n')
            __M_writer('\n\t\t</div>\n\n')
        __M_writer('\n')
        __M_writer('\t<div class="clearfix"></div>\n')
        __M_writer('\n')
        __M_writer('\t<hr>\n')
        __M_writer('\n')
        __M_writer('\t<h3 class="table_title clearfix">Individualized Items</h3>\n')
        __M_writer('\n')
        for item in s_items:
            __M_writer('\n\t\t<div class="item_box">\n\n')
            __M_writer('\t\t\t<a href="/products/products.details/')
            __M_writer(str( item.id ))
            __M_writer('"><h4>')
            __M_writer(str( item.specs.name ))
            __M_writer('</h4></a>\n')
            __M_writer('\n\t\t\t<div class="spacer"></div>\n\t\t\t<div class="spacer"></div>\n\t\t\t<div class="spacer"></div>\n\t\t\t\n')
            __M_writer('\t\t\t<a href="/products/products.details/')
            __M_writer(str( item.id ))
            __M_writer('"><img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer(str( item.specs.photograph.image ))
            __M_writer('" class="product_image"/></a>\n')
            __M_writer('\n\t\t</div>\n\n')
        __M_writer('\n')
        __M_writer('\t<div class="clearfix"></div>\n')
        __M_writer('\n')
        __M_writer('\t<div class="spacer"></div>\n\t<div class="spacer"></div>\n\t<div class="spacer"></div>\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tab_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def tab_title():
            return render_tab_title(context)
        __M_writer = context.writer()
        __M_writer('\n  Products\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "products.html", "filename": "/Users/John/DevProjects/Repositories/chef/products/templates/products.html", "source_encoding": "ascii", "line_map": {"128": 89, "129": 89, "130": 91, "131": 96, "132": 98, "133": 100, "134": 102, "135": 106, "141": 11, "147": 11, "153": 147, "27": 0, "41": 7, "42": 9, "47": 13, "57": 18, "63": 18, "64": 22, "65": 26, "66": 28, "67": 32, "73": 15, "84": 15, "85": 18, "90": 34, "91": 36, "92": 38, "93": 40, "94": 42, "95": 43, "96": 47, "97": 47, "98": 47, "99": 47, "100": 47, "101": 49, "102": 55, "103": 55, "104": 55, "105": 55, "106": 55, "107": 55, "108": 57, "109": 62, "110": 64, "111": 66, "112": 68, "113": 70, "114": 72, "115": 74, "116": 76, "117": 77, "118": 81, "119": 81, "120": 81, "121": 81, "122": 81, "123": 83, "124": 89, "125": 89, "126": 89, "127": 89}}
__M_END_METADATA
"""
