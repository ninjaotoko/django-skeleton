# -*- coding:utf-8 -*-
from djangoskeleton.templatetags.skeleton_tags import register
from djangoskeleton.utils import dict_to_attribs

# Tabs
# http://foundation.zurb.com/sites/docs/v/5.5.3/components/tabs.html#tabs-deeplink-3
@register.inclusion_tag('plugins/generic_tabs.html', takes_context=True)
def generic_tabs(context, object_list=[], tab_id='tab', title_key='title', 
        content_key='content', *args, **kwargs):
    """
    Crea un componente <Tabs> con el QuerySet en object_list

    El `title` pasa a ser el título del tab, y el `content` es el contenido
    """

    _object_list = []

    for obj in object_list:
        title = getattr(obj, title_key)
        content = getattr(obj, content_key)

        if callable(title):
            title = title()

        if callable(content):
            content = content()

        _object_list.append({'title': title, 'content': content})

    return {
            'request': context['request'],
            'tab_id': tab_id,
            'tab_attrs': dict_to_attribs(kwargs),
            'object_list': _object_list
            }

# Accordion
# http://foundation.zurb.com/sites/docs/v/5.5.3/components/accordion.html
