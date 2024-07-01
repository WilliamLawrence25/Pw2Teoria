from django.shortcuts import render
from .models import Persona

# Create your views here.
def personaTestView(request):
    obj = Persona.objects.get(id = 1)
    context ={
        'nombre': obj.nombres,
        'edad': obj.edad,
        }
    return render(request, 'personas/test.html', context)