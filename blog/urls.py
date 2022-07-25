from django.urls import path
from .views import *

urlpatterns = [
    #URLS BLOG
    path('software/', software, name= "software"),
    path('hardware/', hardware, name= "hardware"),
    path('curiosidades/', curiosidades, name= "curiosidades"),
    path('about/', about, name="about"),
    
    path('nuevo_articulo/', nuevo_articulo, name="nuevo_articulo"),
    path('articulo/editar/<pk>', ArticleUpdate.as_view(), name="article_edit"),
    path('articulo/eliminar/<pk>', ArticleDelete.as_view(), name="article_delete"),
    path('post/<int:pk>', ArticleDetailView.as_view(), name='post_detail'),
    
    path('like/<int:pk>', LikeView, name='like_post'),  
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name='agregar_comentario')
]
