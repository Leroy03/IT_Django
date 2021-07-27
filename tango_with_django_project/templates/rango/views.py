from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def about(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, './rango/about.html', context=context_dict)
    # return HttpResponse("<html>Rango says here is the about page.</br><a href='/rango/'>Index</a></html>")


def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, './rango/index.html', context=context_dict)
