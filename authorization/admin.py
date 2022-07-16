from django.contrib import admin

from authorization.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','email')
    

admin.site.register(User, UserAdmin)
