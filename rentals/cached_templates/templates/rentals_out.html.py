# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428084731.171552
_enable_loop = True
_template_filename = '/home/dhasvold/PycharmProjects/chef-master/rentals/templates/rentals_out.html'
_template_uri = 'rentals_out.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'tab_title', 'page_title']


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
    return runtime._inherit_from(context, '/base_admin/templates/View.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        rentalItems = context.get('rentalItems', UNDEFINED)
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'tab_title'):
            context['self'].tab_title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        rentalItems = context.get('rentalItems', UNDEFINED)
        def page_title():
            return render_page_title(context)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\t\n')
        __M_writer('\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\n')
        __M_writer('\n    <div class="item_box">\n\n')
        if len(rentalItems) == 0:
            __M_writer('                <p>You have no active rentals at this time.</p>\n')
        else:
            __M_writer('            <table class="table table-hover table-bordered">\n                <thead>\n                    <tr>\n                        <th>\n                            Name\n                        </th>\n                        <th>\n                            Date Out\n                        </th>\n                        <th>\n                            Due Date\n                        </th>\n                        <th>\n                            Actions\n                        </th>\n                    </tr>\n                </thead>\n                <tbody>\n')
            for li in rentalItems:
                __M_writer('                        <tr>\n                            <td>\n                                 ')
                __M_writer(str( li ))
                __M_writer('\n                            </td>\n                            <td>\n                               ')
                __M_writer(str( li.date_out.strftime('%m/%d/%Y') ))
                __M_writer('\n                            </td>\n                            <td>\n                                ')
                __M_writer(str( li.due_date.strftime('%m/%d/%Y')  ))
                __M_writer('\n                            </td>\n                            <td>\n                                <a class="button" href="/rentals/rentals.return_item/')
                __M_writer(str( li.item.id ))
                __M_writer('/')
                __M_writer(str( li.id ))
                __M_writer('">\n                                    <paper-button raised class="success_button">Return</paper-button>\n                                </a>\n                            </td>\n                        </tr>\n')
            __M_writer('                </tbody>\n                </table>\n')
        __M_writer('\t\t</div>\n\n\n\n')
        __M_writer('\t<div class="clearfix"></div>\n')
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
        __M_writer('\n  \tRental Return\n')
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
        __M_writer('\t\t\t<div class="col-md-8">\n\t\t\t\t<h1>Current Rentals</h1>\n\t\t\t</div>\n')
        __M_writer('\n\n\t\t</div>\n\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/dhasvold/PycharmProjects/chef-master/rentals/templates/rentals_out.html", "uri": "rentals_out.html", "source_encoding": "ascii", "line_map": {"66": 15, "67": 18, "72": 29, "73": 31, "74": 34, "75": 35, "76": 36, "77": 38, "78": 56, "79": 57, "80": 59, "81": 59, "82": 62, "83": 62, "84": 65, "85": 65, "86": 68, "87": 68, "88": 68, "89": 68, "90": 74, "27": 0, "92": 82, "93": 84, "94": 86, "95": 90, "91": 77, "101": 11, "40": 7, "41": 9, "107": 11, "46": 13, "113": 18, "119": 18, "56": 15, "121": 26, "120": 22, "127": 121}}
__M_END_METADATA
"""
