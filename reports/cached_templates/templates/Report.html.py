# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428103055.0719066
_enable_loop = True
_template_filename = '/home/dhasvold/PycharmProjects/chef-master/reports/templates/Report.html'
_template_uri = 'Report.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['tab_title', 'view_table', 'page_title_h1']


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
        def page_title_h1():
            return render_page_title_h1(context._locals(__M_locals))
        report_name = context.get('report_name', UNDEFINED)
        def view_table():
            return render_view_table(context._locals(__M_locals))
        sixty = context.get('sixty', UNDEFINED)
        ninety = context.get('ninety', UNDEFINED)
        ninety_plus = context.get('ninety_plus', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'tab_title'):
            context['self'].tab_title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title_h1'):
            context['self'].page_title_h1(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'view_table'):
            context['self'].view_table(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tab_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def tab_title():
            return render_tab_title(context)
        report_name = context.get('report_name', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  ')
        __M_writer(str( report_name ))
        __M_writer(' Report\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_view_table(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        sixty = context.get('sixty', UNDEFINED)
        ninety_plus = context.get('ninety_plus', UNDEFINED)
        ninety = context.get('ninety', UNDEFINED)
        def view_table():
            return render_view_table(context)
        __M_writer = context.writer()
        __M_writer('\n\t\n')
        __M_writer('\t<div class="table-responsive">\n\t\t<table class="table table-hover table-bordered">\n\t\t\t<thead>\n\t\t\t\t<tr>\n\t\t\t\t\t<th>\n                        Time Overdue\n\t\t\t\t\t</th>\n\t\t\t\t\t<th>\n\t\t\t\t\t\tItem Name\n\t\t\t\t\t</th>\n\t\t\t\t\t<th>\n\t\t\t\t\t\tCustomer\n\t\t\t\t\t</th>\n\t\t\t\t\t<th>\n\t\t\t\t\t\tDue Date\n\t\t\t\t\t</th>\n\t\t\t\t</tr>\n\t\t\t</thead>\n\t\t\t<tbody>\n            <tr><td><b>30 Days</b></td><td></td><td></td><td></td></tr>\n')
        for item in sixty:
            __M_writer('\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t')
            __M_writer(str( item.item.specs.name ))
            __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t')
            __M_writer(str( item.transaction.customer.get_full_name() ))
            __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t')
            __M_writer(str( item.due_date.strftime('%b %d, %Y') ))
            __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t</tr>\n')
        __M_writer('           <tr><td><b>60 Days</b></td><td></td><td></td><td></td></tr>\n')
        for item in ninety:
            __M_writer('\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t')
            __M_writer(str( item.item.specs.name ))
            __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t')
            __M_writer(str( item.transaction.customer.get_full_name() ))
            __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t')
            __M_writer(str( item.due_date.strftime('%b %d, %Y') ))
            __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t</tr>\n')
        __M_writer('           <tr><td><b>90 Or More Days</b></td><td></td><td></td><td></td></tr>\n')
        for item in ninety_plus:
            __M_writer('\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t')
            __M_writer(str( item.item.specs.name ))
            __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t')
            __M_writer(str( item.transaction.customer.get_full_name() ))
            __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<td>\n\t\t\t\t\t\t\t')
            __M_writer(str( item.due_date.strftime('%b %d, %Y') ))
            __M_writer('\n\t\t\t\t\t\t</td>\n\t\t\t\t\t</tr>\n')
        __M_writer('\t\t\t</tbody>\n\t\t</table>\n\t</div>\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title_h1(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title_h1():
            return render_page_title_h1(context)
        report_name = context.get('report_name', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\t<h1>')
        __M_writer(str( report_name ))
        __M_writer(' Report</h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "Report.html", "source_encoding": "ascii", "line_map": {"129": 15, "130": 16, "131": 16, "137": 131, "27": 0, "42": 7, "43": 9, "48": 13, "53": 17, "63": 11, "70": 11, "71": 12, "72": 12, "78": 19, "87": 19, "88": 22, "89": 42, "90": 43, "91": 47, "92": 47, "93": 50, "94": 50, "95": 53, "96": 53, "97": 57, "98": 58, "99": 59, "100": 63, "101": 63, "102": 66, "103": 66, "104": 69, "105": 69, "106": 73, "107": 74, "108": 75, "109": 79, "110": 79, "111": 82, "112": 82, "113": 85, "114": 85, "115": 89, "116": 93, "122": 15}, "filename": "/home/dhasvold/PycharmProjects/chef-master/reports/templates/Report.html"}
__M_END_METADATA
"""
