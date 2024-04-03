from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import CustomUser
from .forms import UserCreationForm, UserChangeForm

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'name', 'is_active', 'is_staff',  'is_superuser')
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser', 'password',)}),
        ('Personal info', {'fields': ('name',)}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser', 'password1', 'password2',)}),
        ('Personal info', {'fields': ('name',)}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    search_fields = ('email', 'name')
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(CustomUser, UserAdmin)
