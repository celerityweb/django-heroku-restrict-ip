#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import RestrictedIP

admin.site.register(RestrictedIP)
