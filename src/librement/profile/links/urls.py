from django.conf.urls import patterns, url

urlpatterns = patterns('librement.profile.links.views',
    url(r'^profile/edit/links$', 'view',
        name='view'),
    url(r'^profile/edit/links/add$', 'add_edit',
        name='add'),
    url(r'^profile/edit/links/(?P<link_id>\d+)$', 'add_edit',
        name='edit'),
    url(r'^profile/edit/links/(?P<link_id>\d+)/delete$', 'delete',
        name='delete'),
)
