from django.shortcuts import render

from .forms import RegistrationForm

def view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()

            assert False, user
    else:
        form = RegistrationForm()

    return render(request, 'registration/view.html', {
        'form': form,
    })
