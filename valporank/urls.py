from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main.views.home', name='home'),
    url(r'^rank/', 'main.views.rank'),
    url(r'^best/', 'main.views.best'),
    url(r'^hipster/', 'main.views.worst'),
    url(r'^admin/', include(admin.site.urls)),
)
