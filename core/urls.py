from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.contrib.flatpages import views as flatpageviews

# Include these two lines to use the core/admin.py file
admin.autodiscover()
import core.admin       # <-- this line is actually necessary

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('login.urls', namespace='login')),

    # Own Apps
    url(r'^blog/', include('blog.urls', namespace='blog')),

    # Flatpages
    url(r'^paper/general-idea/$', flatpageviews.flatpage, {'url': '/paper/general-idea/'}, name='general-idea'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
