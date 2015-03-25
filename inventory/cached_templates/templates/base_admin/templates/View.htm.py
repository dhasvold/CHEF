# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426958347.994172
_enable_loop = True
_template_filename = '/Users/John/DevProjects/Repositories/chef/base_admin/templates/View.htm'
_template_uri = '/base_admin/templates/View.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['top_left_column', 'top_right_column', 'tab_title', 'page_title_h1', 'create_button_block', 'paper_elements_import', 'content', 'page_title', 'view_table']


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
    return runtime._inherit_from(context, '/base_admin/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def top_right_column():
            return render_top_right_column(context._locals(__M_locals))
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        def create_button_block():
            return render_create_button_block(context._locals(__M_locals))
        def page_title_h1():
            return render_page_title_h1(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def view_table():
            return render_view_table(context._locals(__M_locals))
        def top_left_column():
            return render_top_left_column(context._locals(__M_locals))
        def paper_elements_import():
            return render_paper_elements_import(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'tab_title'):
            context['self'].tab_title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'paper_elements_import'):
            context['self'].paper_elements_import(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_left_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_left_column():
            return render_top_left_column(context)
        __M_writer = context.writer()
        __M_writer('\n\t\t\t  \t\n')
        __M_writer('\t\t\t\t<h3>Batch Options</h3>\n\t\t\t\t\n\t\t\t\t<div class="dropdown">\n\t\t\t\t\t<button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropwdown" aria-expanded="true">\n\t\t\t\t\t\tBatch Options\n\t\t\t\t\t\t<span class="caret"></span>\n\t\t\t\t\t</button>\n\t\t\t\t\t<ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1">\n\t\t\t\t\t\t<li role="presentation">Delete</li>\n\t\t\t\t\t</ul>\n\t\t\t\t</div>\n\n\t\t\t\t<paper-button class="success_button run_batch" raised>Submit</paper-button>\n')
        __M_writer('\n\t\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_right_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_right_column():
            return render_top_right_column(context)
        __M_writer = context.writer()
        __M_writer('\n\t\t  \t\n')
        __M_writer('\t\t\t\t<h3>Filter Options</h3>\n\t\t\t\t\n\t\t\t\t<div class="dropdown">\n\t\t\t\t\t<button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropwdown" aria-expanded="true">\n\t\t\t\t\t\tFilter Options\n\t\t\t\t\t\t<span class="caret"></span>\n\t\t\t\t\t</button>\n\t\t\t\t\t<ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1">\n\t\t\t\t\t\t<li role="presentation">Delete</li>\n\t\t\t\t\t</ul>\n\t\t\t\t</div>\n\n\t\t\t\t<paper-input-decorator class="short" floatingLabel label="Criteria">\n\t\t\t\t\t<input is="core-input"></input>\n\t\t\t\t</paper-input-decorator>\n\n\t\t\t\t<paper-button class="success_button apply_filter" raised>Submit</paper-button>\n')
        __M_writer('\n\t\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tab_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def tab_title():
            return render_tab_title(context)
        __M_writer = context.writer()
        __M_writer('\n  View\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title_h1(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title_h1():
            return render_page_title_h1(context)
        __M_writer = context.writer()
        __M_writer('\n\t\t\t\t  \tView\n\t\t\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_create_button_block(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def create_button_block():
            return render_create_button_block(context)
        __M_writer = context.writer()
        __M_writer('\n\t\t\t\t\t  \n\t\t\t\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_paper_elements_import(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def paper_elements_import():
            return render_paper_elements_import(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\t<link rel="import" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_app/styles/bower_components/paper-input/paper-input.html">\n\t<link rel="import" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_app/styles/bower_components/paper-button/paper-button.html">\n\t<link rel="import" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_app/styles/bower_components/paper-checkbox/paper-checkbox.html">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_left_column():
            return render_top_left_column(context)
        def top_right_column():
            return render_top_right_column(context)
        def page_title():
            return render_page_title(context)
        def create_button_block():
            return render_create_button_block(context)
        def page_title_h1():
            return render_page_title_h1(context)
        def content():
            return render_content(context)
        def view_table():
            return render_view_table(context)
        __M_writer = context.writer()
        __M_writer('\n\t\n')
        __M_writer('\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\t<div class="row">\n\t\t\n')
        __M_writer('\t\t<div class="col-md-6">\n\n\t\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_left_column'):
            context['self'].top_left_column(**pageargs)
        

        __M_writer('\n\n\t\t</div>\n')
        __M_writer('\n')
        __M_writer('\t\t<div class="col-md-6">\n\n\t\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_right_column'):
            context['self'].top_right_column(**pageargs)
        

        __M_writer('\n\n\t\t</div>\n')
        __M_writer('\n\t</div>\n')
        __M_writer('\n')
        __M_writer('\t<hr>\n')
        __M_writer('\n')
        __M_writer('\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'view_table'):
            context['self'].view_table(**pageargs)
        

        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\t<div class="spacer"></div>\n\t<div class="spacer"></div>\n\t<div class="spacer"></div>\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def create_button_block():
            return render_create_button_block(context)
        def page_title_h1():
            return render_page_title_h1(context)
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('\n\t\t<div class="row">\n\t\t\t\n')
        __M_writer('\t\t\t<div class="col-md-8">\n\n\t\t\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title_h1'):
            context['self'].page_title_h1(**pageargs)
        

        __M_writer('\n\t\t\t\t\n\t\t\t</div>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<div class="col-md-4">\n\t\t\t\t<div class="create_button">\n\n\t\t\t\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'create_button_block'):
            context['self'].create_button_block(**pageargs)
        

        __M_writer('\n\t\t\t\t\t\n\t\t\t\t</div>\n\t\t\t\t\n\t\t\t</div>\n')
        __M_writer('\n\t\t</div>\n\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_view_table(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def view_table():
            return render_view_table(context)
        __M_writer = context.writer()
        __M_writer('\n\t  \n\t\t\t\n\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "/base_admin/templates/View.htm", "line_map": {"51": 19, "130": 53, "136": 27, "143": 27, "144": 28, "145": 28, "146": 29, "147": 29, "148": 30, "149": 30, "155": 33, "27": 0, "173": 33, "174": 36, "179": 63, "180": 65, "181": 67, "182": 70, "52": 21, "187": 90, "188": 94, "189": 96, "62": 31, "194": 120, "195": 124, "196": 127, "197": 129, "198": 131, "199": 133, "72": 72, "204": 136, "205": 138, "78": 72, "79": 75, "80": 89, "206": 140, "86": 98, "57": 25, "207": 144, "92": 98, "93": 101, "94": 119, "223": 36, "224": 40, "100": 23, "229": 44, "230": 48, "231": 50, "106": 23, "236": 55, "237": 61, "112": 42, "243": 133, "118": 42, "249": 133, "255": 249, "124": 53, "213": 36}, "filename": "/Users/John/DevProjects/Repositories/chef/base_admin/templates/View.htm"}
__M_END_METADATA
"""
