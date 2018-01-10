#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponseForbidden
from django.core.cache import cache

from ipware.ip import get_ip


class RestrictedIPMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # need to look at X_FORWARDED_FOR to get real IP on heroku
        ip = get_ip(request)

        if ip is not None:
            # get list of restricted IPs from the cache
            restricted_ips = cache.get('restrictedip:list')

            # if list exists, compare request IP to list of restricted IPs
            if restricted_ips:
                for network in restricted_ips:
                    if ip in network:
                        # IP found in the restricted list -- return 403
                        return HttpResponseForbidden()

        return self.get_response(request)
