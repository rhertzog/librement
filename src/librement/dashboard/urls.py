from django.conf.urls import patterns, url

urlpatterns = patterns('librement.dashboard.views',
    url(r'^$', 'view',
        name='view'),
)
