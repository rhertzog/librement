from django.conf.urls.defaults import patterns, include

urlpatterns = patterns('',
    (r'', include('librement.static.urls', namespace='static')),

    (r'', include('librement.debug.urls')),
)
