from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'public_visibility', 'birth_year', 'address', 'age')

    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('public_visibility', 'birth_year', 'address')
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {
            'fields': ('public_visibility', 'birth_year', 'address')
        }),
    )

   
    def age(self, obj):
        return obj.age
    age.admin_order_field = 'birth_year'  

from .models import UploadedFile

@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'visibility', 'cost', 'year_of_publication')
