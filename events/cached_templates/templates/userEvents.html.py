# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428097020.347762
_enable_loop = True
_template_filename = '/home/dhasvold/PycharmProjects/chef-master/events/templates/userEvents.html'
_template_uri = 'userEvents.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['tab_title', 'page_title', 'paper_elements_import', 'extra_links', 'content']


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
        def extra_links():
            return render_extra_links(context._locals(__M_locals))
        events = context.get('events', UNDEFINED)
        def paper_elements_import():
            return render_paper_elements_import(context._locals(__M_locals))
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
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
        __M_writer('\r\n  Scheduled Events\r\n')
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
        def page_title():
            return render_page_title(context)
        def content():
            return render_content(context)
        events = context.get('events', UNDEFINED)
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


"""
__M_BEGIN_METADATA
{"filename": "/home/dhasvold/PycharmProjects/chef-master/events/templates/userEvents.html", "source_encoding": "ascii", "uri": "userEvents.html", "line_map": {"130": 24, "140": 24, "141": 27, "146": 37, "147": 39, "148": 41, "149": 44, "150": 49, "151": 51, "152": 55, "153": 58, "154": 60, "27": 0, "156": 64, "157": 85, "158": 86, "159": 91, "160": 91, "161": 94, "162": 94, "155": 62, "164": 97, "165": 97, "166": 100, "167": 100, "168": 106, "169": 109, "170": 111, "171": 115, "44": 6, "45": 8, "177": 171, "50": 12, "55": 18, "60": 22, "70": 10, "76": 10, "82": 27, "163": 97, "88": 27, "89": 31, "90": 35, "96": 14, "103": 14, "104": 15, "105": 15, "106": 16, "107": 16, "108": 17, "109": 17, "115": 20, "122": 20, "123": 21, "124": 21}}
__M_END_METADATA
"""
