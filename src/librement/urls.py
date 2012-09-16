from django.contrib import admin

from django.conf.urls.defaults import patterns, include

urlpatterns = patterns('',
    (r'', include('librement.profile.urls', namespace='profile')),
    (r'', include('librement.registration.urls', namespace='registration')),
    (r'', include('librement.static.urls', namespace='static')),

    (r'', include('librement.debug.urls')),
    (r'^admin/', include(admin.site.urls)),
)
