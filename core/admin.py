from django.contrib import admin
from django.db import models
from django.contrib.flatpages.models import FlatPage
from pagedown.widgets import AdminPagedownWidget


class FlatpageAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget}
    }


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatpageAdmin)