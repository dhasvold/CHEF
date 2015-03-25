# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423355102.45459
_enable_loop = True
_template_filename = '/Users/John/DevProjects/Repositories/chef/base_admin/templates/base.htm'
_template_uri = '/base_admin/templates/base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['navbar_links', 'footer_links']


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
        def navbar_links():
            return render_navbar_links(context._locals(__M_locals))
        def footer_links():
            return render_footer_links(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_links'):
            context['self'].navbar_links(**pageargs)
        

        __M_writer('\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer_links'):
            context['self'].footer_links(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def navbar_links():
            return render_navbar_links(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <ul class="nav navbar-nav navbar-right">\n      <li><a href="/homepage/index/">Home</a></li>\n      <li class="dropdown">\n        <a class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false" href="#">Users</a>\n        <ul class="dropdown-menu dropdown-menu-left" role="menu">\n          <li><a href="/users/users.create">Add User</a></li>\n          <li><a href="/users/users/">View Users</a></li>\n          <li class="divider"></li>\n          <li><a href="/users/groups/">Groups</a></li>\n        </ul>\n      </li>\n      <li class="dropdown">\n        <a class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false" href="#">Inventory</a>\n        <ul class="dropdown-menu dropdown-menu-left" role="menu">\n          <li><a href="/inventory/items.create/1">Add Non-Wardrobe Item</a></li>\n          <li><a href="/inventory/items.create/2">Add Wardrobe Item</a></li>\n          <li><a href="/inventory/items/">View Items</a></li>\n          <li class="divider"></li>\n          <li><a href="/inventory/products/">Products</a></li>\n        </ul>\n      </li>\n      <li class="dropdown">\n        <a class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false" href="#">Events</a>\n        <ul class="dropdown-menu dropdown-menu-left" role="menu">\n          <li><a href="/events/events.create">Schedule Event</a></li>\n          <li><a href="/events/events/">View Events</a></li>\n          <li class="divider"></li>\n          <li><a href="#">Event Templates</a></li>\n          <li class="divider"></li>\n          <li><a href="/events/venues/">Venues</a></li>\n        </ul>\n      </li>\n')
        if request.user.username == '':
            __M_writer('        <li><a href="/homepage/login/">Login</a></li>\n')
        else:
            __M_writer('        <li class="dropdown">\n          <a class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false" href="#">')
            __M_writer(str( request.user.first_name ))
            __M_writer('</a>\n          <ul class="dropdown-menu dropdown-menu-left" role="menu">\n            <li><a href="/homepage/login.logout_user">Log Out</a></li>\n          </ul>\n')
        __M_writer('    </ul>\n')
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
{"filename": "/Users/John/DevProjects/Repositories/chef/base_admin/templates/base.htm", "source_encoding": "ascii", "uri": "/base_admin/templates/base.htm", "line_map": {"64": 47, "65": 48, "66": 49, "67": 50, "68": 50, "69": 55, "75": 60, "81": 60, "82": 62, "83": 65, "84": 74, "85": 76, "86": 87, "87": 89, "88": 99, "89": 102, "27": 0, "95": 89, "37": 8, "38": 10, "43": 56, "44": 58, "49": 103, "55": 13, "62": 13, "63": 46}}
__M_END_METADATA
"""
