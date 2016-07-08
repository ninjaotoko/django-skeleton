# -*- coding:utf-8 -*-

from django.template import Context, Template

def dict_to_attribs(options, join_by=" ", separator='=', quote=True):
    """
    Transforma un `dict` en atributos del estilo key="val" y devuelve un string
    """

    tpl = "{key}{separator}"

    if quote:
        tpl += "'{val}'"
    else:
        tpl += "{val}"

    def _val(val):
        if type(val) == bool:
            return 'true' if val else 'false'
        return val

    return join_by.join([
        tpl.format(key=key, val=_val(val), separator=separator) 
        for key, val in options.iteritems()
        ])
