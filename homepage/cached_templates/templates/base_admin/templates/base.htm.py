# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426620162.195426
_enable_loop = True
_template_filename = '/Users/John/DevProjects/Repositories/chef/base_admin/templates/base.htm'
_template_uri = '/base_admin/templates/base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['footer_links']


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
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer_links'):
            context['self'].footer_links(**pageargs)
        

        __M_writer('\n')
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
        __M_writer('  <div class="row">\n\n')
        __M_writer('    <div class="col-md-4">\n        <h3>Users</h3>\n        <ul>\n          <li><a href="/users/users.create/">Add User</a></li>\n          <li><a href="/users/users/">View Users</a></li>\n          <li><a href="/users/groups/">Groups</a></li>\n        </ul>\n    </div>\n')
        __M_writer('\n')
        __M_writer('    <div class="col-md-4">\n        <h3>Inventory</h3>\n        <ul>\n          <li><a href="/inventory/items.create/1">Add Non-Wardrobe Item</a></li>\n          <li><a href="/inventory/items.create/2">Add Wardrobe Item</a></li>\n          <li><a href="/inventory/items/">View Items</a></li>\n          <li><a href="/inventory/products.create/">Add Product</a></li>\n          <li><a href="/inventory/products/">View Products</a></li>\n        </ul>\n    </div>\n')
        __M_writer('\n')
        __M_writer('    <div class="col-md-4">\n        <h3>Events</h3>\n        <ul>\n          <li><a href="/events/events.create">Schedule Event</a></li>\n          <li><a href="/events/events/">View Events</a></li>\n          <li><a href="#">Event Templates</a></li>\n          <li><a href="/events/venues/">Venues</a></li>\n        </ul>\n    </div>\n')
        __M_writer('\n  </div>\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/John/DevProjects/Repositories/chef/base_admin/templates/base.htm", "uri": "/base_admin/templates/base.htm", "line_map": {"34": 8, "35": 10, "40": 56, "66": 60, "46": 13, "59": 52, "52": 13, "53": 15, "54": 18, "55": 27, "56": 29, "57": 40, "58": 42, "27": 0, "60": 55}, "source_encoding": "ascii"}
__M_END_METADATA
"""
