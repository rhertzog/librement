from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('librement.profile.views',
    (r'', include('librement.profile.links.urls', namespace='links')),

    url(r'^people/(?P<username>[^/]*)$', 'view',
        name='view'),
    url(r'^profile/edit$', 'edit',
        name='edit'),
    url(r'^profile/edit/url$', 'edit_url',
        name='edit-url'),
    url(r'^profile/edit/picture$', 'edit_picture',
        name='edit-picture'),
)
