from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *
# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        ("User Info", {'fields': ('username', 'password' , 'email', 'first_name', 'last_name')}),
              ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'user', 'created_at', 'updated_at']


@admin.register(Stash)
class StashAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'url', 'category', 'user', 'created_at', 'updated_at']
