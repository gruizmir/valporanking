from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main.views.home', name='home'),
    url(r'^rank/', 'main.views.rank'),
    url(r'^best/', 'main.views.best'),
    url(r'^hipster/', 'main.views.worst'),
    url(r'^sendimage/', 'main.views.sendImage'),
    url(r'^voteimage/', 'main.views.voteImage'),
    url(r'^getimages', 'main.views.getImages'),
    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
