# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-15 09:18
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20151215_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='title'),
        ),
    ]
