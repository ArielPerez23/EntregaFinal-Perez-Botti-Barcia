from django.contrib import admin
from blog.models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display=('title','subtitle', 'author' )

admin.site.register(Article,ArticleAdmin)

