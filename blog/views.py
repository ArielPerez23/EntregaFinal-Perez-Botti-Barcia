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

        form = NewArticle(request.POST, request.FILES)
        
        if form.is_valid():
            
            info = form.cleaned_data
            
            article = Article(title=info['title'], subtitle=info['subtitle'], body=info['body'], image=info['image'], category=info['category'])
        
            article.save()
        
            return redirect("curiosidades")
        
        return redirect("nuevo_articulo")

    #get
    emptyForm = NewArticle()
    return render(request, "blog/nuevo_articulo.html",{"form":emptyForm})

def buscar_articulo(request):
    pass

def about(request):
    return render(request, "blog/about.html")
