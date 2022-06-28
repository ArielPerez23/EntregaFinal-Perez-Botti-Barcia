from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Curiosity

from .forms import *


def inicio(request):
    
    return render(request, "blog/index.html")

def software(request):
    
    return render(request, "blog/software.html")

def hardware(request):
    
    return render(request, "blog/hardware.html")

def curiosidades(request):

    if request.method == 'POST':

        formulario = CuriosidadesForm(request.POST)

        print(formulario)

        if formulario.is_valid():
            data = formulario.cleaned_data

            curiosidad = Curiosity(title=data['titulo'], subtitle=data['subtitulo'], content=data['contenido'])
            curiosidad.save()
            
            return render(request, "blog/index.html")

    else:
        formulario = CuriosidadesForm()
    
    return render(request, "blog/curiosidades.html" ,{'curiosidades':formulario})

