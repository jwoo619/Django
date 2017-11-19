# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-14 13:12
from __future__ import unicode_literals

from django.db import migrations
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=tagging.fields.TagField(blank=True, max_length=255),
        ),
    ]
