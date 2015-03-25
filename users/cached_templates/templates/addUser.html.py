# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422494312.281946
_enable_loop = True
_template_filename = '/Users/John/DevProjects/Repositories/chef/users/templates/addUser.html'
_template_uri = 'addUser.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'tab_title', 'navbar_links', 'paper_elements_import', 'footer_links']


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
        def footer_links():
            return render_footer_links(context._locals(__M_locals))
        def navbar_links():
            return render_navbar_links(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\t<div class="page_title">\n\t\t<h1>Add a User</h1>\n\t</div>\n\n')
        __M_writer('\t<div class="row">\n\t\t\n')
        __M_writer('\t <div class="col-md-3">\n\t \t<img class="user_image" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/add-user.png">\n\n')
        __M_writer('\t\t<paper-button raised class="edit_button">Upload Image</paper-button>\n')
        __M_writer('\n\t </div>\n')
        __M_writer('\n')
        __M_writer('\t <div class="col-md-8">\n')
        __M_writer('\t\t<form>\n\n\t\t\t<h3>User Information</h3>\n\n')
        __M_writer('\t\t\t<paper-input-decorator floatingLabel label="Username">\n\t\t\t\t<input is="core-input"></input>\n\t\t\t</paper-input-decorator>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<paper-input-decorator floatingLabel label="Password">\n\t\t\t\t<input is="core-input"></input>\n\t\t\t</paper-input-decorator>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<paper-input-decorator floatingLabel label="Re-Enter Password">\n\t\t\t\t<input is="core-input"></input>\n\t\t\t</paper-input-decorator>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<paper-input-decorator floatingLabel label="First Name">\n\t\t\t\t<input is="core-input"></input>\n\t\t\t</paper-input-decorator>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<paper-input-decorator floatingLabel label="Last Name">\n\t\t\t\t<input is="core-input"></input>\n\t\t\t</paper-input-decorator>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<paper-input-decorator floatingLabel label="Email">\n\t\t\t\t<input is="core-input"></input>\n\t\t\t</paper-input-decorator>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<paper-input-decorator class="short" floatingLabel label="Phone">\n\t\t\t\t<input is="core-input"></input>\n\t\t\t</paper-input-decorator>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<paper-input-decorator floatingLabel label="Address 1">\n\t\t\t\t<input is="core-input"></input>\n\t\t\t</paper-input-decorator>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<paper-input-decorator floatingLabel label="Address 2">\n\t\t\t\t<input is="core-input"></input>\n\t\t\t</paper-input-decorator>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<paper-input-decorator floatingLabel label="City">\n\t\t\t\t<input is="core-input"></input>\n\t\t\t</paper-input-decorator>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<paper-dropdown-menu label="State">\n\t\t\t    <paper-dropdown class="dropdown">\n\t\t\t        <core-menu class="menu">\n\t\t\t            <paper-item>TX</paper-item>\n\t\t\t            <paper-item>TX</paper-item>\n\t\t\t            <paper-item>TX</paper-item>\n\t\t\t        </core-menu>\n\t\t\t    </paper-dropdown>\n\t\t\t</paper-dropdown-menu>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<paper-input-decorator floatingLabel class="short" label="ZIP">\n\t\t\t\t<input is="core-input"></input>\n\t\t\t</paper-input-decorator>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<paper-input-decorator floatingLabel label="Security Question">\n\t\t\t\t<input class="short" is="core-input"></input>\n\t\t\t</paper-input-decorator>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<paper-input-decorator floatingLabel label="Security Answer">\n\t\t\t\t<input class="short" is="core-input"></input>\n\t\t\t</paper-input-decorator>\n')
        __M_writer('\n\t\t\t<h3>Groups/Permissions</h3>\n\n')
        __M_writer('\t\t\t<div>\n\t\t\t\t<paper-radio-group selected="user">\n\t\t\t\t  \t<paper-radio-button name="user" label="User"></paper-radio-button>\n\t\t\t\t  \t<paper-radio-button name="manager" label="Manager"></paper-radio-button>\n\t\t\t\t  \t<paper-radio-button name="administrator" label="Administrator"></paper-radio-button>\n\t\t\t\t</paper-radio-group>\n\t\t\t</div>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<paper-button raised class="delete_button">Cancel</paper-button>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<paper-button raised class="success_button">Submit</paper-button>\n')
        __M_writer('\n\t\t</form>\n')
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
        __M_writer('\n  Add a User\n')
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
        __M_writer('base_app/styles/bower_components/paper-radio-group/paper-radio-group.html">\n\t<link rel="import" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_app/styles/bower_components/paper-radio-button/paper-radio-button.html">\n\t<link rel="import" href="')
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
{"line_map": {"27": 0, "43": 7, "44": 9, "49": 13, "54": 24, "59": 34, "64": 188, "74": 36, "81": 36, "82": 43, "83": 46, "84": 47, "85": 47, "86": 50, "87": 52, "88": 55, "89": 57, "90": 59, "91": 64, "92": 68, "93": 70, "94": 74, "95": 76, "96": 80, "97": 82, "98": 86, "99": 88, "100": 92, "101": 94, "102": 98, "103": 100, "104": 104, "105": 106, "106": 110, "107": 112, "108": 116, "109": 118, "110": 122, "111": 124, "112": 134, "113": 136, "114": 140, "115": 142, "116": 146, "117": 148, "118": 152, "119": 156, "120": 164, "121": 166, "122": 168, "123": 170, "124": 172, "125": 175, "126": 178, "127": 181, "128": 183, "129": 187, "135": 11, "141": 11, "147": 26, "153": 26, "159": 15, "166": 15, "167": 16, "168": 16, "169": 17, "170": 17, "171": 18, "172": 18, "173": 19, "174": 19, "175": 20, "176": 20, "177": 21, "178": 21, "179": 22, "180": 22, "181": 23, "182": 23, "188": 190, "194": 190, "195": 192, "196": 195, "197": 203, "198": 205, "199": 215, "200": 217, "201": 227, "207": 201}, "uri": "addUser.html", "source_encoding": "ascii", "filename": "/Users/John/DevProjects/Repositories/chef/users/templates/addUser.html"}
__M_END_METADATA
"""
