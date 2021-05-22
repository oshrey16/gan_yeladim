# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import myInfo

admin.site.site_url = 'http://127.0.0.1:8000/parentsPage/bugReport/'
# Register your models here.
admin.site.register(myInfo)
