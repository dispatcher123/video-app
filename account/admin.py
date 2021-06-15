from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display=('email','username','login_date','is_active','is_admin')
    list_display_links=('username',)
    search_fields=('is_active',)
    fieldsets=()
    filter_horizontal=()
    list_filter=('is_active',)
