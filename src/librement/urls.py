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

from django.contrib import admin

from django.conf.urls.defaults import patterns, include

urlpatterns = patterns('',
    (r'', include('librement.account.urls', namespace='account')),
    (r'', include('librement.dashboard.urls', namespace='dashboard')),
    (r'', include('librement.profile.urls', namespace='profile')),
    (r'', include('librement.registration.urls', namespace='registration')),
    (r'', include('librement.passwords.urls', namespace='passwords')),
    (r'', include('librement.profile.urls', namespace='profile')),
    (r'', include('librement.static.urls', namespace='static')),

    (r'', include('librement.debug.urls')),
    (r'^admin/', include(admin.site.urls)),
)
