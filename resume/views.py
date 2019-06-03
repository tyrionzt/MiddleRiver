# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.core.paginator import Paginator

from .models import Message, Contact
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, FileResponse, HttpResponseRedirect

# Create your views here.
def my_resume(request):
    # 从数据库中取数据
    all_message = Message.objects.all().order_by('-date')
    try:
        page = request.GET.get('page', 1)
    except:
        page = 1
    p = Paginator(all_message, 10)
    message = p.page(page)
    return render(request, 'resume.html', {'all_message': message})

def download_resuem(request):
    file = open(settings.BASE_DIR + '/resume.docx', 'rb')
    # return HttpResponse("it's ok")
    response = FileResponse(file)
    response['Content-Type'] = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    response['Content-Disposition'] = 'attachment;filename="resume.docx"'
    return response

def save_message(request):
    name = request.POST.get('Full Name')
    wechat = request.POST.get('Wechat')
    qq = request.POST.get('QQ')
    email = request.POST.get('Email')
    phone_num = request.POST.get('Phone Num')
    message = request.POST.get('Message')

    #保存留言到数据库
    lmessage = Message()
    lmessage.name = name
    lmessage.contents = message
    lmessage.save()

    lcontact = Contact()
    lcontact.wechat = wechat
    lcontact.qq = qq
    lcontact.email = email
    lcontact.phone = phone_num
    lcontact.belong = lmessage
    lcontact.save()

    return HttpResponseRedirect('/resume/')

# def show_message(request):
#     #从数据库中取数据
#     all_message = Message().objects.all().order_by('-AddTime')
#     try:
#         page = request.GET.get('page', 1)
#     except :
#         page = 1
#     p = Paginator(all_message, 3, request=request)
#     message = p.page(page)
#     return render(request, 'resume.html', {'all message': message})



