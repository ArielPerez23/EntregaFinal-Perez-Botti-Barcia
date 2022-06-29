from django.shortcuts import redirect, render
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
    
    curiosidades = Curiosity.objects.all()
        
    return render(request, "blog/curiosidades.html",{"curiosidades":curiosidades})

def nueva_publicacion(request):

    if request.method == 'POST':

        formulario = NuevaPublicacion(request.POST)
        
        if formulario.is_valid():
            
            info_publicacion = formulario.cleaned_data
        
            publicacion = Curiosity(title=info_publicacion['titulo'], content=info_publicacion['contenido'])
        
            publicacion.save()
        
            return redirect("curiosidades")
        else:
            return redirect("nueva_publicacion")
    else:

        formularioVacio = NuevaPublicacion()

        return render(request, "blog/nueva_publicacion.html" ,{"form":formularioVacio})

def buscar_publicacion(request):
    pass