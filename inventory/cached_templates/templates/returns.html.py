# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426962410.663425
_enable_loop = True
_template_filename = '/Users/John/DevProjects/Repositories/chef/inventory/templates/returns.html'
_template_uri = 'returns.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['view_table', 'page_title_h1', 'create_button_block', 'top_left_column', 'tab_title', 'top_right_column']


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
        today = context.get('today', UNDEFINED)
        def page_title_h1():
            return render_page_title_h1(context._locals(__M_locals))
        def create_button_block():
            return render_create_button_block(context._locals(__M_locals))
        def top_left_column():
            return render_top_left_column(context._locals(__M_locals))
        def top_right_column():
            return render_top_right_column(context._locals(__M_locals))
        rentals = context.get('rentals', UNDEFINED)
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
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_left_column'):
            context['self'].top_left_column(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_right_column'):
            context['self'].top_right_column(**pageargs)
        

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
        today = context.get('today', UNDEFINED)
        rentals = context.get('rentals', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\t\n')
        __M_writer('\t<div class="table-responsive">\n\t\t<table class="table table-hover table-bordered">\n\t\t\t<thead>\n\t\t\t\t<tr>\n\t\t\t\t\t<th>\n\t\t\t\t\t\tItem Name\n\t\t\t\t\t</th>\n\t\t\t\t\t<th>\n\t\t\t\t\t\tCustomer\n\t\t\t\t\t</th>\n\t\t\t\t\t<th>\n\t\t\t\t\t\tDue Date\n\t\t\t\t\t</th>\n\t\t\t\t\t<th>\n\t\t\t\t\t\tActions\n\t\t\t\t\t</th>\n\t\t\t\t</tr>\n\t\t\t</thead>\n\t\t\t<tbody>\n')
        for rental in rentals:
            __M_writer('\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t')
            __M_writer(str( rental.item.specs.name ))
            __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t')
            __M_writer(str( rental.transaction.customer.get_full_name() ))
            __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n')
            if rental.due_date < today:
                __M_writer('\t\t\t\t\t\t\t\t<span class="form_errors">')
                __M_writer(str( rental.due_date ))
                __M_writer('</span>\n')
            else:
                __M_writer('\t\t\t\t\t\t\t\t')
                __M_writer(str( rental.due_date ))
                __M_writer('\n')
            __M_writer('\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t<a class="button" href="/inventory/returns.return_rental/')
            __M_writer(str( rental.id ))
            __M_writer('">\n\t\t\t\t\t\t\t\t<paper-button raised class="create_button">Check-In</paper-button>\n\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t<a class="button" href="/inventory/returns.edit/')
            __M_writer(str( rental.id ))
            __M_writer('">\n\t\t\t\t\t\t\t\t<paper-button raised class="edit_button">Edit</paper-button>\n\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t</td>\n\t\t\t\t\t</tr>\n')
        __M_writer('\t\t\t</tbody>\n\t\t</table>\t\n\t</div>\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title_h1(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title_h1():
            return render_page_title_h1(context)
        __M_writer = context.writer()
        __M_writer('\n\t<h1>Pending Rentals</h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_create_button_block(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def create_button_block():
            return render_create_button_block(context)
        __M_writer = context.writer()
        __M_writer('\n\t\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_left_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_left_column():
            return render_top_left_column(context)
        __M_writer = context.writer()
        __M_writer('\n  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tab_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def tab_title():
            return render_tab_title(context)
        __M_writer = context.writer()
        __M_writer('\n  \tPending Rentals\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_right_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_right_column():
            return render_top_right_column(context)
        __M_writer = context.writer()
        __M_writer('\n  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"160": 11, "130": 19, "67": 25, "178": 172, "72": 29, "172": 27, "111": 78, "142": 23, "82": 31, "148": 23, "110": 72, "154": 11, "90": 31, "27": 0, "92": 53, "93": 54, "94": 56, "95": 56, "96": 59, "97": 59, "98": 62, "99": 63, "100": 63, "101": 63, "102": 64, "103": 65, "104": 65, "105": 65, "106": 67, "107": 69, "108": 69, "109": 72, "46": 7, "47": 9, "112": 82, "136": 19, "91": 34, "52": 13, "118": 15, "57": 17, "124": 15, "62": 21, "166": 27}, "uri": "returns.html", "filename": "/Users/John/DevProjects/Repositories/chef/inventory/templates/returns.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
