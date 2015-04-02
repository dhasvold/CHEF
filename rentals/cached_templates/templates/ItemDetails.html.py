# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428014805.2545855
_enable_loop = True
_template_filename = '/home/dhasvold/PycharmProjects/chef-master/rentals/templates/ItemDetails.html'
_template_uri = 'ItemDetails.html'
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
        item = context.get('item', UNDEFINED)
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
        item = context.get('item', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\t\t<div class="row">\n\t\t\t\n')
        __M_writer('\t\t\t<div class="col-md-8">\n\t\t\t\t<h1>')
        __M_writer(str( item.specs.name ))
        __M_writer('</h1>\n\t\t\t</div>\n')
        __M_writer('\n\t\t</div>\n\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def page_title():
            return render_page_title(context)
        def content():
            return render_content(context)
        item = context.get('item', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\t<div class="row main_row">\n\t\t\n')
        __M_writer('\t\t<div class="col-md-4">\n\t\t\t\n')
        __M_writer('\t\t\t<img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer(str( item.specs.photograph.image ))
        __M_writer('" class="rental_image"/>\n')
        __M_writer('\n\t\t</div>\n')
        __M_writer('\n')
        __M_writer('\t\t<div class="col-md-5">\n\t\t\t\n')
        __M_writer('\t\t\t<div class="item_info">\n\t\t\t\t<p>')
        __M_writer(str( item.specs.description ))
        __M_writer('</p>\n\t\t\t</div>\n')
        __M_writer('\n\t\t\t<div class="spacer"></div>\n\n')
        __M_writer('\t\t\t<div class="item_info">\n\t\t\t\t<p>Standard Rental Price: $')
        __M_writer(str( item.standard_rental_price ))
        __M_writer('</p>\n\t\t\t</div>\n')
        __M_writer('\n\t\t\t<div class="spacer"></div>\n\n')
        __M_writer('\t\t\t<div class="item_info">\n\t\t\t\t<p>Price Per Day: $')
        __M_writer(str( item.price_per_day ))
        __M_writer('</p>\n\t\t\t</div>\n')
        __M_writer('\n\t\t</div>\n')
        __M_writer('\n')
        __M_writer('\t\t<div class="col-md-3">\n\n')
        __M_writer('\t\t\t<div class="start_date">\n\t\t\t\t<h4>Availability</h4>\n')
        if item.quantity_on_hand > 0:
            __M_writer('                    <p>Available!</p>\n')
        else:
            __M_writer('                <p>Not Available</p>\n')
        __M_writer('\t\t\t</div>\n            <div class="spacer"></div>\n\n')
        __M_writer('\t\t\t<div class="end_date">\n\t\t\t\t<paper-input-decorator class="short" floatingLabel label="Rental Length (Days)">\n\t\t\t\t\t<input is="core-input" id="end_date"  value=""/>\n\t\t\t\t</paper-input-decorator>\n\t\t\t</div>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<paper-button raised data-pid="')
        __M_writer(str( item.id ))
        __M_writer('" class="create_button add_button">Add to Cart</paper-button>\n')
        __M_writer('\n\t\t</div>\n')
        __M_writer('\n\t</div>\n')
        __M_writer('\n\n')
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
        item = context.get('item', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  \t')
        __M_writer(str( item.specs.name ))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/dhasvold/PycharmProjects/chef-master/rentals/templates/ItemDetails.html", "line_map": {"128": 106, "129": 110, "135": 11, "142": 11, "143": 12, "144": 12, "150": 144, "27": 0, "40": 7, "41": 9, "46": 13, "56": 18, "63": 18, "64": 22, "65": 23, "66": 23, "67": 26, "73": 15, "83": 15, "84": 18, "89": 28, "90": 30, "91": 32, "92": 35, "93": 38, "94": 38, "95": 38, "96": 38, "97": 40, "98": 43, "99": 45, "100": 48, "101": 49, "102": 49, "103": 52, "104": 56, "105": 57, "106": 57, "107": 60, "108": 64, "109": 65, "110": 65, "111": 68, "112": 71, "113": 73, "114": 76, "115": 78, "116": 79, "117": 80, "118": 81, "119": 83, "120": 87, "121": 93, "122": 95, "123": 95, "124": 95, "125": 97, "126": 100, "127": 103}, "uri": "ItemDetails.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
