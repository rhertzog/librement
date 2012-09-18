from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('librement.profile.views',
    url(r'^people/(?P<username>[^/]+)$', 'view',
        name='view'),
    url(r'^profile/edit$', 'edit',
        name='edit'),
    url(r'^profile/edit/url$', 'edit_url',
        name='edit-url'),
)
