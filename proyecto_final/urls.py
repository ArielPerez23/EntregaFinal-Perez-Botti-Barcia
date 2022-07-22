from django.contrib import admin
from django.urls import path, include

#Para imagenes
from django.conf import settings
from django.conf.urls.static import static

from blog.views import *
from authorization.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name= "inicio"),

    #URLS BLOG
    path('blog/', include('blog.urls')),
    
    #URLS authorization
    path('authorization/', include('authorization.urls'))
]

#Imagenes
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)