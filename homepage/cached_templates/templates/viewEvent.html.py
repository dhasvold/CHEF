# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422405386.993231
_enable_loop = True
_template_filename = '/Users/John/DevProjects/chef/homepage/templates/viewEvent.html'
_template_uri = 'viewEvent.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'navbar_links', 'tab_title', 'paper_elements_import', 'footer_links']


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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def footer_links():
            return render_footer_links(context._locals(__M_locals))
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
        def paper_elements_import():
            return render_paper_elements_import(context._locals(__M_locals))
        def navbar_links():
            return render_navbar_links(context._locals(__M_locals))
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n\t<div class="page_title">\n\t\t<h1>Event Information</h1>\n\t</div>\n\n')
        __M_writer('\t<div class="row">\n\n')
        __M_writer('\t <div class="col-md-8">\n')
        __M_writer('\t\t<form>\n\n')
        __M_writer('\t\t\t<paper-input-decorator floatingLabel label="Event Name">\n\t\t\t\t<input is="core-input"></input>\n\t\t\t</paper-input-decorator>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<paper-input-decorator floatingLabel label="Start Date">\n\t\t\t\t<input is="core-input"></input>\n\t\t\t</paper-input-decorator>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<paper-input-decorator floatingLabel label="End Date">\n\t\t\t\t<input is="core-input"></input>\n\t\t\t</paper-input-decorator>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<paper-input-decorator floatingLabel label="Description">\n\t\t\t\t<textarea is="core-input"></textarea>\n\t\t\t</paper-input-decorator>\n')
        __M_writer('\n\t\t\t<h3>Venue Information</h3>\n\n')
        __M_writer('\t\t\t<paper-input-decorator floatingLabel label="Venue Name">\n\t\t\t\t<input is="core-input"></input>\n\t\t\t</paper-input-decorator>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<paper-input-decorator floatingLabel label="Address">\n\t\t\t\t<input is="core-input"></input>\n\t\t\t</paper-input-decorator>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<paper-input-decorator floatingLabel label="City">\n\t\t\t\t<input is="core-input"></input>\n\t\t\t</paper-input-decorator>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<paper-dropdown-menu label="State">\n\t\t\t    <paper-dropdown class="dropdown">\n\t\t\t        <core-menu class="menu">\n\t\t\t            <paper-item>TX</paper-item>\n\t\t\t            <paper-item>TX</paper-item>\n\t\t\t            <paper-item>TX</paper-item>\n\t\t\t        </core-menu>\n\t\t\t    </paper-dropdown>\n\t\t\t</paper-dropdown-menu>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<paper-input-decorator floatingLabel class="short" label="ZIP">\n\t\t\t\t<input is="core-input"></input>\n\t\t\t</paper-input-decorator>\n')
        __M_writer('\n\t\t</form>\n')
        __M_writer('\t\t\t\n\t </div>\n')
        __M_writer('\n')
        __M_writer('\t <div class="col-md-4">\n\n\t \t<h3>Related Actions</h3>\n\n')
        __M_writer('\t\t<paper-button raised class="edit_button">Upload Map</paper-button>\n')
        __M_writer('\n')
        __M_writer('\t\t<paper-button raised class="success_button">View Related Areas</paper-button>\n')
        __M_writer('\n')
        __M_writer('\t\t<paper-button raised class="success_button">View Map</paper-button>\n')
        __M_writer('\n')
        __M_writer('\t\t<paper-button raised class="success_button">View Items for Sale</paper-button>\n')
        __M_writer('\n')
        __M_writer('\t\t<paper-button raised class="delete_button">Cancel Event</paper-button>\n')
        __M_writer('\n\t </div>\n')
        __M_writer('\n\t</div>\n')
        __M_writer('\n\t<div class="spacer"></div>\n\t<div class="spacer"></div>\n\t<div class="spacer"></div>\n\n')
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


def render_tab_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def tab_title():
            return render_tab_title(context)
        __M_writer = context.writer()
        __M_writer('\n  Event Information\n')
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


"""
__M_BEGIN_METADATA
{"line_map": {"128": 25, "192": 186, "134": 11, "140": 11, "146": 15, "153": 15, "154": 16, "27": 0, "156": 17, "157": 17, "158": 18, "159": 18, "160": 19, "161": 19, "162": 20, "155": 16, "164": 21, "163": 20, "166": 22, "167": 22, "43": 7, "44": 9, "173": 154, "49": 13, "179": 154, "180": 156, "181": 159, "54": 23, "183": 169, "184": 179, "185": 181, "186": 191, "59": 33, "64": 152, "182": 167, "74": 35, "80": 35, "81": 42, "82": 45, "83": 47, "84": 50, "85": 54, "86": 56, "87": 60, "88": 62, "89": 66, "90": 68, "91": 72, "92": 76, "93": 80, "94": 82, "95": 86, "96": 88, "97": 92, "98": 94, "99": 104, "100": 106, "101": 110, "102": 113, "103": 116, "104": 118, "105": 123, "106": 125, "107": 127, "108": 129, "109": 131, "110": 133, "111": 135, "112": 137, "113": 139, "114": 141, "115": 144, "116": 147, "122": 25, "165": 21}, "source_encoding": "ascii", "uri": "viewEvent.html", "filename": "/Users/John/DevProjects/chef/homepage/templates/viewEvent.html"}
__M_END_METADATA
"""
