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

from django.conf import settings
from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout

from .forms import LoginForm

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = form.cleaned_data['user']
            user.backend = settings.AUTHENTICATION_BACKENDS[0]
            auth.login(request, user)

            return redirect('dashboard:view')

    else:
        form = LoginForm()

    return render(request, 'account/login.html', {
        'form': form,
    })

def logout(request):
    django_logout(request)

    return redirect('dashboard:view')
