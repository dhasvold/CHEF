# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422077096.046514
_enable_loop = True
_template_filename = '/Users/John/DevProjects/chef/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['full_width_content', 'sidebar', 'paper_elements_import', 'navbar_links', 'footer_links', 'tab_title', 'extra_links', 'content']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        def sidebar():
            return render_sidebar(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def footer_links():
            return render_footer_links(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def full_width_content():
            return render_full_width_content(context._locals(__M_locals))
        def paper_elements_import():
            return render_paper_elements_import(context._locals(__M_locals))
        def navbar_links():
            return render_navbar_links(context._locals(__M_locals))
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
        def extra_links():
            return render_extra_links(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
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
        __M_writer("    <link href='http://fonts.googleapis.com/css?family=Arvo:400,400italic|Open+Sans:300italic,700italic,700,300|Pinyon+Script' rel='stylesheet' type='text/css'>\n\n")
        __M_writer('    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\n\n')
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


def render_full_width_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def full_width_content():
            return render_full_width_content(context)
        def sidebar():
            return render_sidebar(context)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('        <div class="wrapper">\n\n')
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


def render_paper_elements_import(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def paper_elements_import():
            return render_paper_elements_import(context)
        __M_writer = context.writer()
        __M_writer('\n      \n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def navbar_links():
            return render_navbar_links(context)
        __M_writer = context.writer()
        __M_writer('\n              <ul class="nav navbar-nav navbar-right">\n                <li><a href="/homepage/index/">Home</a></li>\n                <li><a href="/homepage/about/">About</a></li>\n                <li><a href="/homepage/terms/">Terms</a></li>\n                <li><a href="/homepage/contact/">Contact</a></li>\n                <li><a href="/homepage/login/">Login</a></li>\n              </ul>\n            ')
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


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "base.htm", "line_map": {"131": 91, "132": 94, "133": 97, "138": 99, "139": 101, "140": 103, "16": 4, "145": 105, "18": 0, "147": 110, "215": 14, "171": 37, "153": 97, "239": 103, "159": 97, "197": 128, "165": 37, "146": 107, "177": 69, "42": 2, "43": 4, "44": 5, "203": 165, "48": 5, "49": 13, "54": 16, "55": 19, "56": 21, "57": 24, "58": 27, "59": 31, "60": 34, "61": 34, "62": 34, "63": 37, "195": 122, "68": 39, "69": 42, "198": 138, "199": 140, "200": 150, "201": 152, "74": 44, "75": 47, "76": 47, "77": 47, "78": 53, "79": 57, "80": 69, "209": 14, "227": 42, "85": 77, "86": 79, "87": 82, "88": 86, "89": 88, "90": 91, "221": 42, "95": 111, "96": 113, "97": 116, "98": 118, "99": 121, "196": 125, "104": 166, "105": 169, "106": 172, "107": 184, "108": 186, "109": 188, "110": 191, "111": 194, "112": 197, "113": 199, "114": 199, "115": 199, "245": 239, "189": 122, "233": 103, "121": 91, "183": 69, "202": 162}, "filename": "/Users/John/DevProjects/chef/homepage/templates/base.htm"}
__M_END_METADATA
"""
