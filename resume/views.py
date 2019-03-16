# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_resume(request):
    return render(request, 'resume.html')

def download_resuem(request):
    return HttpResponse("404")