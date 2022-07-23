from cgitb import reset
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import ListView, DetailView

from blog.models import Article, Message
from blog.forms import NewArticle, UserEditForm

from django.db.models import Q
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


class HomeView(ListView):
    model = Article
    paginate_by = 4    
    template_name = 'blog/index.html'
    ordering = ['-created_at']

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/detalle_articulo.html'

class MessageView(ListView):
    model = Message
    #paginate_by = 4    
    template_name = 'blog/mensajes.html'

def LikeView(request, pk):
    post = get_object_or_404(Article, id=request.POST.get('post_id'))
    post.likes.add (request.user)
    return HttpResponseRedirect(reverse('post_detail',args=[str(pk)]))


def software(request):
    
    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            software = Article.objects.filter( Q(title__icontains=search) | Q(body__icontains=search) ).values()

            return render(request,"blog/software.html",{"software":software, "search":True, "busqueda":search})

    software = Article.objects.all()

    return render(request, "blog/software.html",{"software":software})

def hardware(request):
    
    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            hardware = Article.objects.filter( Q(title__icontains=search) | Q(body__icontains=search) ).values()

            return render(request,"blog/hardware.html",{"hardware":hardware, "search":True, "busqueda":search})

    hardware = Article.objects.all()

    return render(request, "blog/hardware.html",{"hardware":hardware})

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


@login_required
def editar_perfil(request):

    user = request.user 

    if request.method == "POST":

        form = UserEditForm(request.POST)

        if form.is_valid():

            info = form.cleaned_data
            user.email = info['email']
            user.password1 = info['password1']
            user.password2 = info['password2']
            
            user.save()

            return redirect("inicio")
    form = UserEditForm(request.GET)

    return render(request, "blog/editarperfil.html",{"usereditform": form})
