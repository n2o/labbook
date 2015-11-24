from django.contrib import admin
from .models import Item
from pagedown.widgets import AdminPagedownWidget
from django.db import models


class ItemAdmin(admin.ModelAdmin):
    list_display = ('created', 'title')
    list_filter = ['created']
    search_fields = ['created']
    fieldsets = [
        (None,        {'fields': ['title', 'content', 'source', 'related']}),
        ('Erweitert', {'fields': ['created'], 'classes': ['collapse']}),
    ]
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget}
    }


admin.site.register(Item, ItemAdmin)
