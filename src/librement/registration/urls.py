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

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('librement.registration.views',
    url(r'^register$', 'view',
        name='view'),
    url(r'^register/done$', 'done',
        name='done'),
    url(r'^register/confirm$', 'confirm',
        name='confirm'),
)
