# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=20)
    contents = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "%s" % self.name

class Contact(models.Model):
    wechat = models.CharField(max_length=20)
    qq = models.BigIntegerField()
    email = models.EmailField()
    phone = models.BigIntegerField()
    belong = models.ForeignKey("Message")
