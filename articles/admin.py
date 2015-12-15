from django.contrib import admin
from pagedown.widgets import AdminPagedownWidget
from django.db import models
from .models import Article, Comment


class CommentAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget}
    }


class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget}
    }

    def save_model(self, request, obj, form, change):
        # Automatic set author if None is set
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)