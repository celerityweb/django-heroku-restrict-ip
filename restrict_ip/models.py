#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ipcalc
import logging

from django.db import models
from django.core.cache import cache
from django.db.models.signals import post_save, post_delete

logger = logging.getLogger(__name__)


class RestrictedIP(models.Model):
    network = models.CharField(max_length=18, help_text='IP or Network mask.')
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.network

    def get_network(self):
        return ipcalc.Network(self.network)

    class Meta:
        verbose_name = 'Restricted IP'
        verbose_name_plural = 'Restricted IPs'


def _build_cache(sender, instance, **kwargs):
    """Build a list of banned IPs / subnets and store it in the cache."""
    restricted_ips = [i.get_network() for i in RestrictedIP.objects.all()]
    # this is cleared on save/delete so we can store it indefinitely
    cache.set('restrictedip:list', restricted_ips, timeout=None)
    logger.info('Cleared restricted IP list.')


post_save.connect(_build_cache, sender=RestrictedIP)
post_delete.connect(_build_cache, sender=RestrictedIP)
