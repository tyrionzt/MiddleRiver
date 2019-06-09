# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from .models import Item, Photo
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'gallery/gallery.html'
    def get_queryset(self):
        return Item.objects.all()[:5]

class ListView(generic.ListView):
    model = Item
    template_name = 'gallery/gallery_item_list.html'

class ItemDetailView(generic.DetailView):
    model = Item
    template_name = 'gallery/gallery_item_detail.html'

class PhotoDetailView(generic.DetailView):
    model = Photo
    template_name = 'gallery/gallery_photo_detail.html'