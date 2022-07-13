from django.urls import path
from .views import *

urlpatterns = [
    #URLS BLOG
    path('software/', software, name= "software"),
    path('hardware/', hardware, name= "hardware"),
    path('curiosidades/', curiosidades, name= "curiosidades"),
    path('nuevo_articulo/', nuevo_articulo, name="nuevo_articulo"),
]
