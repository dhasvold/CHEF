# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426964865.057948
_enable_loop = True
_template_filename = '/Users/John/DevProjects/Repositories/chef/inventory/templates/ProcessReturn.html'
_template_uri = 'ProcessReturn.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['page_title', 'tab_title', 'content']


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
    return runtime._inherit_from(context, '/base_admin/templates/Edit.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
        rental_item = context.get('rental_item', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'tab_title'):
            context['self'].tab_title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

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
        __M_writer('\n\n\t<h1>Process Rental Return</h1>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tab_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def tab_title():
            return render_tab_title(context)
        __M_writer = context.writer()
        __M_writer('\n  \tProcess Rental Return\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        rental_item = context.get('rental_item', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\t<div class="row">\n\t\t\n')
        __M_writer('\t <div class="col-md-8">\n\t \t\n')
        __M_writer('\t\t')
        __M_writer(str( form ))
        __M_writer('\n')
        __M_writer('\n\t </div>\n')
        __M_writer('\n')
        __M_writer('\t <div class="col-md-4">\n\n\t \t<div class="right_col_content">\n\t \t\t<h2>Actions</h2>\n\n')
        __M_writer('\t\t\t<paper-button raised data-id="')
        __M_writer(str( rental_item.id ))
        __M_writer('" id="add_fee" class="edit_button">Add Fee</paper-button>\n')
        __M_writer('\n\t\t</div>\n\t\t\t\n\t </div>\n')
        __M_writer('\n\t</div>\n')
        __M_writer('\n')
        __M_writer('\t<div class="spacer"></div>\n\t<div class="spacer"></div>\n\t<div class="spacer"></div>\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"67": 15, "73": 11, "79": 11, "115": 109, "85": 21, "27": 0, "93": 21, "94": 24, "95": 27, "96": 30, "97": 30, "98": 30, "99": 32, "100": 35, "101": 37, "102": 43, "103": 43, "40": 7, "41": 9, "106": 50, "107": 53, "108": 55, "109": 59, "46": 13, "104": 43, "51": 19, "105": 45, "61": 15}, "uri": "ProcessReturn.html", "filename": "/Users/John/DevProjects/Repositories/chef/inventory/templates/ProcessReturn.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
