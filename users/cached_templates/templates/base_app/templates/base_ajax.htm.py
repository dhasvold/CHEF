# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425520528.548539
_enable_loop = True
_template_filename = '/Users/John/DevProjects/Repositories/chef/base_app/templates/base_ajax.htm'
_template_uri = '/base_app/templates/base_ajax.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['extra_links', 'paper_elements_import', 'content']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def extra_links():
            return render_extra_links(context._locals(__M_locals))
        def paper_elements_import():
            return render_paper_elements_import(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_links'):
            context['self'].extra_links(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'paper_elements_import'):
            context['self'].paper_elements_import(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('  \n\n')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_links():
            return render_extra_links(context)
        __M_writer = context.writer()
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_paper_elements_import(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def paper_elements_import():
            return render_paper_elements_import(context)
        __M_writer = context.writer()
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n  Sub-templates should place their ajax content here.\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"32": 6, "33": 7, "98": 92, "68": 13, "37": 7, "38": 10, "39": 10, "80": 18, "92": 23, "74": 18, "44": 15, "16": 6, "49": 20, "18": 0, "54": 25, "55": 28, "56": 28, "86": 23, "62": 13, "31": 4}, "filename": "/Users/John/DevProjects/Repositories/chef/base_app/templates/base_ajax.htm", "uri": "/base_app/templates/base_ajax.htm", "source_encoding": "ascii"}
__M_END_METADATA
"""
