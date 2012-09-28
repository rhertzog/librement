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

import time
import functools

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
from django.utils import simplejson

class ajax(object):
    def __init__(self, required=True):
        self.required = required

    def allow_request(self, request):
        if not self.required:
            return True

        if request.user.is_superuser:
            return True

        if request.META.get('SERVER_NAME') == 'testserver':
            return True

        if request.is_ajax():
            return True

        return False

    def __call__(self, fn):
        @functools.wraps(fn)
        def wrapped(request, *args, **kwargs):
            if not self.allow_request(request):
                return HttpResponseBadRequest()

            time.sleep(settings.XHR_SIMULATED_DELAY)

            response = fn(request, *args, **kwargs) or {}

            if isinstance(response, dict):
                return HttpResponse(
                    simplejson.dumps(response),
                    mimetype='text/html' if request.FILES else 'application/json',
                )

            return response
        return wrapped
