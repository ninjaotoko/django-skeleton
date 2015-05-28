# -*- coding:utf-8 -*-

from django.template import Context, Template
from django import template
register = template.Library()

def dict_to_attribs(options):
    """
    Transforma un `dict` en atributos del estilo key="val" y devuelve un string
    """

    return " ".join([
        "%s=\"%s\"" % (key, val) 
        for key, val in options.iteritems()
        ])

def skeleton_get_html_attributes(context):
    pass

def skeleton_get_meta(context):
    pass

def skeleton_get_style(context):
    pass

def skeleton_get_head_scripts(context):
    pass

def skeleton_get_body_attributes(context):
    pass

def skeleton_get_header(context):
    pass

def skeleton_get_footer(context):
    pass

def skeleton_get_scripts(context):
    pass


def render_as_list(context, object_list, tag_wrapper='ul', \
        tag_wrapper_attribs='class="no-bullet"', tag_wrapper_element='li', \
        tag_wrapper_element_attribs='', tag_element='', tag_element_attribs='', \
        object_field=''):

    if isinstance(tag_wrapper_attribs, dict):
        tag_wrapper_attribs = dict_to_attribs(tag_wrapper_attribs)

    if isinstance(tag_wrapper_attribs, dict):
        tag_wrapper_element_attribs = dict_to_attribs(tag_wrapper_element_attribs)

    if isinstance(tag_element_attribs, dict):
        tag_element_attribs = dict_to_attribs(tag_element_attribs)

    object_tag = 'object'
    
    if object_field:
        object_tag = 'object.%s' % object_field

    if tag_element:
        element = "<%(tag)s %(attribs)s>{{ %(object_tag) }}</%(tag)s>" % {
                'tag':tag_element, 
                'attribs': tag_element_attribs,
                'object_tag': object_tag
            }
    else:
        element = "{{ %s }}" % object_tag

    args = {
        'tag_wrapper': tag_wrapper,
        'tag_wrapper_attribs': tag_wrapper_attribs,
        'tag_wrapper_element': tag_wrapper_element,
        'tag_wrapper_element_attribs': tag_wrapper_element_attribs,
        'element': element
    }

    template = Template("""
        <%(tag_wrapper)s %(tag_wrapper_attribs)s>
        {%% for object in object_list %%}
            <%(tag_wrapper_element)s %(tag_wrapper_element_attribs)s>
                %(element)s
            </%(tag_wrapper_element)s>
        {%% endfor %%}
        </%(tag_wrapper)s>
        """ % args)

    context = Context(dict(object_list=object_list))

    return template.render(context)

register.assignment_tag(render_as_list, name='generic_object_list', takes_context=True)
