from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main.views.home', name='home'),
    url(r'^rank/', 'main.views.rank'),
    url(r'^admin/', include(admin.site.urls)),
)
