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

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import ForgotPasswordForm, ResetPasswordForm

def forgot_password(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('passwords:forgot-password-done')

    else:
        form = ForgotPasswordForm()

    return render(request, 'passwords/forgot_password.html', {
        'form': form,
    })

def forgot_password_done(request):
    return render(request, 'passwords/forgot_password_done.html')

@login_required
def reset_password(request):
    if request.method == 'POST':
        form = ResetPasswordForm(request.user, request.POST)

        if form.is_valid():
            form.save()

            return redirect('passwords:reset-password-done')

        print form.errors

    else:
        form = ResetPasswordForm(request.user)

    return render(request, 'passwords/reset_password.html', {
        'form': form,
    })

@login_required
def reset_password_done(request):
    return render(request, 'passwords/reset_password_done.html')
