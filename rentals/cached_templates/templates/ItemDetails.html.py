# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426908406.207882
_enable_loop = True
_template_filename = '/Users/John/DevProjects/Repositories/chef/rentals/templates/ItemDetails.html'
_template_uri = 'ItemDetails.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['tab_title', 'page_title', 'content']


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
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
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
        def content():
            return render_content(context)
        def page_title():
            return render_page_title(context)
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
        __M_writer('\t\t\t<div class="start_date">\n\t\t\t\t<paper-input-decorator class="short" floatingLabel label="Rental Start Date">\n\t\t\t\t\t<input is="core-input" id="start_date" class="datetimepicker" value=""/>\n\t\t\t\t</paper-input-decorator>\n\t\t\t</div>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<div class="end_date">\n\t\t\t\t<paper-input-decorator class="short" floatingLabel label="Rental End Date">\n\t\t\t\t\t<input is="core-input" id="end_date" class="datetimepicker" value=""/>\n\t\t\t\t</paper-input-decorator>\n\t\t\t</div>\n')
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


"""
__M_BEGIN_METADATA
{"filename": "/Users/John/DevProjects/Repositories/chef/rentals/templates/ItemDetails.html", "uri": "ItemDetails.html", "source_encoding": "ascii", "line_map": {"128": 73, "129": 76, "130": 82, "131": 84, "132": 90, "133": 92, "134": 92, "135": 92, "136": 94, "137": 97, "138": 100, "139": 103, "140": 107, "146": 140, "27": 0, "40": 7, "41": 9, "46": 13, "56": 11, "63": 11, "64": 12, "65": 12, "71": 18, "78": 18, "79": 22, "80": 23, "81": 23, "82": 26, "88": 15, "98": 15, "99": 18, "104": 28, "105": 30, "106": 32, "107": 35, "108": 38, "109": 38, "110": 38, "111": 38, "112": 40, "113": 43, "114": 45, "115": 48, "116": 49, "117": 49, "118": 52, "119": 56, "120": 57, "121": 57, "122": 60, "123": 64, "124": 65, "125": 65, "126": 68, "127": 71}}
__M_END_METADATA
"""
