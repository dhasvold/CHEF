# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425692781.240258
_enable_loop = True
_template_filename = '/Users/John/DevProjects/Repositories/chef/account/templates/NewUser.html'
_template_uri = 'NewUser.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'page_title', 'tab_title']


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
        def content():
            return render_content(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        def page_title():
            return render_page_title(context)
        form = context.get('form', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\t<div class="page_title">\n\t\t\n\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\n\n\t</div>\n\n')
        __M_writer('\t<div class="row">\n\t\t\n')
        __M_writer('\t\t <div class="col-md-3">\n\t\t \t<img class="user_image" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/add-user.png">\n\n')
        __M_writer('\t\t\t<paper-button raised class="edit_button">Upload Image</paper-button>\n')
        __M_writer('\n\t\t </div>\n')
        __M_writer('\n')
        __M_writer('\t\t <div class="col-md-9">\n\n\t\t \t')
        __M_writer(str( form ))
        __M_writer('\n\t\t\t\t\n\t\t </div>\n')
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
        __M_writer('\n\n\t\t\t<h1>New User</h1>\n\n\t \t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tab_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def tab_title():
            return render_tab_title(context)
        __M_writer = context.writer()
        __M_writer('\n  \tNew User\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"66": 15, "71": 23, "72": 28, "73": 31, "74": 32, "75": 32, "76": 35, "77": 37, "78": 40, "79": 42, "80": 44, "81": 44, "82": 48, "83": 51, "84": 53, "85": 57, "27": 0, "97": 19, "91": 19, "103": 11, "40": 7, "41": 9, "109": 11, "46": 13, "115": 109, "56": 15}, "source_encoding": "ascii", "filename": "/Users/John/DevProjects/Repositories/chef/account/templates/NewUser.html", "uri": "NewUser.html"}
__M_END_METADATA
"""
