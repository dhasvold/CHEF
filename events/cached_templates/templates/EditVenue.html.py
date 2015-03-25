# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423359525.697578
_enable_loop = True
_template_filename = '/Users/John/DevProjects/Repositories/chef/events/templates/EditVenue.html'
_template_uri = 'EditVenue.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['paper_elements_import', 'content', 'tab_title', 'extra_links']


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
    return runtime._inherit_from(context, '/base_admin/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def paper_elements_import():
            return render_paper_elements_import(context._locals(__M_locals))
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        def extra_links():
            return render_extra_links(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'tab_title'):
            context['self'].tab_title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'paper_elements_import'):
            context['self'].paper_elements_import(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_links'):
            context['self'].extra_links(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_paper_elements_import(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def paper_elements_import():
            return render_paper_elements_import(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\t<link rel="import" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_app/styles/bower_components/paper-input/paper-input.html">\n\t<link rel="import" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_app/styles/bower_components/paper-button/paper-button.html">\n\t<link rel="import" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_app/styles/bower_components/paper-radio-group/paper-radio-group.html">\n\t<link rel="import" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_app/styles/bower_components/paper-radio-button/paper-radio-button.html">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\t<div class="page_title">\n\t\t<h1>Edit Venue</h1>\n\t</div>\n\n')
        __M_writer('\t<div class="row">\n\n')
        __M_writer('\t <div class="col-md-12">\n\t \t\n')
        __M_writer('\t\t')
        __M_writer(str( form ))
        __M_writer('\n')
        __M_writer('\t\t\t\n\t </div>\n')
        __M_writer('\n\t</div>\n')
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
        __M_writer('\n  Edit Venue\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_links():
            return render_extra_links(context)
        __M_writer = context.writer()
        __M_writer('\n  \t\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"130": 23, "68": 15, "112": 11, "136": 130, "75": 15, "76": 16, "77": 16, "78": 17, "79": 17, "80": 18, "81": 18, "82": 19, "83": 19, "89": 27, "27": 0, "96": 27, "97": 34, "98": 37, "99": 40, "100": 40, "101": 40, "102": 42, "103": 45, "104": 48, "105": 50, "42": 7, "43": 9, "48": 13, "53": 20, "118": 11, "58": 25, "124": 23, "106": 54}, "source_encoding": "ascii", "uri": "EditVenue.html", "filename": "/Users/John/DevProjects/Repositories/chef/events/templates/EditVenue.html"}
__M_END_METADATA
"""
