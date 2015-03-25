# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425521507.42419
_enable_loop = True
_template_filename = '/Users/John/DevProjects/Repositories/chef/users/templates/modal_password.html'
_template_uri = 'modal_password.html'
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
        user = context.get('user', UNDEFINED)
        form = context.get('form', UNDEFINED)
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
        __M_writer('base_admin/styles/Edit.css" rel="stylesheet" type="text/css">\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        user = context.get('user', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\t<input class="hidden" id="user_id" value="')
        __M_writer(str( user.id ))
        __M_writer('"/>\n\n\t')
        __M_writer(str( form ))
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "modal_password.html", "filename": "/Users/John/DevProjects/Repositories/chef/users/templates/modal_password.html", "source_encoding": "ascii", "line_map": {"64": 14, "70": 18, "39": 8, "40": 10, "45": 16, "78": 18, "79": 21, "80": 21, "81": 21, "82": 23, "83": 23, "55": 12, "89": 83, "27": 0, "62": 12, "63": 14}}
__M_END_METADATA
"""
