# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    brief = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name