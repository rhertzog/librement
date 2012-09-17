from django.conf.urls import patterns, url

urlpatterns = patterns('librement.passwords.views',
    url(r'^forgot-password$', 'forgot_password',
        name='forgot-password'),
    url(r'^forgot-password/done$', 'forgot_password_done',
        name='forgot-password-done'),

    url(r'^reset-password$', 'reset_password',
        name='reset-password'),
    url(r'^reset-password/done$', 'reset_password_done',
        name='reset-password-done'),
)
