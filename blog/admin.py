from django.contrib import admin
from blog.models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display=('title', 'subtitle', 'author', 'category', 'created_at')
    search_fields=('title', 'subtitle', 'author', 'category', 'created_at')

admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)


