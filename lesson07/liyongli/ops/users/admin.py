from django.contrib import admin

# Register your models here.

from .models import Users

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'age', 'phone', 'email']

admin.site.register(Users, UserAdmin)
