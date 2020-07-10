from django.contrib import admin

# Register your models here.
from .models import Users

class UsersAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'age', 'phone', 'email']

    search_fields = ['username', 'phone']

    list_per_page = 3

    list_filter = ['username', 'phone']



admin.site.register(Users, UsersAdmin)
