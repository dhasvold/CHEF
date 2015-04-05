# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428197584.8809292
_enable_loop = True
_template_filename = '/home/dhasvold/PycharmProjects/chef-master/reports/templates/Report.html'
_template_uri = 'Report.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['page_title_h1', 'view_table', 'tab_title', 'top_right_column', 'top_left_column']


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
        sixty = context.get('sixty', UNDEFINED)
        def view_table():
            return render_view_table(context._locals(__M_locals))
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
        def top_right_column():
            return render_top_right_column(context._locals(__M_locals))
        def page_title_h1():
            return render_page_title_h1(context._locals(__M_locals))
        report_name = context.get('report_name', UNDEFINED)
        ninety = context.get('ninety', UNDEFINED)
        ninety_plus = context.get('ninety_plus', UNDEFINED)
        def top_left_column():
            return render_top_left_column(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'tab_title'):
            context['self'].tab_title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title_h1'):
            context['self'].page_title_h1(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_left_column'):
            context['self'].top_left_column(**pageargs)
        

        __M_writer('\n\n\t\t</div>\n')
        __M_writer('\n')
        __M_writer('\t\t<div class="col-md-6">\n\n\t\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_right_column'):
            context['self'].top_right_column(**pageargs)
        

        __M_writer('\n\n\t\t</div>\n')
        __M_writer('\n\n\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'view_table'):
            context['self'].view_table(**pageargs)
        

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


def render_view_table(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        ninety_plus = context.get('ninety_plus', UNDEFINED)
        sixty = context.get('sixty', UNDEFINED)
        def view_table():
            return render_view_table(context)
        ninety = context.get('ninety', UNDEFINED)
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


def render_top_right_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_right_column():
            return render_top_right_column(context)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\t\t\t\t<h3>Filter Options</h3>\n\n\t\t\t\t<div class="dropdown">\n\t\t\t\t\t<button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropwdown" aria-expanded="true">\n\t\t\t\t\t\tFilter Options\n\t\t\t\t\t\t<span class="caret"></span>\n\t\t\t\t\t</button>\n\t\t\t\t\t<ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1">\n\t\t\t\t\t\t<li role="presentation">Delete</li>\n\t\t\t\t\t</ul>\n\t\t\t\t</div>\n\n\t\t\t\t<paper-input-decorator class="short" floatingLabel label="Criteria">\n\t\t\t\t\t<input is="core-input"></input>\n\t\t\t\t</paper-input-decorator>\n\n\n                <a href="/reports/rentals.send_emails/">\n\t\t\t\t    <paper-button class="success_button apply_filter" raised>Email Customers</paper-button>\n                </a>\n')
        __M_writer('\n\t\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_left_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_left_column():
            return render_top_left_column(context)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\t\t\t\t<h3>Batch Options</h3>\n\n\t\t\t\t<div class="dropdown">\n\t\t\t\t\t<button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropwdown" aria-expanded="true">\n\t\t\t\t\t\tBatch Options\n\t\t\t\t\t\t<span class="caret"></span>\n\t\t\t\t\t</button>\n\t\t\t\t\t<ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1">\n\t\t\t\t\t\t<li role="presentation">Delete</li>\n\t\t\t\t\t</ul>\n\t\t\t\t</div>\n\n\t\t\t\t<paper-button class="success_button run_batch" raised>Submit</paper-button>\n')
        __M_writer('\n\t\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"128": 142, "129": 142, "130": 145, "131": 145, "132": 149, "133": 153, "139": 11, "175": 22, "146": 11, "147": 12, "148": 12, "174": 19, "154": 45, "27": 0, "160": 45, "161": 48, "162": 69, "168": 19, "46": 7, "47": 9, "176": 36, "52": 13, "182": 176, "57": 17, "62": 37, "63": 41, "64": 43, "69": 70, "70": 74, "80": 15, "87": 15, "88": 16, "89": 16, "95": 79, "104": 79, "105": 82, "106": 102, "107": 103, "108": 107, "109": 107, "110": 110, "111": 110, "112": 113, "113": 113, "114": 117, "115": 118, "116": 119, "117": 123, "118": 123, "119": 126, "120": 126, "121": 129, "122": 129, "123": 133, "124": 134, "125": 135, "126": 139, "127": 139}, "uri": "Report.html", "filename": "/home/dhasvold/PycharmProjects/chef-master/reports/templates/Report.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
