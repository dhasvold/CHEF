# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426968960.005706
_enable_loop = True
_template_filename = '/Users/John/DevProjects/Repositories/chef/inventory/templates/EditFeeAjax.html'
_template_uri = 'EditFeeAjax.html'
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
        form = context.get('form', UNDEFINED)
        def extra_links():
            return render_extra_links(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
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
        __M_writer = context.writer()
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n\t<div class="row">\n\t\t\n\t\t<div class="col-md-12">\n\t\t\t\n\t\t\t')
        __M_writer(str( form ))
        __M_writer('\t\t\n\n\t\t</div>\n\n\t</div>\n\n\t<div class="spacer"></div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"80": 74, "59": 11, "27": 0, "37": 7, "38": 9, "65": 15, "72": 15, "73": 21, "74": 21, "43": 13, "53": 11}, "filename": "/Users/John/DevProjects/Repositories/chef/inventory/templates/EditFeeAjax.html", "uri": "EditFeeAjax.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
