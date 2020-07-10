from django.contrib import admin

# Register your models here.
from .models import Users

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'password', 'roles']
    list_per_page = 2

admin.site.register(Users, UserAdmin)