# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 09:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raster', '0034_legendentryorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rastertile',
            name='rast',
        ),
    ]
