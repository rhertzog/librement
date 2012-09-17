from django.conf.urls import patterns, url

urlpatterns = patterns('librement.account.views',
    url(r'^login$', 'login',
        name='login'),
    url(r'^logout$', 'logout',
        name='logout'),
)
