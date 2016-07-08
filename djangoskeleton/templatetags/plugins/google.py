# -*- coding:utf-8 -*-
import json
import re
from django.template import Context, Template
from djangoskeleton.templatetags.skeleton_tags import register, skeleton

skeleton.set_head_script('https://maps.googleapis.com/maps/api/js?v=3.exp', **{'data-src': 'skeleton'})

# Google Map marks
@register.inclusion_tag('plugins/google_map.html', takes_context=True)
def google_map(context, object_list=[], html_id="map-canvas", center=None, zoom=12, 
        scrollwheel=False, draggable=True, animation=None, map_control=True,
        map_control_style="default", map_control_position="top_left", 
        zoom_control=True, zoom_position="left_top", streetview_control=True,
        streetview_position="left_top"):
    """
    Crea un mapa basado en la API de Google Maps con muy pocos argumentos de entrada.

    """

    # https://developers.google.com/maps/documentation/javascript/3.exp/reference#MapTypeControlStyle
    # https://developers.google.com/maps/documentation/javascript/3.exp/reference#ControlPosition
    google_maps_position_constants = {
            'bottom': 11,
            'bottom_center': 11,
            'bottom_left': 10,
            'bottom_right': 12,
            'center': 13,
            'left': 5,
            'left_bottom': 6,
            'left_center': 4,
            'left_top': 5,
            'right': 7,
            'right_bottom': 9,
            'right_center': 8,
            'right_top': 7,
            'top': 2,
            'top_center': 2,
            'top_left': 1,
            'top_right': 3
            }

    google_maps_style_constants = {
            'default': 0, 
            'horizontal_bar': 1, 
            'dropdown_menu': 2, 
            'inset': 3, 
            'inset_large': 4
            }

    map_args = {
        "zoom": zoom, 
        "scrollwheel": scrollwheel, 
        "draggable": draggable,
        "mapTypeControl": map_control,
        "mapTypeControlOptions": {
            "style": google_maps_style_constants[map_control_style],
            "position": google_maps_position_constants[map_control_position]
        },
        "zoomControl": zoom_control,
        "zoomControlOptions": {
            "position": google_maps_position_constants[zoom_position]
        },
        "streetViewControl": streetview_control,
        "streetViewControlOptions": {
            "position": google_maps_position_constants[streetview_position]
        }
    }


    if animation and animation.upper() in ["DROP", "BOUNCE"]:
        map_args.update(
                dict(
                    animation="google.maps.Animation.%s" % animation.upper()
                    )
                )
    
    if isinstance(center, basestring):
        center = re.split('\s*,\s*', center)

    if isinstance(center, (list, tuple)):
        center = "new google.maps.LatLng({0},{1})".format(*center) # center es una lista o tupla

    _object_list = []

    if isinstance(object_list, basestring):
        _object_list = [
                dict(
                    zip(
                        ('name', 'lat', 'lng'), re.split('\s*,\s*', obj)
                        )
                    ) for obj in re.split('\s*;\s*', object_list)] 

    else:

        for obj in object_list:

            _d = {}

            if not hasattr(obj, 'name'):
                _d['name'] = "%s" % obj
            else:
                _d['name'] = obj.get('name')

            if not hasattr(obj, 'gis') and hasattr(obj, 'lat') and hasattr(obj, 'lng'):
                _d['gis'] = {
                        'lat': obj['lat'],
                        'lng': obj['lng'],
                        }

            _object_list.append(_d)

    return {
        'request': context['request'],
        'map_options': json.dumps(map_args),
        'center_point': center,
        'html_id': html_id,
        'object_list': _object_list
    }
