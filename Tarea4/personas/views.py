from django.shortcuts import render
from .models import Persona

# Create your views here.
def personaTestView(request):
    obj = Persona.objects.get(id = 1)
    context ={
        'objeto': obj,
        }
    return render(request, 'personas/descripcion.html', context)