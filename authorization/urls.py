from django.urls import path
from .views import *

urlpatterns = [
    #URLS Autentication
    path('login/', login_request, name="login"),
    path('register/', register_request, name="register"),
    path('logout/', logout_request, name="logout"),
    # path('editar_perfil/', editar_perfil, name="editar_perfil"),
    path('editar_avatar/', editar_avatar, name="editar_avatar"), 
    path('edit_profile/', EditarPerfil.as_view(), name="editar_perfil"),
]