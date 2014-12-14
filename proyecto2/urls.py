from django.conf.urls import patterns, include, url

from django.contrib import admin
from app.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyecto2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^desarrollo/$','app.views.desarrollo',name='desarrollo'),
    url(r'^categoria/(\d+)$','app.views.categoria',name='categoria'),
    url(r'^blog/$','app.views.blog',name='blog'),
    url(r'^estrategia/$','app.views.estrategia',name='estrategia'),
    url(r'^$','app.views.home',name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
