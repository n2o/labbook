from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.overview, name='overview'),
    url(r'^(?P<year>[0-9]+)/$', views.year, name='year'),
    url(r'^(?P<year>[0-9]+)/(?P<month>[0-9]+)$', views.month, name='month'),
    url(r'^(?P<year>[0-9]+)/(?P<month>[0-9]+)/(?P<day>[0-9]+)$', views.day, name='day'),
]