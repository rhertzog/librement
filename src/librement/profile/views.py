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
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from librement.utils.ajax import ajax

from .forms import ProfileForm, URLForm, PictureForm, PasswordForm
from .utils import get_rss_feed

def view(request, username):
    user = get_object_or_404(User, username=username)

    return render(request, 'profile/view.html', {
        'user': user,
    })

@ajax()
def xhr_rss(request, username):
    user = get_object_or_404(User, username=username)

    return render(request, 'profile/rss.html', {
        'feed': get_rss_feed(user.profile.rss_url),
    })

@login_required
def edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)

        if form.is_valid():
            form.save()

            messages.success(request, "Profile updated successfully")

            return redirect('profile:edit')

    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, 'profile/edit/view.html', {
        'form': form,
    })

@login_required
def edit_url(request):
    if request.method == 'POST':
        form = URLForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()

            messages.success(request, "URL updated successfully")

            return redirect('profile:edit-url')

    else:
        form = URLForm(instance=request.user)

    return render(request, 'profile/edit/url.html', {
        'form': form,
    })

@login_required
def edit_picture(request):
    if request.method == 'POST':
        form = PictureForm(request.user, request.POST, request.FILES)

        if form.is_valid():
            form.save()

            messages.success(request, "Profile picture updated")

            return redirect('profile:edit-picture')

    else:
        form = PictureForm(request.user)

    return render(request, 'profile/edit/picture.html', {
        'form': form,
    })

@login_required
def edit_password(request):
    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Password changed successfully")

            return redirect('profile:edit-password')

    else:
        form = PasswordForm(request.user)

    return render(request, 'profile/edit/password.html', {
        'form': form,
    })
