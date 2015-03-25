# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423205015.95166
_enable_loop = True
_template_filename = '/Users/John/DevProjects/Repositories/chef/events/templates/areas.html'
_template_uri = 'areas.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['tab_title', 'paper_elements_import', 'page_title', 'content']


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
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        event = context.get('event', UNDEFINED)
        areas = context.get('areas', UNDEFINED)
        def paper_elements_import():
            return render_paper_elements_import(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
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


def render_tab_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def tab_title():
            return render_tab_title(context)
        event = context.get('event', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  Areas for ')
        __M_writer(str( event.name ))
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
        __M_writer('base_app/styles/bower_components/paper-checkbox/paper-checkbox.html">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        event = context.get('event', UNDEFINED)
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('\n\t\t<div class="row">\n\t\t\t\n')
        __M_writer('\t\t\t<div class="col-md-8">\n\t\t\t\t<h1>Areas for ')
        __M_writer(str( event.name ))
        __M_writer('</h1>\n\t\t\t</div>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<div class="col-md-4">\n\t\t\t\t<div class="create_button">\n\t\t\t\t\t<a class="button" href="/events/areas.create/')
        __M_writer(str( event.id ))
        __M_writer('">\n\t\t\t\t\t\t<paper-button class="create_button" raised>Create new Area</paper-button>\n\t\t\t\t\t</a>\n\t\t\t\t</div>\n\t\t\t\t\n\t\t\t</div>\n')
        __M_writer('\n\t\t</div>\n\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        event = context.get('event', UNDEFINED)
        def page_title():
            return render_page_title(context)
        areas = context.get('areas', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\t\n')
        __M_writer('\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\t<div class="row">\n\t\t\n')
        __M_writer('\t\t<div class="col-md-6">\n\n')
        __M_writer('\t\t\t<h3>Batch Options</h3>\n\t\t\t\n\t\t\t<div class="dropdown">\n\t\t\t\t<button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropwdown" aria-expanded="true">\n\t\t\t\t\tBatch Options\n\t\t\t\t\t<span class="caret"></span>\n\t\t\t\t</button>\n\t\t\t\t<ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1">\n\t\t\t\t\t<li role="presentation">Delete</li>\n\t\t\t\t</ul>\n\t\t\t</div>\n\n\t\t\t<paper-button class="success_button run_batch" raised>Submit</paper-button>\n\n')
        __M_writer('\n\t\t</div>\n')
        __M_writer('\n')
        __M_writer('\t\t<div class="col-md-6">\n\t\t\t\n')
        __M_writer('\t\t\t<h3>Filter Options</h3>\n\t\t\t\n\t\t\t<div class="dropdown">\n\t\t\t\t<button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropwdown" aria-expanded="true">\n\t\t\t\t\tFilter Options\n\t\t\t\t\t<span class="caret"></span>\n\t\t\t\t</button>\n\t\t\t\t<ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1">\n\t\t\t\t\t<li role="presentation">Delete</li>\n\t\t\t\t</ul>\n\t\t\t</div>\n\n\t\t\t<paper-input-decorator class="short" floatingLabel label="Criteria">\n\t\t\t\t<input is="core-input"></input>\n\t\t\t</paper-input-decorator>\n\n\t\t\t<paper-button class="success_button apply_filter" raised>Submit</paper-button>\n')
        __M_writer('\n\t\t</div>\n')
        __M_writer('\n\t</div>\n')
        __M_writer('\n')
        __M_writer('\t<hr>\n')
        __M_writer('\n')
        __M_writer('\t<table class="table table-hover table-bordered">\n\t\t<thead>\n\t\t\t<tr>\n\t\t\t\t<th>\n\t\t\t\t\t<paper-button raised class="">Select All</paper-button>\n\t\t\t\t</th>\n\t\t\t\t<th>\n\t\t\t\t\tName\n\t\t\t\t</th>\n\t\t\t\t<th>\n\t\t\t\t\tPlace Number\n\t\t\t\t</th>\n\t\t\t\t<th>\n\t\t\t\t\tActions\n\t\t\t\t</th>\n\t\t\t</tr>\n\t\t</thead>\n\t\t<tbody>\n')
        for area in areas:
            __M_writer('\t\t\t\t<tr>\n\t\t\t\t\t<td>\n\t\t\t\t\t\t<paper-checkbox></paper-checkbox>\n\t\t\t\t\t</td>\n\t\t\t\t\t<td>\n\t\t\t\t\t\t')
            __M_writer(str( area.name ))
            __M_writer('\n\t\t\t\t\t</td>\n\t\t\t\t\t<td>\n\t\t\t\t\t\t')
            __M_writer(str( area.place_number ))
            __M_writer('\n\t\t\t\t\t</td>\n\t\t\t\t\t<td>\n\t\t\t\t\t\t<a class="button" href="/events/events.edit/')
            __M_writer(str( event.id ))
            __M_writer('">\n\t\t\t\t\t\t\t<paper-button raised class="success_button">Event Info</paper-button>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t\t<a class="button" href="/events/areas.edit/')
            __M_writer(str( event.id ))
            __M_writer('/')
            __M_writer(str( area.id ))
            __M_writer('">\n\t\t\t\t\t\t\t<paper-button raised class="edit_button">Edit</paper-button>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t\t<a class="button" href="/events/areas.delete/')
            __M_writer(str( event.id ))
            __M_writer('/')
            __M_writer(str( area.id ))
            __M_writer('">\n\t\t\t\t\t\t\t<paper-button raised class="delete_button">Delete</paper-button>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t</td>\n\t\t\t\t</tr>\n')
        __M_writer('\t\t</tbody>\n\t</table>\t\n')
        __M_writer('\n')
        __M_writer('\t<div class="spacer"></div>\n\t<div class="spacer"></div>\n\t<div class="spacer"></div>\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "areas.html", "filename": "/Users/John/DevProjects/Repositories/chef/events/templates/areas.html", "source_encoding": "ascii", "line_map": {"129": 21, "130": 24, "135": 45, "136": 47, "137": 49, "138": 52, "139": 55, "140": 70, "141": 73, "142": 75, "143": 78, "144": 96, "145": 99, "146": 102, "147": 104, "148": 106, "149": 108, "150": 126, "151": 127, "152": 132, "153": 132, "154": 135, "27": 0, "156": 138, "157": 138, "158": 141, "159": 141, "160": 141, "161": 141, "162": 144, "155": 135, "164": 144, "165": 144, "166": 150, "167": 153, "168": 155, "169": 159, "43": 7, "44": 9, "175": 169, "49": 13, "54": 19, "64": 11, "71": 11, "72": 12, "73": 12, "79": 15, "163": 144, "86": 15, "87": 16, "88": 16, "89": 17, "90": 17, "91": 18, "92": 18, "98": 24, "105": 24, "106": 28, "107": 29, "108": 29, "109": 32, "110": 34, "111": 36, "112": 36, "113": 43, "119": 21}}
__M_END_METADATA
"""
