from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.flatpages import views as flatpageviews
from blog import views as blogviews


# Include these two lines to use the core/admin.py file
admin.autodiscover()
import core.admin       # <-- this line *is* necessary

urlpatterns = [
    url(r'^$', blogviews.overview, name='index'),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('login.urls', namespace='account')),

    # Own Apps
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^wiki/', include('wiki.urls', namespace='wiki')),
    url(r'^articles/', include('articles.urls', namespace='articles')),

    # Flatpages
    url(r'^papers/general-idea/$', flatpageviews.flatpage, {'url': '/papers/general-idea/'}, name='general-idea'),
    url(r'^ideas/integration-in-websites/$', flatpageviews.flatpage, {'url': '/ideas/integration-in-websites/'}, name='integration-in-websites'),
    url(r'^dev/dwarfjs/$', flatpageviews.flatpage, {'url': '/dev/discuss/'}, name='discuss'),
    url(r'^dev/ff-extension/$', flatpageviews.flatpage, {'url': '/dev/ff-extension/'}, name='ff-extension'),
    url(r'^definitions/$', flatpageviews.flatpage, {'url': '/definitions/'}, name='definitions'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
