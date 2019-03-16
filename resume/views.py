# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import StreamingHttpResponse

# Create your views here.
def my_resume(request):
    return render(request, 'resume.html')

def download_resuem(request):
    file = open('/home/amarsoft/download/example.tar.gz', 'rb')
    response = HttpResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="简历.zip"'
    return response