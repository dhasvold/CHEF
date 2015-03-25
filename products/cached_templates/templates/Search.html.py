# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425795915.542657
_enable_loop = True
_template_filename = '/Users/John/DevProjects/Repositories/chef/products/templates/Search.html'
_template_uri = 'Search.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['extra_links', 'content']


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
        def extra_links():
            return render_extra_links(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_links'):
            context['self'].extra_links(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_links():
            return render_extra_links(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\t<link href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/styles/login.css" rel="stylesheet" type="text/css">\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\t\t\t\t\n\t<div id="error"></div>\n\n')
        __M_writer('\t<paper-input-decorator floatingLabel label="Search">\n\t\t<input type="text" id="search_input" value="">\n\t</paper-input-decorator>\n')
        __M_writer('\n')
        __M_writer('\t<div class="search_button_con">\n\t\t<paper-button raised class="success_button" id="search_button">Search</paper-button>\n\t</div>\n')
        __M_writer('\n\t<div class="clearfix"></div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "Search.html", "source_encoding": "ascii", "line_map": {"43": 15, "68": 17, "37": 7, "38": 9, "74": 17, "75": 22, "76": 26, "77": 28, "78": 32, "84": 78, "53": 11, "27": 0, "60": 11, "61": 13, "62": 13}, "filename": "/Users/John/DevProjects/Repositories/chef/products/templates/Search.html"}
__M_END_METADATA
"""
