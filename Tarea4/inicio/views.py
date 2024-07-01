from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.

def myHomeView(request, *args, **kwargs):
    myContent = {
        'myText': 'Esto es sobre nosotros',
        'myNumber': 123,
        'myList': [33, 44, 55],
    }
    return render(request, "home.html", myContent)

def anotherView(request):
    return HttpResponse('<h1>Solo otra pagina</h1>')
