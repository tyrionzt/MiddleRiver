# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    videos = ResourceInfo.objects.all()
    return render(request, 'movie/movie.html', {'videos': videos})

def play(request):
    name = request.GET.get('name')
    print name
    return render(request, 'movie/play.html', {'name': name})

