from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Article
from .forms import NewArticle


def inicio(request):
    
    return render(request, "blog/index.html")

def software(request):
    
    return render(request, "blog/software.html")

def hardware(request):
    
    return render(request, "blog/hardware.html")

def curiosidades(request):
    
    curiosidades = Article.objects.all()
        
    return render(request, "blog/curiosidades.html",{"curiosidades":curiosidades})

def nuevo_articulo(request):

    #post
    if request.method == 'POST':

        formulario = NewArticle(request.POST)
        
        if formulario.is_valid():
            
            info_articulo = formulario.cleaned_data
        
            articulo = Article(title=info_articulo["title"],subtitle=info_articulo["subtitle"],body=info_articulo["body"])
        
            articulo.save()
        
            return redirect("curiosidades")
        
        return redirect("nuevo_articulo")

    #get
    formularioVacio = NewArticle()
    return render(request, "blog/nuevo_articulo.html",{"form":formularioVacio})

def buscar_articulo(request):
    pass