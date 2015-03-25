# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423375466.621125
_enable_loop = True
_template_filename = '/Users/John/DevProjects/Repositories/chef/inventory/templates/items.html'
_template_uri = 'items.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['page_title', 'content', 'tab_title', 'paper_elements_import']


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
        w_items = context.get('w_items', UNDEFINED)
        n_w_items = context.get('n_w_items', UNDEFINED)
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        str = context.get('str', UNDEFINED)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
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


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('\n\t\t<div class="row">\n\t\t\t\n')
        __M_writer('\t\t\t<div class="col-md-8">\n\t\t\t\t<h1>View Items</h1>\n\t\t\t</div>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<div class="col-md-4">\n\t\t\t\t\n\t\t\t</div>\n')
        __M_writer('\n\t\t</div>\n\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        def content():
            return render_content(context)
        n_w_items = context.get('n_w_items', UNDEFINED)
        w_items = context.get('w_items', UNDEFINED)
        str = context.get('str', UNDEFINED)
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
        __M_writer('\t<h3 class="table_title">Non Wardrobe Items</h3>\n')
        __M_writer('\n')
        __M_writer('\t<div class="create_button_div">\n\t\t<a class="button" href="/inventory/items.create/1">\n\t\t\t<paper-button class="create_button" raised>Add New Non-Wardrobe Item</paper-button>\n\t\t</a>\n\t</div>\n')
        __M_writer('\n')
        __M_writer('\t<table class="table table-hover table-bordered">\n\t\t<thead>\n\t\t\t<tr>\n\t\t\t\t<th>\n\t\t\t\t\t<paper-button raised class="">Select All</paper-button>\n\t\t\t\t</th>\n\t\t\t\t<th>\n\t\t\t\t\tName\n\t\t\t\t</th>\n\t\t\t\t<th>\n\t\t\t\t\tIs Rentable?\n\t\t\t\t</th>\n\t\t\t\t<th>\n\t\t\t\t\tActions\n\t\t\t\t</th>\n\t\t\t</tr>\n\t\t</thead>\n\t\t<tbody>\n')
        for item in n_w_items:
            __M_writer('\t\t\t\t<tr>\n\t\t\t\t\t<td>\n\t\t\t\t\t\t<paper-checkbox></paper-checkbox>\n\t\t\t\t\t</td>\n\t\t\t\t\t<td>\n\t\t\t\t\t\t')
            __M_writer(str( item.name ))
            __M_writer('\n\t\t\t\t\t</td>\n\t\t\t\t\t<td>\n\t\t\t\t\t\t')
            __M_writer(str( item.is_rentable ))
            __M_writer('\n\t\t\t\t\t</td>\n\t\t\t\t\t<td>\n\t\t\t\t\t\t<a class="button" href="/inventory/items.edit_non/')
            __M_writer(str( item.id ))
            __M_writer('/">\n\t\t\t\t\t\t\t<paper-button raised class="edit_button">Edit</paper-button>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t\t<a class="button" href="/inventory/items.delete_nw')
            __M_writer(str( item.id ))
            __M_writer('/1">\n\t\t\t\t\t\t\t<paper-button raised class="delete_button">Delete</paper-button>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t</td>\n\t\t\t\t</tr>\n')
        __M_writer('\t\t</tbody>\n\t</table>\t\n')
        __M_writer('\n')
        __M_writer('\t<hr>\n')
        __M_writer('\n')
        __M_writer('\t<h3 class="table_title">Wardrobe Items</h3>\n')
        __M_writer('\n')
        __M_writer('\t<div class="create_button_div">\n\t\t<a class="button" href="/inventory/items.create/2">\n\t\t\t<paper-button class="create_button" raised>Add New Wardrobe Item</paper-button>\n\t\t</a>\n\t</div>\n')
        __M_writer('\n')
        __M_writer('\t<table class="table table-hover table-bordered">\n\t\t<thead>\n\t\t\t<tr>\n\t\t\t\t<th>\n\t\t\t\t\t<paper-button raised class="">Select All</paper-button>\n\t\t\t\t</th>\n\t\t\t\t<th>\n\t\t\t\t\tName\n\t\t\t\t</th>\n\t\t\t\t<th>\n\t\t\t\t\tIs Rentable?\n\t\t\t\t</th>\n\t\t\t\t<th>\n\t\t\t\t\tGender\n\t\t\t\t</th>\n\t\t\t\t<th>\n\t\t\t\t\tSize\n\t\t\t\t</th>\n\t\t\t\t<th>\n\t\t\t\t\tActions\n\t\t\t\t</th>\n\t\t\t</tr>\n\t\t</thead>\n\t\t<tbody>\n')
        for item in w_items:
            __M_writer('\t\t\t\t<tr>\n\t\t\t\t\t<td>\n\t\t\t\t\t\t<paper-checkbox></paper-checkbox>\n\t\t\t\t\t</td>\n\t\t\t\t\t<td>\n\t\t\t\t\t\t')
            __M_writer(str( item.name ))
            __M_writer('\n\t\t\t\t\t</td>\n\t\t\t\t\t<td>\n\t\t\t\t\t\t')
            __M_writer(str( item.is_rentable ))
            __M_writer('\n\t\t\t\t\t</td>\n\t\t\t\t\t<td>\n\t\t\t\t\t\t')
            __M_writer(str( item.gender ))
            __M_writer('\n\t\t\t\t\t</td>\n\t\t\t\t\t<td>\n\t\t\t\t\t\t')
            __M_writer(str( str(item.size) + ' ' + item.size_modifier ))
            __M_writer('\n\t\t\t\t\t</td>\n\t\t\t\t\t<td>\n\t\t\t\t\t\t<a class="button" href="/inventory/items.edit_w/')
            __M_writer(str( item.id ))
            __M_writer('/">\n\t\t\t\t\t\t\t<paper-button raised class="edit_button">Edit</paper-button>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t\t<a class="button" href="/inventory/items.delete_w/')
            __M_writer(str( item.id ))
            __M_writer('/2">\n\t\t\t\t\t\t\t<paper-button raised class="delete_button">Delete</paper-button>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t</td>\n\t\t\t\t</tr>\n')
        __M_writer('\t\t</tbody>\n\t</table>\t\n')
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
        __M_writer('\n  View Items\n')
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


"""
__M_BEGIN_METADATA
{"filename": "/Users/John/DevProjects/Repositories/chef/inventory/templates/items.html", "uri": "items.html", "source_encoding": "ascii", "line_map": {"128": 157, "129": 159, "130": 161, "131": 163, "132": 165, "133": 167, "134": 173, "135": 175, "136": 199, "137": 200, "138": 205, "139": 205, "140": 208, "141": 208, "142": 211, "143": 211, "144": 214, "145": 214, "146": 217, "147": 217, "148": 220, "149": 220, "150": 226, "151": 229, "152": 231, "153": 235, "27": 0, "159": 11, "165": 11, "171": 15, "44": 7, "45": 9, "50": 13, "179": 16, "180": 16, "181": 17, "182": 17, "55": 19, "184": 18, "183": 18, "190": 184, "65": 24, "71": 24, "72": 28, "73": 32, "74": 34, "75": 38, "81": 21, "92": 21, "93": 24, "178": 15, "98": 40, "99": 42, "100": 44, "101": 47, "102": 50, "103": 65, "104": 68, "105": 70, "106": 73, "107": 91, "108": 94, "109": 97, "110": 99, "111": 101, "112": 103, "113": 105, "114": 107, "115": 113, "116": 115, "117": 133, "118": 134, "119": 139, "120": 139, "121": 142, "122": 142, "123": 145, "124": 145, "125": 148, "126": 148, "127": 154}}
__M_END_METADATA
"""
