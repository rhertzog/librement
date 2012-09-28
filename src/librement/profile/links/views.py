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

from .forms import LinkForm

@login_required
def view(request):
    return render(request, 'profile/links/view.html')

@login_required
def add_edit(request, link_id=None):
    if link_id:
        link = get_object_or_404(request.user.links, pk=link_id)
    else:
        link = None

    if request.method == 'POST':
        form = LinkForm(request.POST, instance=link)

        if form.is_valid():
            link = form.save(commit=False)
            link.user = request.user
            link.save()

            if link:
                messages.success(request, "Link updated successfully.")
            else:
                messages.success(request, "Link added successfully.")

            return redirect('profile:links:view')

    else:
        form = LinkForm(instance=link)

    return render(request, 'profile/links/add_edit.html', {
        'link': link,
        'form': form,
    })

@require_POST
@login_required
def delete(request, link_id):
    link = get_object_or_404(request.user.links, pk=link_id)

    link.delete()

    messages.success(request, "Link deleted.")

    return redirect('profile:links:view')
