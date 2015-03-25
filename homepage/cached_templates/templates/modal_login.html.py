# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426620135.918468
_enable_loop = True
_template_filename = '/Users/John/DevProjects/Repositories/chef/homepage/templates/modal_login.html'
_template_uri = 'modal_login.html'
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
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
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\t')
        __M_writer(str( form.as_login() ))
        __M_writer('\n\n')
        __M_writer('\t<div class="center">\n\t\t\n\t\t<a href="/homepage/login.reset_password/" id="forgot_pass">Forgot Password?</a>\n\n\t</div> \n\n\t<div class="spacer"></div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/John/DevProjects/Repositories/chef/homepage/templates/modal_login.html", "source_encoding": "ascii", "line_map": {"69": 18, "38": 8, "39": 10, "44": 16, "76": 18, "77": 20, "78": 20, "79": 23, "85": 79, "54": 12, "27": 0, "61": 12, "62": 14, "63": 14}, "uri": "modal_login.html"}
__M_END_METADATA
"""
