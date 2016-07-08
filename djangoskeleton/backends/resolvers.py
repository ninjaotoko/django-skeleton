# -*- coding:utf-8 -*-

import re
from django.conf import settings
from django.utils.module_loading import import_string
import logging
log = logging.getLogger(__name__)

skeleton_link_resolvers = getattr(settings, 'SKELETON_LINK_RESOLVERS', 
        ['djangoskeleton.backends.resolvers.GenericLinkResolver'])


def link_resolver(obj):
    for module in skeleton_link_resolvers:
        module_class = import_string(module)

        link = module_class(obj)

        if link.resolve():
            return link.resolve()


class GenericLinkResolver(object):
    def __init__(self, obj, *args, **kwargs):
        self.obj = obj

    def resolve(self, *args, **kwargs):
        if hasattr(self.obj, 'get_absolute_url'):
            return seld.obj.get_absolute_url()

        url = re.search("(?P<url>https?://[^\s]+)", self.obj)

        if url:
            return url.group('url')

        return ''

