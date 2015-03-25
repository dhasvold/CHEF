# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422408240.371713
_enable_loop = True
_template_filename = '/Users/John/DevProjects/chef/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['full_width_content']


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
        def full_width_content():
            return render_full_width_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'full_width_content'):
            context['self'].full_width_content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_full_width_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def full_width_content():
            return render_full_width_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\t<div class="full_width_image">\n\t\t<img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/colonial-shoes.jpg">\n\t</div>\n\n')
        __M_writer('\t<div class="wrapper">\n\t\t<p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo. Quisque sit amet est et sapien ullamcorper pharetra. Vestibulum erat wisi, condimentum sed, commodo vitae, ornare sit amet, wisi. Aenean fermentum, elit eget tincidunt condimentum, eros ipsum rutrum orci, sagittis tempus lacus enim ac dui. Donec non enim in turpis pulvinar facilisis. Ut felis. Praesent dapibus, neque id cursus faucibus, tortor neque egestas augue, eu vulputate magna eros eu erat. Aliquam erat volutpat. Nam dui mi, tincidunt quis, accumsan porttitor, facilisis luctus, metus</p>\n\n')
        __M_writer('\t\t<div class="spacer"></div>\n\t\t<div class="spacer"></div>\n\t\t<div class="spacer"></div>\n')
        __M_writer('\n')
        __M_writer('\t\t<div class="row">\n\n')
        __M_writer('\t\t\t<div class="col-md-4">\n\t\t\t\t<div class="center">\n\t\t\t\t\t<i class="fa fa-university fa-3x"></i><br>\n\t\t\t\t\t<p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo.</p>\n\t\t\t\t</div>\n\t\t\t</div>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<div class="col-md-4">\n\t\t\t\t<div class="center">\n\t\t\t\t\t<i class="fa fa-file-o fa-3x"></i><br>\n\t\t\t\t\t<p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo.</p>\n\t\t\t\t</div>\n\t\t\t</div>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<div class="col-md-4">\n\t\t\t\t<div class="center">\n\t\t\t\t\t<i class="fa fa-paper-plane-o fa-3x"></i><br>\n\t\t\t\t\t<p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo.</p>\n\t\t\t\t</div>\n\t\t\t</div>\n')
        __M_writer('\n\t\t</div>\n')
        __M_writer('\n\t\t</div>\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/John/DevProjects/chef/homepage/templates/index.html", "uri": "index.html", "line_map": {"64": 53, "65": 60, "66": 63, "35": 11, "36": 13, "73": 67, "46": 15, "27": 0, "67": 67, "53": 15, "54": 18, "55": 18, "56": 22, "57": 26, "58": 30, "59": 32, "60": 35, "61": 42, "62": 44, "63": 51}}
__M_END_METADATA
"""
