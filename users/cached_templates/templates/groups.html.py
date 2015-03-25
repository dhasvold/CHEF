# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425172315.672776
_enable_loop = True
_template_filename = '/Users/John/DevProjects/Repositories/chef/users/templates/groups.html'
_template_uri = 'groups.html'
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
        def view_table():
            return render_view_table(context._locals(__M_locals))
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
        groups = context.get('groups', UNDEFINED)
        def page_title_h1():
            return render_page_title_h1(context._locals(__M_locals))
        def create_button_block():
            return render_create_button_block(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'tab_title'):
            context['self'].tab_title(**pageargs)
        

        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title_h1'):
            context['self'].page_title_h1(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'create_button_block'):
            context['self'].create_button_block(**pageargs)
        

        __M_writer('\n\t\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'view_table'):
            context['self'].view_table(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_view_table(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        groups = context.get('groups', UNDEFINED)
        def view_table():
            return render_view_table(context)
        __M_writer = context.writer()
        __M_writer('\n  \t\n\t<table class="table table-hover table-bordered">\n\t\t<thead>\n\t\t\t<tr>\n\t\t\t\t<th>\n\t\t\t\t\t<paper-button raised class="">Select All</paper-button>\n\t\t\t\t</th>\n\t\t\t\t<th>\n\t\t\t\t\tName\n\t\t\t\t</th>\n\t\t\t\t<th>\n\t\t\t\t\tNumber of Members\n\t\t\t\t</th>\n\t\t\t\t<th>\n\t\t\t\t\tActions\n\t\t\t\t</th>\n\t\t\t</tr>\n\t\t</thead>\n\t\t<tbody>\n')
        for group in groups:
            __M_writer('\t\t\t\t<tr>\n\t\t\t\t\t<td>\n\t\t\t\t\t\t<paper-checkbox></paper-checkbox>\n\t\t\t\t\t</td>\n\t\t\t\t\t<td>\n\t\t\t\t\t\t')
            __M_writer(str( group.name ))
            __M_writer('\n\t\t\t\t\t</td>\n\t\t\t\t\t<td>\n\t\t\t\t\t\t')
            __M_writer(str( group.user_set.all().count() ))
            __M_writer('\n\t\t\t\t\t</td>\n\t\t\t\t\t<td>\n')
            __M_writer('\t\t\t\t\t\t<a class="button" href="/users/groups.edit/')
            __M_writer(str( group.id ))
            __M_writer('">\n\t\t\t\t\t\t\t<paper-button raised class="edit_button">Edit</paper-button>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t\t<a class="button" href="/users/groups.delete/')
            __M_writer(str( group.id ))
            __M_writer('">\n\t\t\t\t\t\t\t<paper-button raised class="delete_button">Delete</paper-button>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t</td>\n\t\t\t\t</tr>\n')
        __M_writer('\t\t</tbody>\n\t</table>\t\n\t\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tab_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def tab_title():
            return render_tab_title(context)
        __M_writer = context.writer()
        __M_writer('\n  View Groups\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title_h1(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title_h1():
            return render_page_title_h1(context)
        __M_writer = context.writer()
        __M_writer('\n\t<h1>View Groups</h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_create_button_block(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def create_button_block():
            return render_create_button_block(context)
        __M_writer = context.writer()
        __M_writer('\n\t<a class="button" href="/users/groups.create/">\n\t\t<paper-button class="create_button" raised>Add New Group</paper-button>\n\t</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/John/DevProjects/Repositories/chef/users/templates/groups.html", "line_map": {"128": 122, "67": 26, "74": 26, "75": 46, "76": 47, "77": 52, "78": 52, "79": 55, "80": 55, "81": 59, "82": 59, "83": 59, "84": 62, "85": 62, "86": 68, "27": 0, "92": 11, "116": 20, "98": 11, "104": 16, "41": 7, "42": 9, "110": 16, "47": 13, "52": 18, "57": 24, "122": 20}, "uri": "groups.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
