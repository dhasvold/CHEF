# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425797409.423593
_enable_loop = True
_template_filename = '/Users/John/DevProjects/Repositories/chef/account/templates/confirmation.html'
_template_uri = 'confirmation.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['tab_title', 'content', 'page_title']


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
        def content():
            return render_content(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
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
        __M_writer = context.writer()
        __M_writer('\n  \tOrder Confirmation\n')
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
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\t<div class="row main_row">\n\t\t\n')
        __M_writer('\t\t<div class="col-md-12">\n\t\t\t\n\t\t\t<p>Your order is on its way!</p>\n\n\t\t\t<p>Thank you for doing business with us!</p>\n\n\t\t</div>\n')
        __M_writer('\n\t</div>\n')
        __M_writer('\n\n')
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
        __M_writer('\n\t\t<div class="row">\n\t\t\t\n')
        __M_writer('\t\t\t<div class="col-md-8">\n\t\t\t\t<h1>Congratulations!</h1>\n\t\t\t</div>\n')
        __M_writer('\n\t\t</div>\n\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/John/DevProjects/Repositories/chef/account/templates/confirmation.html", "uri": "confirmation.html", "line_map": {"66": 15, "74": 15, "75": 18, "80": 28, "81": 30, "82": 32, "83": 35, "84": 43, "85": 46, "86": 49, "87": 53, "27": 0, "93": 18, "99": 18, "100": 22, "101": 26, "38": 7, "39": 9, "107": 101, "44": 13, "54": 11, "60": 11}}
__M_END_METADATA
"""
