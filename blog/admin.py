from django.contrib import admin
from .models import Entry, Category, Tag
from pagedown.widgets import AdminPagedownWidget
from django.db import models


class Blogadmin(admin.ModelAdmin):
    list_display = ('created', 'title', 'category')
    list_filter = ['created']
    search_fields = ['created']
    fieldsets = [
        (None,        {'fields': ['title', 'category', 'tags', 'image', 'attachment', 'content']}),
        ('Erweitert', {'fields': ['created', 'author'], 'classes': ['collapse']}),
    ]
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget}
    }
    ordering = ['-created']

    def save_model(self, request, obj, form, change):
        # Automatic set author if None is set
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


admin.site.register(Entry, Blogadmin)
admin.site.register(Category)
admin.site.register(Tag)
