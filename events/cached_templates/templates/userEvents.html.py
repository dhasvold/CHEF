# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427491336.670804
_enable_loop = True
_template_filename = 'C:\\Users\\Derik\\PycharmProjects\\chef-master\\events\\templates/userEvents.html'
_template_uri = 'userEvents.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['paper_elements_import', 'extra_links', 'content', 'page_title', 'tab_title']


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
        def content():
            return render_content(context._locals(__M_locals))
        events = context.get('events', UNDEFINED)
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def paper_elements_import():
            return render_paper_elements_import(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        def extra_links():
            return render_extra_links(context._locals(__M_locals))
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


def render_paper_elements_import(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def paper_elements_import():
            return render_paper_elements_import(context)
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


def render_extra_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def extra_links():
            return render_extra_links(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_admin/styles/View.css">\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
        events = context.get('events', UNDEFINED)
        def page_title():
            return render_page_title(context)
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
        __M_writer('\r\n')
        __M_writer('\t<table class="table table-hover table-bordered">\r\n\t\t<thead>\r\n\t\t\t<tr>\r\n\t\t\t\t<th>\r\n\t\t\t\t\t<paper-button raised class="">Select All</paper-button>\r\n\t\t\t\t</th>\r\n\t\t\t\t<th>\r\n\t\t\t\t\tName\r\n\t\t\t\t</th>\r\n\t\t\t\t<th>\r\n\t\t\t\t\tStart Date\r\n\t\t\t\t</th>\r\n\t\t\t\t<th>\r\n\t\t\t\t\tPhoto\r\n\t\t\t\t</th>\r\n                <th>\r\n\t\t\t\t\tDetails\r\n\t\t\t\t</th>\r\n\t\t\t</tr>\r\n\t\t</thead>\r\n\t\t<tbody>\r\n')
        for event in events:
            __M_writer('\t\t\t\t<tr>\r\n\t\t\t\t\t<td>\r\n\t\t\t\t\t\t<paper-checkbox></paper-checkbox>\r\n\t\t\t\t\t</td>\r\n\t\t\t\t\t<td>\r\n\t\t\t\t\t\t')
            __M_writer(str( event.name ))
            __M_writer('\r\n\t\t\t\t\t</td>\r\n\t\t\t\t\t<td>\r\n\t\t\t\t\t\t')
            __M_writer(str( event.start_date.strftime("%B %d, %Y") ))
            __M_writer('\r\n\t\t\t\t\t</td>\r\n\t\t\t\t\t<td>\r\n\t\t\t\t\t\t<img src="')
            __M_writer(str(STATIC_URL))
            __M_writer(str( event.related_image ))
            __M_writer('">\r\n\t\t\t\t\t</td>\r\n\t\t\t\t\t<td>\r\n\t\t\t\t\t\t<a class="button" href="/events/userEvents.eventAreas/')
            __M_writer(str( event.id ))
            __M_writer('/">\r\n\t\t\t\t\t\t\t<paper-button raised class="success_button">View Event Areas</paper-button>\r\n\t\t\t\t\t\t</a>\r\n\t\t\t\t\t</td>\r\n\t\t\t\t</tr>\r\n')
        __M_writer('\t\t</tbody>\r\n\t</table>\t\r\n')
        __M_writer('\r\n')
        __M_writer('\t<div class="spacer"></div>\r\n\t<div class="spacer"></div>\r\n\t<div class="spacer"></div>\r\n')
        __M_writer('\r\n')
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
        __M_writer('\t\t\t<div class="col-md-8">\r\n\t\t\t\t<h1>Scheduled Events</h1>\r\n\t\t\t</div>\r\n')
        __M_writer('\r\n\t\t</div>\r\n\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tab_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def tab_title():
            return render_tab_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n  Scheduled Events\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Derik\\PycharmProjects\\chef-master\\events\\templates/userEvents.html", "line_map": {"128": 60, "129": 62, "130": 64, "131": 85, "132": 86, "133": 91, "134": 91, "135": 94, "136": 94, "137": 97, "138": 97, "139": 97, "140": 100, "141": 100, "142": 106, "143": 109, "144": 111, "145": 115, "151": 27, "27": 0, "157": 27, "158": 31, "159": 35, "165": 10, "171": 10, "44": 6, "45": 8, "177": 171, "50": 12, "55": 18, "60": 22, "70": 14, "77": 14, "78": 15, "79": 15, "80": 16, "81": 16, "82": 17, "83": 17, "89": 20, "96": 20, "97": 21, "98": 21, "104": 24, "114": 24, "115": 27, "120": 37, "121": 39, "122": 41, "123": 44, "124": 49, "125": 51, "126": 55, "127": 58}, "source_encoding": "ascii", "uri": "userEvents.html"}
__M_END_METADATA
"""
