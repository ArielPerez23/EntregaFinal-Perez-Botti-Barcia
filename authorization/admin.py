from django.contrib import admin

from authorization.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'first_name', 'last_name')
    

admin.site.register(User, UserAdmin)
