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

            return redirect('static:landing')

    else:
        form = LoginForm()

    return render(request, 'account/login.html', {
        'form': form,
    })

def logout(request):
    django_logout(request)

    return redirect('static:landing')
