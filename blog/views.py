from django.shortcuts import redirect, render
from django.http import HttpResponse

from django.views.generic import ListView, DetailView

from blog.models import Article
from blog.forms import NewArticle

from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


class HomeView(ListView):
    model = Article
    paginate_by = 4    
    template_name = 'blog/index.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/detalle_articulo.html'

def categoryView(request, articulo):
    
    category_post = Article.objects.filter(category = articulo)
    
    return render(request, "blog/categories.html", {"articulo":articulo, "category_post":category_post})

def software(request):
    
    return render(request, "blog/software.html")

def hardware(request):
    
    return render(request, "blog/hardware.html")

def curiosidades(request):
    
    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            curiosidades = Article.objects.filter( Q(title__icontains=search) | Q(body__icontains=search) ).values()

            return render(request,"blog/curiosidades.html",{"curiosidades":curiosidades, "search":True, "busqueda":search})

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
        
            if article.category == 'C':
                return redirect("curiosidades")
            elif article.category == 'H':
                return redirect("hardware")
            elif article.category == 'S':
                return redirect("software")
            else:
                return redirect("inicio")


        return redirect("nuevo_articulo")

    #get
    emptyForm = NewArticle()
    return render(request, "blog/nuevo_articulo.html",{"form":emptyForm})

def about(request):
    return render(request, "blog/about.html")
