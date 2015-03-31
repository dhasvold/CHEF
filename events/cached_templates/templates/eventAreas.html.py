# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427680070.5417
_enable_loop = True
_template_filename = 'C:\\Users\\Derik\\PycharmProjects\\chef-master\\events\\templates/eventAreas.html'
_template_uri = 'eventAreas.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['tab_title', 'page_title', 'extra_links', 'paper_elements_import', 'content']


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
        def extra_links():
            return render_extra_links(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
        areas = context.get('areas', UNDEFINED)
        def paper_elements_import():
            return render_paper_elements_import(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'tab_title'):
            context['self'].tab_title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'paper_elements_import'):
            context['self'].paper_elements_import(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_links'):
            context['self'].extra_links(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tab_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def tab_title():
            return render_tab_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n  Event Areas\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t\t<div class="row">\r\n\t\t\t\r\n')
        __M_writer('\t\t\t<div class="col-md-8">\r\n\t\t\t\t<h1>Event Areas</h1>\r\n\t\t\t</div>\r\n')
        __M_writer('\r\n\t\t</div>\r\n\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_links():
            return render_extra_links(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_admin/styles/View.css">\r\n')
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
        __M_writer('\r\n\t<link rel="import" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_app/styles/bower_components/paper-input/paper-input.html">\r\n\t<link rel="import" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_app/styles/bower_components/paper-button/paper-button.html">\r\n\t<link rel="import" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_app/styles/bower_components/paper-checkbox/paper-checkbox.html">\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        areas = context.get('areas', UNDEFINED)
        def page_title():
            return render_page_title(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t\r\n')
        __M_writer('\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer('\t<div class="row">\r\n\t\t\r\n')
        __M_writer('\t\t<div class="col-md-6">\r\n\r\n\r\n\t\t</div>\r\n')
        __M_writer('\r\n')
        __M_writer('\t\t<div class="col-md-6">\r\n\r\n\t\t</div>\r\n')
        __M_writer('\r\n\t</div>\r\n')
        __M_writer('\r\n')
        __M_writer('\t<hr>\r\n')
        __M_writer('\r\n\r\n\r\n')
        for area in areas:
            __M_writer('        <div id="spacer">\r\n            <h2>')
            __M_writer(str( area.name ))
            __M_writer('</h2>\r\n            <b>Description:</b> ')
            __M_writer(str( area.description ))
            __M_writer('\r\n            <br>\r\n            <b>Products for sale:</b>\r\n')
            for item in areas[area]:
                __M_writer('            <div>\r\n                <img src="')
                __M_writer(str( STATIC_URL))
                __M_writer(str( item.related_image ))
                __M_writer('"\r\n            </div>\r\n')
            __M_writer('\r\n        </div>\r\n')
        __M_writer('\r\n')
        __M_writer('\t<div class="spacer"></div>\r\n\t<div class="spacer"></div>\r\n\t<div class="spacer"></div>\r\n')
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "eventAreas.html", "line_map": {"130": 24, "140": 24, "141": 27, "146": 37, "147": 39, "148": 41, "149": 44, "150": 49, "151": 51, "152": 55, "153": 58, "154": 60, "27": 0, "156": 65, "157": 66, "158": 67, "159": 67, "160": 68, "161": 68, "162": 71, "155": 62, "164": 73, "165": 73, "166": 73, "167": 76, "168": 79, "169": 81, "170": 85, "44": 6, "45": 8, "176": 170, "50": 12, "55": 18, "60": 22, "70": 10, "76": 10, "82": 27, "163": 72, "88": 27, "89": 31, "90": 35, "96": 20, "103": 20, "104": 21, "105": 21, "111": 14, "118": 14, "119": 15, "120": 15, "121": 16, "122": 16, "123": 17, "124": 17}, "source_encoding": "ascii", "filename": "C:\\Users\\Derik\\PycharmProjects\\chef-master\\events\\templates/eventAreas.html"}
__M_END_METADATA
"""
