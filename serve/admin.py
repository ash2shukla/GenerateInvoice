# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import database

class databaseAdmin(admin.ModelAdmin):
  list_display = ['invoice_no']

admin.site.register(database,databaseAdmin)
