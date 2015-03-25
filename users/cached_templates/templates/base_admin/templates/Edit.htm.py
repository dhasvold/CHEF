# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425170237.155668
_enable_loop = True
_template_filename = '/Users/John/DevProjects/Repositories/chef/base_admin/templates/Edit.htm'
_template_uri = '/base_admin/templates/Edit.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['paper_elements_import', 'content', 'page_title']


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
        def content():
            return render_content(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'paper_elements_import'):
            context['self'].paper_elements_import(**pageargs)
        

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
        def page_title():
            return render_page_title(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\t\n\t<div class="page_title">\n\t\t\n\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\n\n\t</div>\n\n')
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


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('\n\n\t\t\t<h1>Edit</h1>\n\n\t \t')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "/base_admin/templates/Edit.htm", "source_encoding": "ascii", "line_map": {"64": 19, "65": 19, "66": 20, "67": 20, "68": 21, "69": 21, "70": 22, "71": 22, "77": 25, "99": 52, "86": 25, "91": 33, "92": 38, "93": 41, "94": 44, "95": 44, "96": 44, "97": 46, "98": 49, "27": 0, "100": 54, "101": 58, "40": 14, "41": 16, "107": 29, "46": 23, "113": 29, "119": 113, "56": 18, "63": 18}, "filename": "/Users/John/DevProjects/Repositories/chef/base_admin/templates/Edit.htm"}
__M_END_METADATA
"""
