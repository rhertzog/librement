from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from librement.utils.ajax import ajax

from .forms import ProfileForm, URLForm, PictureForm
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
