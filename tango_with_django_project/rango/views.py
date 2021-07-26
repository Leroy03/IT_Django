from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def about(request):
    return render(request, 'about.html', {})
    # return HttpResponse("<html>Rango says here is the about page.</br><a href='/rango/'>Index</a></html>")


def index(request):
    context = {}
    return render(request, 'index.html', context)
    # return HttpResponse("<html>Rango says hey there partner!</br><a href='/rango/about/'>About</a></html>")
