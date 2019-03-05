"""Users app Admin module."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        (
            'Perfil', {
                'fields': (
                    'website',
                    'bio',
                    'phone_number',
                    'picture'
                )
            }
        ),
    )


admin.site.register(User, UserAdmin)
