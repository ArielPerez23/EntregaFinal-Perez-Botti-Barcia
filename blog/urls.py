from django.urls import path

from .views import *

urlpatterns = [
    #URLS BLOG
    path('', inicio),
    
    path('software/', software, name= "software"),
    path('hardware/', hardware, name= "hardware"),
    path('curiosidades/', curiosidades, name= "curiosidades"),
    
]
