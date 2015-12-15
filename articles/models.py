from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from autoslug import AutoSlugField


class Article(models.Model):
    title = models.CharField('Title', max_length=50, blank=True)
    slug = AutoSlugField(null=True, populate_from='title')
    author = models.ForeignKey(User, null=True, blank=True, verbose_name="Author")
    content = models.TextField('Content', blank=False)
    created = models.DateTimeField('Created', default=datetime.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField('Name', max_length=50, default="Anonym", blank=True)
    comment = models.TextField('Comment', max_length=1024, blank=False)
    created = models.DateTimeField('Created', default=datetime.now)
    article = models.ForeignKey(Article)

    def __str__(self):
        return self.comment