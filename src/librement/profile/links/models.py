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

from django.db import models

class Link(models.Model):
    user = models.ForeignKey('auth.User', related_name='links')

    url = models.URLField()
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return u"%s <%s>" % (self.title, self.url)
