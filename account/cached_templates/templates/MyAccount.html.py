# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425673939.724605
_enable_loop = True
_template_filename = '/Users/John/DevProjects/Repositories/chef/account/templates/MyAccount.html'
_template_uri = 'MyAccount.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'tab_title', 'page_title']


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
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
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
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        def page_title():
            return render_page_title(context)
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
        __M_writer('\n')
        __M_writer('\t\t\t<paper-button raised id="change_password_button" class="create_button">Change Password</paper-button>\n')
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


def render_tab_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def tab_title():
            return render_tab_title(context)
        __M_writer = context.writer()
        __M_writer('\n  \tMy Account\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('\n\n\t\t\t<h1>My Account</h1>\n\n\t \t')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"66": 17, "71": 25, "72": 30, "73": 33, "74": 34, "75": 34, "76": 37, "77": 39, "78": 41, "79": 43, "80": 46, "81": 48, "82": 50, "83": 50, "84": 54, "85": 57, "86": 59, "87": 63, "27": 0, "93": 13, "99": 13, "40": 9, "41": 11, "46": 15, "111": 21, "117": 111, "105": 21, "56": 17}, "source_encoding": "ascii", "uri": "MyAccount.html", "filename": "/Users/John/DevProjects/Repositories/chef/account/templates/MyAccount.html"}
__M_END_METADATA
"""
