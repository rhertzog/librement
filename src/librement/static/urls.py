from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('librement.static.views',
    url(r'^$', 'landing',
        name='landing'),
)
