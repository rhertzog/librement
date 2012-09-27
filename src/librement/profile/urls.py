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

urlpatterns = patterns('librement.profile.views',
    (r'', include('librement.profile.links.urls', namespace='links')),
    (r'', include('librement.profile.emails.urls', namespace='emails')),

    url(r'^people/(?P<username>[^/]*)$', 'view',
        name='view'),
    url(r'^people/(?P<username>[^/]*)/rss$', 'xhr_rss',
        name='xhr-rss'),
    url(r'^profile/edit$', 'edit',
        name='edit'),
    url(r'^profile/edit/url$', 'edit_url',
        name='edit-url'),
    url(r'^profile/edit/picture$', 'edit_picture',
        name='edit-picture'),
)
