from django.contrib import admin
from django.urls import path, include
from blog.views import *

from .views import *

urlpatterns = [
    #URLS BLOG
    path('', inicio, name= "inicio"),

    path('software/', software, name= "software"),
    path('hardware/', hardware, name= "hardware"),
    path('curiosidades/', curiosidades, name= "curiosidades"),
    
]
