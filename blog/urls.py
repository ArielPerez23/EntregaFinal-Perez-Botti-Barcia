from django.urls import path
from .views import *

urlpatterns = [
    #URLS BLOG
    path('software/', software, name= "software"),
    path('hardware/', hardware, name= "hardware"),
    path('curiosidades/', curiosidades, name= "curiosidades"),
    path('nuevo_articulo/', nuevo_articulo, name="nuevo_articulo"),
    path('about/', about, name="about"),
    path('category/<str:articulo>/', categoryView, name="category"),
    path('post/<int:pk>', ArticleDetailView.as_view(), name='post_detail')
    
]
