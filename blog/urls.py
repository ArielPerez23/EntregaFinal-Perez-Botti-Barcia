from django.urls import path
from .views import *

urlpatterns = [
    #URLS BLOG
    path('software/', software, name= "software"),
    path('hardware/', hardware, name= "hardware"),
    path('curiosidades/', curiosidades, name= "curiosidades"),
    
    path('nuevo_articulo/', nuevo_articulo, name="nuevo_articulo"),
    path('eliminar_articulo/<articulo_id>', eliminar_articulo, name="eliminar_articulo"),
    path('editar_articulo/<articulo_id>', editar_articulo, name="editar_articulo"),

    path('post/<int:pk>', ArticleDetailView.as_view(), name='post_detail'),

    path('about/', about, name="about"),
    path('editarperfil/', editar_perfil, name="editarperfil"),
    path('post/<int:pk>', ArticleDetailView.as_view(), name='post_detail'),
    path('mensajes/', MessageView.as_view(), name='messages'),
    path('like/<int:pk>', LikeView, name='like_post'),
    
]
