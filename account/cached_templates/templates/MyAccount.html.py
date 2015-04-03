# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428018321.212903
_enable_loop = True
_template_filename = '/home/dhasvold/PycharmProjects/chef-master/account/templates/MyAccount.html'
_template_uri = 'MyAccount.html'
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
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


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/home/dhasvold/PycharmProjects/chef-master/account/templates/MyAccount.html", "uri": "MyAccount.html", "line_map": {"68": 13, "74": 13, "80": 17, "110": 59, "90": 17, "27": 0, "95": 25, "96": 30, "97": 33, "98": 34, "99": 34, "100": 37, "101": 39, "102": 41, "103": 43, "40": 9, "41": 11, "106": 50, "107": 50, "108": 54, "109": 57, "46": 15, "111": 63, "104": 46, "117": 111, "105": 48, "56": 21, "62": 21}}
__M_END_METADATA
"""
