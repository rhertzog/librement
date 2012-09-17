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
    return render(request, 'registration/confirm.html')
