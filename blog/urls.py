from django.urls import path
from .views import *
from authorization.views import *

urlpatterns = [
    #URLS BLOG
    path('editarperfil/', editar_perfil, name="editarperfil"),
    path('agregar_avatar/', agregar_avatar, name="agregar_avatar"),

    path('software/', software, name= "software"),
    path('hardware/', hardware, name= "hardware"),
    path('curiosidades/', curiosidades, name= "curiosidades"),
    path('about/', about, name="about"),
    
    path('nuevo_articulo/', nuevo_articulo, name="nuevo_articulo"),
    path('eliminar_articulo/<articulo_id>', eliminar_articulo, name="eliminar_articulo"),
    path('articulo/editar/<pk>', ArticleUpdate.as_view(), name="editar_articulo"),

    
    #path('post/<int:pk>', ArticleDetailView.as_view(), name='post_detail'), 
    path('post/<int:pk>', ArticleDetailView.as_view(), name='post_detail'),
    path('mensajes/', MessageView.as_view(), name='messages'),
    path('like/<int:pk>', LikeView, name='like_post'),  
]
