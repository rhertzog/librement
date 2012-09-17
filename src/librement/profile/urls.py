from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('librement.profile.views',
    url(r'^people/(?P<username>[^/]+)$', 'view',
        name='view'),
)
