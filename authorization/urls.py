from django.urls import path
from .views import *

urlpatterns = [
    #URLS Autentication
    path('', home, name="inicio"),
    path('login/', login_request, name="login"),
    path('register/', register_request, name="register"),
    path('logout/', logout_request, name="logout")
    
    
]