from django.conf.urls import patterns, url

urlpatterns = patterns('librement.profile.emails.views',
    url(r'^profile/edit/emails$', 'view',
        name='view'),
    url(r'^profile/edit/emails/confirm$', 'confirm',
        name='confirm'),
    url(r'^profile/edit/emails/add$', 'add',
        name='add'),
    url(r'^profile/edit/emails/(?P<email_id>\d+)/delete$', 'delete',
        name='delete'),
)
