# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import AreaInfo, PlayerInfo, ResourceInfo, CatalogInfo

# Register your models here.
class AreaInfoAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class CatalogInfoAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(AreaInfo, AreaInfoAdmin)
admin.site.register(PlayerInfo)
admin.site.register(ResourceInfo)
admin.site.register(CatalogInfo, CatalogInfoAdmin)