from datetime import datetime
from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField('Name', max_length=50, blank=False)
    intro = models.TextField('Kurzbeschreibung', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Tag(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Entry(models.Model):
    title = models.CharField('Title', max_length=1024, blank=True)
    author = models.ForeignKey(User, null=True, blank=True, verbose_name="Author")
    content = models.TextField('Content', blank=False)
    image = models.ImageField('Image', null=True, blank=True)
    attachment = models.FileField('Attachment', null=True, blank=True)
    created = models.DateTimeField('Created', default=datetime.now)
    category = models.ForeignKey('Category', null=True, verbose_name="Category")
    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'
        ordering = ('created',)



