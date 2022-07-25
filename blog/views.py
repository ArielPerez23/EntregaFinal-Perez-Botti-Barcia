from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect

from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy

from blog.models import Article, Comment
from blog.forms import NewArticle, CommentForm

from django.db.models import Q
from django.urls import reverse

from django.contrib.auth.decorators import login_required


class HomeView(ListView):
    model = Article
    paginate_by = 4    
    template_name = 'blog/index.html'
    ordering = ['-created_at']



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

@login_required
def nuevo_articulo(request):

    #post
    if request.method == 'POST':

        form = NewArticle(request.POST, request.FILES)
        
        if form.is_valid():
            
            info = form.cleaned_data
            
            article = Article(title=info['title'], subtitle=info['subtitle'], body=info['body'], image=info['image'], category=info['category'])
        
            article.save()
        
            if article.category == 'Curiosidades':
                return redirect("curiosidades")
            elif article.category == 'Hardware':
                return redirect("hardware")
            elif article.category == 'Software':
                return redirect("software")
            else:
                return redirect("inicio")

        return redirect("nuevo_articulo")

    #get
    emptyForm = NewArticle()
    return render(request, "blog/nuevo_articulo.html",{"form":emptyForm})

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/detalle_articulo.html'

    def get_context_data(self, *args , **kwargs):
        context= super(ArticleDetailView, self).get_context_data()
        stuff= get_object_or_404(Article, id=self.kwargs['pk'])
        total_likes= stuff.total_likes()
        context['total_likes']=total_likes
        return context

class ArticleDelete(DeleteView):
    
    model = Article
    success_url = reverse_lazy('inicio')

class ArticleUpdate(UpdateView):

    model = Article
    success_url = reverse_lazy('inicio')
    fields = ["title", "subtitle", "body", "image"]


def about(request):
    return render(request, "blog/about.html")

class AddCommentView(CreateView):
    model=Comment
    template_name= 'blog/agregar_comentario.html'
    form_class = CommentForm
    success_url = reverse_lazy('inicio')

    def form_valid(self,form):
        form.instance.article_id = self.kwargs['pk']
        return super().form_valid(form)