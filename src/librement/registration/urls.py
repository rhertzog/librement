from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('librement.registration.views',
    url(r'^register$', 'view',
        name='view'),
)
