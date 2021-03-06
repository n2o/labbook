# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2015-11-16 09:42
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('intro', models.TextField(blank=True, null=True, verbose_name='Kurzbeschreibung')),
            ],
            options={
                'verbose_name': 'Kategorie',
                'verbose_name_plural': 'Kategorien',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, verbose_name='Titel')),
                ('content', models.TextField(verbose_name='Inhalt')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Bild')),
                ('attachment', models.FileField(blank=True, null=True, upload_to='', verbose_name='Anhang')),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='Erstellt am')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='Kategorie')),
            ],
            options={
                'verbose_name': 'Eintrag',
                'ordering': ('created',),
                'verbose_name_plural': 'Einträge',
            },
        ),
    ]
