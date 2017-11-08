# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from news.models import News

# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','text')

admin.site.register(News, NewsAdmin)
