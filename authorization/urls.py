from django.urls import path
from .views import *

urlpatterns = [
    #URLS Autentication
    path('', home, name="inicio"),
    path('login/', login_request, name="login"),
    path('register/', register_request, name="register"),
    path('logout/', logout_request, name="logout"),
    path('editar_perfil/', editar_perfil, name="editar_perfil"),
    path('agregar_avatar/', agregar_avatar, name="agregar_avatar"),    
]