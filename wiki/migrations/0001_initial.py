# -*- coding: utf-8 -*-
# Generated by Django 1.9c1 on 2015-11-24 13:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Description')),
                ('source', models.URLField(verbose_name='Source')),
                ('related', models.CharField(blank=True, max_length=1024, verbose_name='Related')),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='Created')),
            ],
        ),
    ]
