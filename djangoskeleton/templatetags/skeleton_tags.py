# -*- coding:utf-8 -*-

from django.template import Context, Template
from django import template
from djangoskeleton.utils import dict_to_attribs
from djangoskeleton.core import skeleton
from djangoskeleton.backends.resolvers import link_resolver

import logging
log = logging.getLogger(__name__)

register = template.Library()

log.debug('carga de skeleton_tags')

skeleton.set_html_attributes({'data-app': 'skeleton_app'})
skeleton.set_style('https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/css/foundation.min.css', order=1)
skeleton.set_style('https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/css/normalize.min.css')

skeleton.set_scripts('https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/js/vendor/modernizr.js')
skeleton.set_scripts("https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/js/vendor/jquery.js")
skeleton.set_scripts("https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/js/foundation.min.js")
skeleton.set_scripts("https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/js/vendor/fastclick.js")
skeleton.set_scripts("https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/js/vendor/jquery.cookie.js")
skeleton.set_scripts("https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/js/vendor/placeholder.js")

# HTML
@register.simple_tag(takes_context=True)
def skeleton_get_html_attributes(context, default_attrs=""):
    return skeleton.get_html_attributes(context)

# HTML ATTRS
@register.simple_tag(takes_context=True)
def skeleton_set_html_attributes(context, **attrs):
    return skeleton.get_html_attributes(context, **attrs)

# META
@register.simple_tag(takes_context=True)
def skeleton_get_meta(context):
    return skeleton.get_meta(context)

# STYLE
@register.simple_tag(takes_context=True)
def skeleton_get_style(context):
    return skeleton.get_style(context)

# HEAD SCRIPT
@register.simple_tag(takes_context=True)
def skeleton_get_head_scripts(context):
    return skeleton.get_head_script(context)

# BODY ATTRS
@register.simple_tag(takes_context=True)
def skeleton_get_body_attributes(context):
    return skeleton.get_body_attributes(context)

# HEADER
@register.simple_tag(takes_context=True)
def skeleton_get_header(context):
    return skeleton.get_header(context)

# FOOTER
@register.simple_tag(takes_context=True)
def skeleton_get_footer(context):
    return skeleton.get_footer(context)

# SCRIPTS
@register.simple_tag(takes_context=True)
def skeleton_get_scripts(context):
    return skeleton.get_scripts(context)

@register.filter
def resolve_link(obj):
    """
    Busca entre los mecanismos para obtener links
    por defecto es get_absolute_url

    """
    return link_resolver(obj)

@register.filter
def make_split(obj, splitter=','):
    return obj.split(splitter)


@register.assignment_tag(name='generic_object_list', takes_context=True)
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
