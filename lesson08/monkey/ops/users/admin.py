from django.contrib import admin

# Register your models here.
from .models import Users, Manufacturer, Car, UserProfile

class UsersAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'age', 'phone', 'email']

    search_fields = ['username', 'phone']

    list_per_page = 15

    list_filter = ['username', 'phone']


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name', ]

    search_fields = ['name',]

    list_per_page = 15

class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'manufacturers']

    search_fields = ['name',]

    list_per_page = 15


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username_cn', 'users']

    search_fields = ['username_cn',]

    list_per_page = 15


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Users, UsersAdmin)
