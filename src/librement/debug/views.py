from django.shortcuts import render

def error(request, code):
    return render(request, '%s.html' % code)
