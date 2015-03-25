# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425707157.045832
_enable_loop = True
_template_filename = '/Users/John/DevProjects/Repositories/chef/users/templates/users.html'
_template_uri = 'users.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['view_table', 'tab_title', 'page_title_h1', 'create_button_block']


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
        users = context.get('users', UNDEFINED)
        def view_table():
            return render_view_table(context._locals(__M_locals))
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
        def page_title_h1():
            return render_page_title_h1(context._locals(__M_locals))
        def create_button_block():
            return render_create_button_block(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'tab_title'):
            context['self'].tab_title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title_h1'):
            context['self'].page_title_h1(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'create_button_block'):
            context['self'].create_button_block(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'view_table'):
            context['self'].view_table(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_view_table(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def view_table():
            return render_view_table(context)
        users = context.get('users', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\t\n')
        __M_writer('\t<div class="table-responsive">\n\t\t<table class="table table-hover table-bordered">\n\t\t\t<thead>\n\t\t\t\t<tr>\n\t\t\t\t\t<th>\n\t\t\t\t\t\t<paper-button raised class="">Select All</paper-button>\n\t\t\t\t\t</th>\n\t\t\t\t\t<th>\n\t\t\t\t\t\tName\n\t\t\t\t\t</th>\n\t\t\t\t\t<th>\n\t\t\t\t\t\tGroup\n\t\t\t\t\t</th>\n\t\t\t\t\t<th>\n\t\t\t\t\t\tActions\n\t\t\t\t\t</th>\n\t\t\t\t</tr>\n\t\t\t</thead>\n\t\t\t<tbody>\n')
        for user in users:
            __M_writer('\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t<paper-checkbox></paper-checkbox>\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t')
            __M_writer(str( user.get_full_name() ))
            __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t')
            __M_writer(str( user.groups.all()[0] ))
            __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n')
            __M_writer('\t\t\t\t\t\t\t<a class="button" href="/users/users.edit/')
            __M_writer(str( user.id ))
            __M_writer('">\n\t\t\t\t\t\t\t\t<paper-button raised class="edit_button">Edit</paper-button>\n\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t<a class="button" href="/users/users.delete/')
            __M_writer(str( user.id ))
            __M_writer('">\n\t\t\t\t\t\t\t\t<paper-button raised class="delete_button">Delete</paper-button>\n\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</td>\n\t\t\t\t\t</tr>\n')
        __M_writer('\t\t\t</tbody>\n\t\t</table>\t\n\t</div>\n')
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
        __M_writer('\n  View Users\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title_h1(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title_h1():
            return render_page_title_h1(context)
        __M_writer = context.writer()
        __M_writer('\n\t<h1>View Users</h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_create_button_block(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def create_button_block():
            return render_create_button_block(context)
        __M_writer = context.writer()
        __M_writer('\n\t<a class="button" href="/users/users.create/">\n\t\t<paper-button class="create_button" raised>Create New User</paper-button>\n\t</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/John/DevProjects/Repositories/chef/users/templates/users.html", "source_encoding": "ascii", "uri": "users.html", "line_map": {"130": 124, "67": 25, "74": 25, "75": 28, "76": 47, "77": 48, "78": 53, "79": 53, "80": 56, "81": 56, "82": 60, "83": 60, "84": 60, "85": 63, "86": 63, "87": 69, "88": 73, "27": 0, "94": 11, "100": 11, "41": 7, "42": 9, "47": 13, "112": 15, "52": 17, "118": 19, "57": 23, "124": 19, "106": 15}}
__M_END_METADATA
"""
