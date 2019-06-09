# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Book
# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request, "book/book.html", {'books': books})
