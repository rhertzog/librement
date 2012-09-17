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
