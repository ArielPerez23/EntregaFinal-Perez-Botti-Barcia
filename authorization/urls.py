from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    #URLS Autentication
    path('login/', login_request, name="login"),
    path('register/', register_request, name="register"),
    path('logout/', logout_request, name="logout"),
    path('editar_avatar/', editar_avatar, name="editar_avatar"), 
    path('edit_profile/', EditarPerfil.as_view(), name="editar_perfil"),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='blog/change_password.html')),
    path('password/', PasswordsChangeView.as_view(template_name='blog/change_password.html')),
]