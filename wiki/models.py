from datetime import datetime
from django.db import models


class Item(models.Model):
    title = models.CharField("Title", max_length=50, blank=False)
    content = models.TextField("Description", blank=False)
    source = models.URLField("Source", blank=True)
    related = models.ManyToManyField("self", blank=True)
    created = models.DateTimeField('Created', default=datetime.now)

    def __str__(self):
        return self.title