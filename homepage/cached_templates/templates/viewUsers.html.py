# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422476652.194877
_enable_loop = True
_template_filename = '/Users/John/DevProjects/chef/homepage/templates/users.html'
_template_uri = 'users.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['tab_title', 'content', 'paper_elements_import', 'footer_links', 'navbar_links']


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
    return runtime._inherit_from(context, '/base_app/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
        def paper_elements_import():
            return render_paper_elements_import(context._locals(__M_locals))
        def navbar_links():
            return render_navbar_links(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        users = context.get('users', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def footer_links():
            return render_footer_links(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'tab_title'):
            context['self'].tab_title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'paper_elements_import'):
            context['self'].paper_elements_import(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_links'):
            context['self'].navbar_links(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer_links'):
            context['self'].footer_links(**pageargs)
        

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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        users = context.get('users', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n\t<div class="page_title">\n\t\t<h1>View Users</h1>\n\t</div>\n\n')
        __M_writer('\t<div class="row">\n\t\t\n')
        __M_writer('\t\t<div class="col-md-6">\n\n')
        __M_writer('\t\t\t<h3>Batch Options</h3>\n\t\t\t\n\t\t\t<div class="dropdown">\n\t\t\t\t<button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropwdown" aria-expanded="true">\n\t\t\t\t\tBatch Options\n\t\t\t\t\t<span class="caret"></span>\n\t\t\t\t</button>\n\t\t\t\t<ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1">\n\t\t\t\t\t<li role="presentation">Delete</li>\n\t\t\t\t</ul>\n\t\t\t</div>\n\n\t\t\t<paper-button class="success_button run_batch" raised>Submit</paper-button>\n\n')
        __M_writer('\n\t\t</div>\n')
        __M_writer('\n')
        __M_writer('\t\t<div class="col-md-6">\n\t\t\t\n')
        __M_writer('\t\t\t<h3>Filter Options</h3>\n\t\t\t\n\t\t\t<div class="dropdown">\n\t\t\t\t<button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropwdown" aria-expanded="true">\n\t\t\t\t\tFilter Options\n\t\t\t\t\t<span class="caret"></span>\n\t\t\t\t</button>\n\t\t\t\t<ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1">\n\t\t\t\t\t<li role="presentation">Delete</li>\n\t\t\t\t</ul>\n\t\t\t</div>\n\n\t\t\t<paper-input-decorator class="short" floatingLabel label="Criteria">\n\t\t\t\t<input is="core-input"></input>\n\t\t\t</paper-input-decorator>\n\n\t\t\t<paper-button class="success_button apply_filter" raised>Submit</paper-button>\n')
        __M_writer('\n\t\t</div>\n')
        __M_writer('\n\t</div>\n')
        __M_writer('\n\t<table class="table table-hover table-bordered">\n\t\t<thead>\n\t\t\t<tr>\n\t\t\t\t<th>\n\t\t\t\t\t<paper-button raised class="">Select All</paper-button>\n\t\t\t\t</th>\n\t\t\t\t<th>\n\t\t\t\t\tName\n\t\t\t\t</th>\n\t\t\t\t<th>\n\t\t\t\t\tGroup\n\t\t\t\t</th>\n\t\t\t\t<th>\n\t\t\t\t\tActions\n\t\t\t\t</th>\n\t\t\t</tr>\n\t\t</thead>\n\t\t<tbody>\n')
        for user in users:
            __M_writer('\t\t\t\t<tr>\n\t\t\t\t\t<td>\n\t\t\t\t\t\t<paper-checkbox></paper-checkbox>\n\t\t\t\t\t</td>\n\t\t\t\t\t<td>\n\t\t\t\t\t\t')
            __M_writer(str( user.first_name ))
            __M_writer('\n\t\t\t\t\t</td>\n\t\t\t\t\t<td>\n\t\t\t\t\t\t')
            __M_writer(str( user.role ))
            __M_writer('\n\t\t\t\t\t</td>\n\t\t\t\t\t<td>\n\t\t\t\t\t\t<paper-button raised class="success_button">View</paper-button>\n\t\t\t\t\t\t<paper-button raised class="edit_button"><a href="/homepage/users.edit/')
            __M_writer(str( user.id ))
            __M_writer('">Edit</paper-button>\n\t\t\t\t\t\t<paper-button raised class="delete_button">Delete</paper-button>\n\t\t\t\t\t</td>\n\t\t\t\t</tr>\n')
        __M_writer('\t\t</tbody>\n\t</table>\t\n\n')
        __M_writer('\t<div class="spacer"></div>\n\t<div class="spacer"></div>\n\t<div class="spacer"></div>\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_paper_elements_import(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def paper_elements_import():
            return render_paper_elements_import(context)
        __M_writer = context.writer()
        __M_writer('\n\t<link rel="import" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_app/styles/bower_components/paper-input/paper-input.html">\n\t<link rel="import" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_app/styles/bower_components/paper-button/paper-button.html">\n\t<link rel="import" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_app/styles/bower_components/paper-checkbox/paper-checkbox.html">\n\t<link rel="import" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_app/styles/bower_components/core-menu/core-menu.html">\n\t<link rel="import" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_app/styles/bower_components/paper-dropdown/paper-dropdown.html">\n\t<link rel="import" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_app/styles/bower_components/paper-item/paper-item.html">\n\t<link rel="import" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_app/styles/bower_components/paper-dropdown-menu/paper-dropdown-menu.html">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer_links():
            return render_footer_links(context)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\t<div class="row">\n\n')
        __M_writer('\t\t<div class="col-md-4">\n\t\t  \t<h3>Users</h3>\n\t  \t\t<ul>\n\t\t\t  \t<li><a href="#">Add User</a></li>\n\t\t\t    <li><a href="#">View Users</a></li>\n\t  \t\t</ul>\n\t\t</div>\n')
        __M_writer('\n')
        __M_writer('\t\t<div class="col-md-4">\n\t\t  \t<h3>Items</h3>\n\t\t  \t<ul>\n\t\t    \t<li><a href="#">Add New Rental Item</a></li>\n\t\t    \t<li><a href="#">Add New Product</a></li>\n\t\t    \t<li><a href="#">View Rental Items</a></li>\n\t\t    \t<li><a href="#">View Products</a></li>\n\t\t  \t</ul>\n\t\t</div>\n')
        __M_writer('\n')
        __M_writer('\t\t<div class="col-md-4">\n\t\t  \t<h3>Events</h3>\n\t\t  \t<ul>\n\t\t    \t<li><a href="#">Add New Event Template</a></li>\n\t\t    \t<li><a href="#">View Event Templates</a></li>\n\t\t    \t<li><a href="#">Schedule New Event</a></li>\n\t\t    \t<li><a href="#">View Scheduled Events</a></li>\n\t\t  \t</ul>\n\t\t</div>\n')
        __M_writer('\n\t</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def navbar_links():
            return render_navbar_links(context)
        __M_writer = context.writer()
        __M_writer('\n  \t<ul class="nav navbar-nav navbar-right">\n\t    <li><a href="/homepage/index/">Home</a></li>\n\t    <li><a href="#">Users</a></li>\n\t    <li><a href="#">Items</a></li>\n\t    <li><a href="#">Events</a></li>\n\t    <li><a href="#">Logout</a></li>\n  \t</ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"128": 15, "129": 16, "130": 16, "131": 17, "132": 17, "133": 18, "134": 18, "135": 19, "136": 19, "137": 20, "138": 20, "139": 21, "140": 21, "141": 22, "142": 22, "173": 25, "148": 143, "154": 143, "27": 0, "156": 148, "157": 156, "158": 158, "159": 168, "160": 170, "161": 180, "155": 145, "167": 25, "44": 7, "45": 9, "50": 13, "179": 173, "55": 23, "60": 33, "65": 141, "75": 11, "81": 11, "87": 35, "94": 35, "95": 42, "96": 45, "97": 48, "98": 63, "99": 66, "100": 68, "101": 71, "102": 89, "103": 92, "104": 95, "105": 114, "106": 115, "107": 120, "108": 120, "109": 123, "110": 123, "111": 127, "112": 127, "113": 132, "114": 136, "115": 140, "121": 15}, "uri": "users.html", "source_encoding": "ascii", "filename": "/Users/John/DevProjects/chef/homepage/templates/users.html"}
__M_END_METADATA
"""
