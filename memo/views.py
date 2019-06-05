# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Memo
# Create your views here.

def index(request):
    memos = Memo.objects.all()
    return render(request, 'memo.html', {'memos': memos})
