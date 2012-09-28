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

from .forms import RegistrationForm

def view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('registration:done')

    else:
        form = RegistrationForm()

    return render(request, 'registration/view.html', {
        'form': form,
    })

def done(request):
    return render(request, 'registration/done.html')

@login_required
def confirm(request):
    # Mark the user as active
    request.user.is_active = True
    request.user.save()

    return render(request, 'registration/confirm.html')
