# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import permalink
from mysite.fields import ThumbnailImageField
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible # 解决django后台不能写入中文到数据库的问题
class Item(models.Model):
    name = models.CharField(max_length=249)
    desc = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return ('item_detail', None, {'pk': self.id})

@python_2_unicode_compatible
class Photo(models.Model):
    item = models.ForeignKey(Item)
    title = models.CharField(max_length=100)
    image = ThumbnailImageField(upload_to='photos')
    caption = models.CharField(max_length=249, blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('photo_detail', None, {'pk': self.id})
