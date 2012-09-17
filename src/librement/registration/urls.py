from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('librement.registration.views',
    url(r'^register$', 'view',
        name='view'),
    url(r'^register/done$', 'done',
        name='done'),
    url(r'^register/confirm$', 'confirm',
        name='confirm'),
)
