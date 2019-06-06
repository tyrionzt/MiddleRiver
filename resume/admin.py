# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Message, Contact

# Register your models here.
class ContactInline(admin.TabularInline):
    model = Contact

class MessageAdmin(admin.ModelAdmin):
    inlines = [ContactInline]

admin.site.register(Message, MessageAdmin)
admin.site.register(Contact)