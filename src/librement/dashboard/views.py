from django.shortcuts import render

def view(request):
    if not request.user.is_authenticated():
        return render(request, 'static/landing.html')

    return render(request, 'dashboard/view.html')
