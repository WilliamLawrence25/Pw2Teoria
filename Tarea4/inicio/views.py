from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myHomeView(request, *args, **kwargs):
    print (args, kwargs)
    print (request.user)
    return HttpResponse('<h1>Hola mundo desde Django</h1>')

def anotherView(request):
    return HttpResponse('<h1>Solo otra pagina</h1>')
