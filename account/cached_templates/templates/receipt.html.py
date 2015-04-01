# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427928170.8840232
_enable_loop = True
_template_filename = '/home/dhasvold/PycharmProjects/chef-master/account/templates/receipt.html'
_template_uri = 'receipt.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        items = context.get('items', UNDEFINED)
        quantity = context.get('quantity', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n<head lang="en">\n    <meta charset="UTF-8">\n    <title></title>\n</head>\n<body>\n\n    <h1>Thank you for your purchase, here is your receipt.</h1>\n\n\n    <table>\n        <thead>\n            <tr>\n                <th>\n                    Name\n                </th>\n                <th>\n                    Type\n                </th>\n                <th>\n                    Price\n                </th>\n            </tr>\n        </thead>\n        <tbody>\n            ')
        count = 0 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['count'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n')
        for item in items:
            __M_writer('                <tr>\n                    <td>\n                        ')
            __M_writer(str( item.specs.name ))
            __M_writer('\n                    </td>\n                    <td>\n                        ')
            __M_writer(str( quantity[count] ))
            __M_writer('\n                    </td>\n                    <td class="price">\n                        ')
            __M_writer(str( item.specs.price ))
            __M_writer('\n                        ')
            count += 1 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['count'] if __M_key in __M_locals_builtin_stored]))
            __M_writer('\n                    </td>\n                </tr>\n')
        __M_writer('            <tr>\n                <th>\n                    Total Price\n                </th>\n                <th>\n\n                </th>\n                <th>\n                    ')
        __M_writer(str( request.session['total'] ))
        __M_writer('\n                </th>\n            </tr>\n        </tbody>\n    </table>\n\n\n\n\n\n\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "receipt.html", "source_encoding": "ascii", "filename": "/home/dhasvold/PycharmProjects/chef-master/account/templates/receipt.html", "line_map": {"32": 31, "33": 31, "34": 34, "35": 34, "36": 37, "37": 37, "38": 38, "42": 38, "43": 42, "44": 50, "45": 50, "16": 0, "51": 45, "24": 1, "25": 27, "29": 27, "30": 28, "31": 29}}
__M_END_METADATA
"""
