# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426904638.070237
_enable_loop = True
_template_filename = '/Users/John/DevProjects/Repositories/chef/rentals/templates/rentals.html'
_template_uri = 'rentals.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'tab_title', 'page_title']


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
        non_wardrobe = context.get('non_wardrobe', UNDEFINED)
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        wardrobe = context.get('wardrobe', UNDEFINED)
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        non_wardrobe = context.get('non_wardrobe', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def page_title():
            return render_page_title(context)
        wardrobe = context.get('wardrobe', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\t\n')
        __M_writer('\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\t<h3 class="table_title">Non Wardrobe Items</h3>\n')
        __M_writer('\n')
        for item in non_wardrobe:
            __M_writer('\n\t\t<div class="item_box">\n\n')
            __M_writer('\t\t\t<a href="/rentals/rentals.details/')
            __M_writer(str( item.id ))
            __M_writer('"><h4>')
            __M_writer(str( item.specs.name ))
            __M_writer('</h4></a>\n')
            __M_writer('\n\t\t\t<div class="spacer"></div>\n\t\t\t\n')
            __M_writer('\t\t\t<a href="/rentals/rentals.details/')
            __M_writer(str( item.id ))
            __M_writer('"><img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer(str( item.specs.photograph.image ))
            __M_writer('" class="rental_image"/></a>\n')
            __M_writer('\n\t\t</div>\n\n')
        __M_writer('\n')
        __M_writer('\t<div class="clearfix"></div>\n')
        __M_writer('\n')
        __M_writer('\t<hr>\n')
        __M_writer('\n')
        __M_writer('\t<h3 class="table_title clearfix">Wardrobe Items</h3>\n')
        __M_writer('\n')
        for item in wardrobe:
            __M_writer('\n\t\t<div class="item_box">\n\n')
            __M_writer('\t\t\t<a href="/rentals/rentals.details/')
            __M_writer(str( item.id ))
            __M_writer('"><h4>')
            __M_writer(str( item.specs.name ))
            __M_writer('</h4></a>\n')
            __M_writer('\n\t\t\t<div class="spacer"></div>\n\t\t\t\n')
            __M_writer('\t\t\t<a href="/rentals/rentals.details/')
            __M_writer(str( item.id ))
            __M_writer('"><img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer(str( item.specs.photograph.image ))
            __M_writer('" class="rental_image"/></a>\n')
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
        __M_writer('\n  \tRentals\n')
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
        __M_writer('\t\t\t<div class="col-md-8">\n\t\t\t\t<h1>View Rentals Available</h1>\n\t\t\t</div>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<div class="col-md-4">\n\t\t\t\t<paper-button class="create_button search_button" raised>Search</paper-button>\n\t\t\t</div>\n')
        __M_writer('\n\t\t</div>\n\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"131": 11, "137": 18, "143": 18, "144": 22, "145": 26, "146": 28, "147": 32, "153": 147, "27": 0, "41": 7, "42": 9, "47": 13, "57": 15, "68": 15, "69": 18, "74": 34, "75": 36, "76": 38, "77": 40, "78": 42, "79": 43, "80": 47, "81": 47, "82": 47, "83": 47, "84": 47, "85": 49, "86": 53, "87": 53, "88": 53, "89": 53, "90": 53, "91": 53, "92": 55, "93": 60, "94": 62, "95": 64, "96": 66, "97": 68, "98": 70, "99": 72, "100": 74, "101": 75, "102": 79, "103": 79, "104": 79, "105": 79, "106": 79, "107": 81, "108": 85, "109": 85, "110": 85, "111": 85, "112": 85, "113": 85, "114": 87, "115": 92, "116": 94, "117": 96, "118": 98, "119": 102, "125": 11}, "uri": "rentals.html", "source_encoding": "ascii", "filename": "/Users/John/DevProjects/Repositories/chef/rentals/templates/rentals.html"}
__M_END_METADATA
"""
