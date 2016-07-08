# -*- coding:utf-8 -*-
from djangoskeleton.templatetags.skeleton_tags import register
from djangoskeleton.utils import dict_to_attribs
import json

# Orbit slider
# http://foundation.zurb.com/docs/components/orbit.html
@register.inclusion_tag('plugins/generic_slider.html', takes_context=True)
def orbit_slider(context, object_list=[], slider_id='slider', resolve_link=True, *args, **kwargs):

    slider_options = {
            "slide_number": False,
            "bullets": False,
            "animation": "slide",
            "navigation_arrows": True,
            "animation_speed": 250
            }

    #slider_options.update(kwargs)

    return {
            'request': context['request'],
            'slider_id': slider_id,
            'slider_options': dict_to_attribs(slider_options, join_by=';', separator=':', quote=False),
            'resolve_link': resolve_link,
            'object_list': object_list
            }
