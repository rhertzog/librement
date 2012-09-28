# Copyright 2012 The Librement Developers
#
# See the AUTHORS file at the top-level directory of this distribution
# and at http://librement.net/copyright/
#
# This file is part of Librement. It is subject to the license terms in
# the LICENSE file found in the top-level directory of this distribution
# and at http://librement.net/license/. No part of Librement, including
# this file, may be copied, modified, propagated, or distributed except
# according to the terms contained in the LICENSE file.

from django.conf.urls.defaults import patterns, url, include

from django.conf import settings

urlpatterns = patterns('librement.debug.views',
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        url(r'^media/(?P<path>.*)$', 'serve',
            {'document_root': settings.STATIC_MEDIA_ROOT}),
        url(r'^storage/(?P<path>.*)$', 'serve',
            {'document_root': settings.MEDIA_ROOT}),
        url(r'^(?P<path>favicon\.ico|robots\.txt)$', 'serve',
            {'document_root': settings.STATIC_MEDIA_ROOT}),
    )

    urlpatterns += patterns('librement.debug.views',
        url(r'^(?P<code>404|500)$', 'error'),
    )

    urlpatterns += patterns('',
        url(r'', include('debug_toolbar_user_panel.urls')),
    )
