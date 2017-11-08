# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.generic import ListView, DetailView
from bookmark.models import Bookmark
# Create your views here.

class BookmarkLV(ListView):
    model = Bookmark

class BookmarkDV(DetailView):
    model = Bookmark
