# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import ListView , DetailView
from news.models import News

class NewsLV(ListView):
    model = News

class NewsDV(DetailView):
    model = News
# Create your views here.
