# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425674831.797408
_enable_loop = True
_template_filename = '/Users/John/DevProjects/Repositories/chef/users/templates/EditUser.html'
_template_uri = 'EditUser.html'
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        user = context.get('user', UNDEFINED)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
        user = context.get('user', UNDEFINED)
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('\n\n\t<div class="page_title">\n\t\t\n\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\n\n\t</div>\n\n')
        __M_writer('\t<div class="row">\n\t\t\n')
        __M_writer('\t <div class="col-md-3">\n\t \t<img class="user_image" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/add-user.png">\n\n')
        __M_writer('\t\t<paper-button raised class="edit_button">Upload Image</paper-button>\n')
        __M_writer('\n\t </div>\n')
        __M_writer('\n')
        __M_writer('\t <div class="col-md-9">\n\n')
        __M_writer('\t \t<input class="hidden" id="user_id" value="')
        __M_writer(str( user.id ))
        __M_writer('"/>\n\t \t\n')
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
        __M_writer('\n  Edit User\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('\n\n\t\t\t<h1>Edit User</h1>\n\n\t \t')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/John/DevProjects/Repositories/chef/users/templates/EditUser.html", "source_encoding": "ascii", "uri": "EditUser.html", "line_map": {"68": 15, "73": 23, "74": 28, "75": 31, "76": 32, "77": 32, "78": 35, "79": 37, "80": 40, "81": 42, "82": 45, "83": 45, "84": 45, "85": 48, "86": 48, "87": 48, "88": 50, "89": 53, "90": 56, "27": 0, "92": 62, "98": 11, "91": 58, "104": 11, "41": 7, "42": 9, "110": 19, "47": 13, "116": 19, "57": 15, "122": 116}}
__M_END_METADATA
"""
