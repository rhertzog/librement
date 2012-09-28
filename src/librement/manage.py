#!/usr/bin/env python

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

import os
import sys

from os.path import join, dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
sys.path.insert(0, join(dirname(dirname(abspath(__file__))), 'contrib'))

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'librement.settings')

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
