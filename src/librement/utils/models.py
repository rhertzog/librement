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

from django.template import add_to_builtins

add_to_builtins('django_autologin.templatetags.django_autologin')
add_to_builtins('librement.utils.templatetags.media')
add_to_builtins('librement.utils.templatetags.switch')
