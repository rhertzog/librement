from django.shortcuts import render, redirect

from .forms import ForgotPasswordForm

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
