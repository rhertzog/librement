from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import ProfileForm, URLForm, PictureForm

def view(request, username):
    user = get_object_or_404(User, username=username)

    return render(request, 'profile/view.html', {
        'user': user,
    })

@login_required
def edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)

        if form.is_valid():
            form.save()

            return redirect('profile:view', request.user.username)

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

            return redirect('profile:view', request.user.username)

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

            return redirect('profile:view', request.user.username)

    else:
        form = PictureForm(request.user)

    return render(request, 'profile/edit/picture.html', {
        'form': form,
    })
