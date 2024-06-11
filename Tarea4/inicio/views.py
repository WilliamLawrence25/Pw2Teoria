from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myHomeView(*args, **kwargs):
    return HttpResponse('<h1>Hola mundo desde Django</h1>')
