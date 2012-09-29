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

from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from .forms import EmailForm, ConfirmForm

@login_required
def view(request):
    return render(request, 'profile/emails/view.html')

@login_required
def confirm(request):
    form = ConfirmForm(request.user, request.GET)

    if form.is_valid():
        form.save()

        messages.success(
            request,
            "Your email adddress was successfully confirmed.",
        )
    else:
        messages.error(
            request,
            "There was an error confirming your email address.",
        )

    return redirect('profile:emails:view')

@login_required
def add(request):
    if request.method == 'POST':
        form = EmailForm(request.user, request.POST)

        if form.is_valid():
            form.send_email()

            messages.success(
                request,
                "Please check your email inbox to confirm your email address.",
            )

            return redirect('profile:emails:view')

    else:
        form = EmailForm(request.user)

    return render(request, 'profile/emails/add.html', {
        'form': form,
    })

@require_POST
@login_required
def delete(request, email_id):
    email = get_object_or_404(request.user.emails, pk=email_id)

    if request.user.emails.count() > 1:
        email.delete()
        messages.success(request, "Email address deleted.")
    else:
        messages.error(request, "Cannot delete last remaining email address.")

    return redirect('profile:emails:view')
