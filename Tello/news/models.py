# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField()
    
