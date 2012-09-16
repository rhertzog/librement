from django.conf.urls.defaults import patterns, url, include

from django.conf import settings

urlpatterns = patterns('librement.debug.views',
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        url(r'^media/(?P<path>.*)$', 'serve',
            {'document_root': settings.STATIC_MEDIA_ROOT}),
        (r'^(?P<path>favicon\.ico|robots\.txt)$', 'serve',
            {'document_root': settings.STATIC_MEDIA_ROOT}),
    )

    urlpatterns += patterns('librement.debug.views',
        url(r'^(?P<code>404|500)$', 'error'),
    )
