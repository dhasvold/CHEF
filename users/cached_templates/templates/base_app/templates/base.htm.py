# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426525532.378965
_enable_loop = True
_template_filename = '/Users/John/DevProjects/Repositories/chef/base_app/templates/base.htm'
_template_uri = '/base_app/templates/base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['sidebar', 'tab_title', 'extra_links', 'navbar_links', 'full_width_content', 'page_title', 'paper_elements_import', 'content', 'footer_links']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
        def paper_elements_import():
            return render_paper_elements_import(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def extra_links():
            return render_extra_links(context._locals(__M_locals))
        def navbar_links():
            return render_navbar_links(context._locals(__M_locals))
        def footer_links():
            return render_footer_links(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def full_width_content():
            return render_full_width_content(context._locals(__M_locals))
        perms = context.get('perms', UNDEFINED)
        def sidebar():
            return render_sidebar(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n  <meta charset="UTF-8">\n  <head>\n    \n')
        __M_writer('    <title>\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'tab_title'):
            context['self'].tab_title(**pageargs)
        

        __M_writer('\n    </title>\n')
        __M_writer('    \n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n\n')
        __M_writer('    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_app/media/jquery_form_plugin.js"></script>\n\n')
        __M_writer('    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_app/media/load_modal.js"></script>\n\n')
        __M_writer("    <link href='http://fonts.googleapis.com/css?family=Arvo:400,400italic|Open+Sans:300italic,700italic,700,300|Pinyon+Script' rel='stylesheet' type='text/css'>\n\n")
        __M_writer('    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\n\n')
        __M_writer('    <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.6.3/css/bootstrap-select.min.css">\n    <script src="//cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.6.3/js/bootstrap-select.min.js"></script>\n\n')
        __M_writer('    <link href="http://maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet">\n\n')
        __M_writer('    <link rel="icon" type="image/x-icon" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/favicon.ico" />\n\n')
        __M_writer('    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'paper_elements_import'):
            context['self'].paper_elements_import(**pageargs)
        

        __M_writer('\n\n')
        __M_writer('    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_links'):
            context['self'].extra_links(**pageargs)
        

        __M_writer('\n  \n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n  \n  </head>\n  <body> \n\n')
        __M_writer('    <div class="navbar navbar-default custom_header" role="navigation">\n      <div class="container-fluid">\n\n')
        __M_writer('        <div class="wrapper">\n          <div class="navbar-header">\n            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">\n              <span class="icon-bar"></span>\n              <span class="icon-bar"></span>\n              <span class="icon-bar"></span>\n            </button>\n            <a class="navbar-brand" id="main_title" href="/homepage/index">Colonial Heritage Foundation</a>\n          </div>\n          <div class="navbar-collapse collapse">\n            \n')
        __M_writer('            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_links'):
            context['self'].navbar_links(**pageargs)
        

        __M_writer('\n')
        __M_writer('          </div>\n        </div>\n')
        __M_writer('\n      </div>\n    </div>\n')
        __M_writer('\n')
        __M_writer('    <div class="container-fluid main_content">\n\n')
        __M_writer('      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'full_width_content'):
            context['self'].full_width_content(**pageargs)
        

        __M_writer('    \n')
        __M_writer('\n    </div>\n')
        __M_writer('\n')
        __M_writer('    <footer class="footer">\n\n')
        __M_writer('      <div class="wrapper">\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer_links'):
            context['self'].footer_links(**pageargs)
        

        __M_writer('\n\n')
        __M_writer('        <div class="center">\n\n')
        __M_writer('          <div class="social_media">\n            <a href="http://facebook.com" target="_blank">\n              <i class="fa fa-facebook-square fa-2x"></i>  \n            </a>\n            <a href="http://instagram.com" target="_blank">\n              <i class="fa fa-instagram fa-2x"></i>  \n            </a>\n            <a href="http://twitter.com" target="_blank">\n              <i class="fa fa-twitter-square fa-2x"></i>  \n            </a>\n          </div>\n')
        __M_writer('\n')
        __M_writer('          <p>Copyright 2015</p>\n')
        __M_writer('\n        </div>\n')
        __M_writer('\n      </div>\n')
        __M_writer('\n    </footer>\n')
        __M_writer('  \n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n  \n  </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sidebar(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def sidebar():
            return render_sidebar(context)
        __M_writer = context.writer()
        __M_writer('\n\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tab_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def tab_title():
            return render_tab_title(context)
        __M_writer = context.writer()
        __M_writer('\n        Colonial Heritage Foundation\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_links():
            return render_extra_links(context)
        __M_writer = context.writer()
        __M_writer('\n      \n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        perms = context.get('perms', UNDEFINED)
        def navbar_links():
            return render_navbar_links(context)
        __M_writer = context.writer()
        __M_writer('\n              <ul class="nav navbar-nav navbar-right">\n')
        if request.user.username == '':
            __M_writer('                  <li><a href="/homepage/index/">Home</a></li>\n                  <li><a href="/homepage/about/">About</a></li>\n                  <li><a href="/homepage/terms/">Terms</a></li>\n                  <li><a href="/homepage/contact/">Contact</a></li>\n                  <li><a href="/products/products/">Products</a></li>\n                  <li><a href="/account/NewUser/">Sign Up</a></li>\n                  <li><a id="login_link" href="#">Login</a></li>\n')
        else:
            __M_writer('                  <li class="dropdown">\n                    <a class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false" href="#">Home</a>\n                    <ul class="dropdown-menu dropdown-menu-left" role="menu">\n                      <li><a href="/homepage/index/">Home Page</a></li>\n                      <li><a href="/homepage/about/">About</a></li>\n                      <li><a href="/homepage/terms/">Terms</a></li>\n                      <li><a href="/homepage/contact/">Contact</a></li>\n                    </ul>\n                  </li>\n                  <li><a href="/products/products/">Products</a></li>\n')
            if perms['base_app']['add_inventory'] or perms['base_app']['change_inventory'] or perms['base_app']['delete_inventory']:
                __M_writer('                    <li class="dropdown">\n                      <a class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false" href="#">Inventory</a>\n                      <ul class="dropdown-menu dropdown-menu-left" role="menu">\n                        <li><a href="/inventory/items.create/1">Add Non-Wardrobe Item</a></li>\n                        <li><a href="/inventory/items.create/2">Add Wardrobe Item</a></li>\n                        <li><a href="/inventory/items/">View Items</a></li>\n                        <li class="divider"></li>\n                        <li><a href="/inventory/products/">View Products</a></li>\n                      </ul>\n                    </li>\n')
            if perms['base_app']['add_event'] or perms['base_app']['change_event'] or perms['base_app']['delete_event']:
                __M_writer('                    <li class="dropdown">\n                      <a class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false" href="#">Events</a>\n                      <ul class="dropdown-menu dropdown-menu-left" role="menu">\n                        <li><a href="/events/events.create">Schedule Event</a></li>\n                        <li><a href="/events/events/">View Events</a></li>\n                        <li class="divider"></li>\n                        <li><a href="#">Event Templates</a></li>\n                        <li class="divider"></li>\n                        <li><a href="/events/venues/">Venues</a></li>\n                      </ul>\n                    </li>\n')
            if perms['base_app']['add_user'] or perms['base_app']['change_user'] or perms['base_app']['delete_user']:
                __M_writer('                    <li class="dropdown">\n                      <a class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false" href="#">Users</a>\n                      <ul class="dropdown-menu dropdown-menu-left" role="menu">\n                        <li><a href="/users/users.create">Add User</a></li>\n                        <li><a href="/users/users/">View Users</a></li>\n')
                if perms['auth']['add_group'] or perms['auth']['change_group'] or perms['auth']['delete_group']:
                    __M_writer('                          <li class="divider"></li>\n                          <li><a href="/users/groups/">Groups</a></li>\n')
                __M_writer('                      </ul>\n                    </li>\n')
            if perms['base_app']['add_item'] or perms['base_app']['change_item'] or perms['base_app']['delete_item']:
                __M_writer('                    <li class="dropdown">\n                      <a class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false" href="#">Reports</a>\n                      <ul class="dropdown-menu dropdown-menu-left" role="menu">\n                        <li><a href="/reports/rentals.overdue">Overdue Items</a></li>\n                      </ul>\n                    </li>\n')
            __M_writer('                  <li class="dropdown">\n                    <a class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false" href="#">')
            __M_writer(str( request.user.first_name ))
            __M_writer('</a>\n                    <ul class="dropdown-menu dropdown-menu-left" role="menu">\n                      <li><a href="/account/MyAccount">My Account</a></li>\n                      <li><a id="cart_link" href="#">My Cart</a></li>\n                      <li><a href="/homepage/login.logout_user">Log Out</a></li>\n                    </ul> \n                  </li>                 \n')
        __M_writer('              </ul>\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_full_width_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def sidebar():
            return render_sidebar(context)
        def full_width_content():
            return render_full_width_content(context)
        def page_title():
            return render_page_title(context)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('        <div class="wrapper">\n\n')
        __M_writer('        <div class="page_title">\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\n        </div>\n')
        __M_writer('\n')
        __M_writer('        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sidebar'):
            context['self'].sidebar(**pageargs)
        

        __M_writer('\n')
        __M_writer('\n')
        __M_writer('          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        __M_writer('\n        </div>\n')
        __M_writer('\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('\n              \n          ')
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
        __M_writer('\n      <link rel="import" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_app/styles/bower_components/paper-input/paper-input.html">\n      <link rel="import" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_app/styles/bower_components/paper-button/paper-button.html">\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n             If you are seeing this, something went wrong...\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer_links():
            return render_footer_links(context)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('          <div class="row">\n            \n')
        __M_writer('            <div class="col-md-4">\n              <h3>Main Menu</h3>\n              <ul>\n                <li><a href="/homepage/index/">Home</a></li>\n                <li><a href="/homepage/about/">About</a></li>\n                <li><a href="/homepage/terms/">Terms</a></li>\n                <li><a href="/homepage/contact/">Contact</a></li>\n              </ul>\n            </div>\n')
        __M_writer('\n')
        __M_writer('            <div class="col-md-4">\n              <h3>Rentals</h3>\n              <ul>\n                <li><a href="/homepage/index/">Home</a></li>\n                <li><a href="/homepage/about/">About</a></li>\n                <li><a href="/homepage/terms/">Terms</a></li>\n                <li><a href="/homepage/contact/">Contact</a></li>\n              </ul>\n            </div>\n')
        __M_writer('\n')
        __M_writer('            <div class="col-md-4">\n              <h3>Shop</h3>\n              <ul>\n                <li><a href="/homepage/index/">Home</a></li>\n                <li><a href="/homepage/about/">About</a></li>\n                <li><a href="/homepage/terms/">Terms</a></li>\n                <li><a href="/homepage/contact/">Contact</a></li>\n              </ul>\n            </div>\n')
        __M_writer('\n          </div>\n')
        __M_writer('\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "/base_app/templates/base.htm", "line_map": {"260": 55, "261": 56, "262": 56, "263": 57, "264": 57, "270": 199, "16": 12, "18": 0, "276": 199, "302": 296, "282": 218, "288": 218, "289": 221, "290": 224, "291": 234, "292": 236, "293": 246, "294": 248, "295": 258, "296": 261, "45": 10, "46": 12, "47": 13, "51": 13, "52": 21, "57": 24, "58": 27, "59": 29, "60": 32, "61": 32, "62": 32, "63": 35, "64": 35, "65": 35, "66": 38, "67": 41, "68": 45, "69": 49, "70": 52, "71": 52, "72": 52, "73": 55, "78": 58, "79": 61, "84": 63, "85": 66, "86": 66, "87": 66, "88": 72, "89": 76, "90": 88, "95": 165, "96": 167, "97": 170, "98": 174, "99": 176, "100": 179, "105": 207, "106": 209, "107": 212, "108": 214, "109": 217, "114": 262, "115": 265, "116": 268, "117": 280, "118": 282, "119": 284, "120": 287, "121": 290, "122": 293, "123": 295, "124": 295, "125": 295, "131": 193, "137": 193, "143": 22, "149": 22, "155": 61, "161": 61, "167": 88, "175": 88, "176": 90, "177": 91, "178": 98, "179": 99, "180": 109, "181": 110, "182": 121, "183": 122, "184": 134, "185": 135, "186": 140, "187": 141, "188": 144, "189": 147, "190": 148, "191": 155, "192": 156, "193": 156, "194": 164, "200": 179, "212": 179, "213": 182, "214": 185, "219": 188, "220": 191, "221": 193, "226": 195, "227": 197, "228": 199, "233": 201, "234": 203, "235": 206, "241": 186, "247": 186, "253": 55}, "source_encoding": "ascii", "filename": "/Users/John/DevProjects/Repositories/chef/base_app/templates/base.htm"}
__M_END_METADATA
"""
