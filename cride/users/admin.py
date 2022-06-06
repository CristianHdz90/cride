"""Users models admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from .models import User, Profile


class ProfileInline(admin.StackedInline):
    """Profile model admin settings"""

    model = Profile


class CustomUserAdmin(UserAdmin):
    """Additional settings for user model admin"""

    inlines = (ProfileInline,)
    list_display = ("username", "email", "is_staff", "is_client", "is_verified")
    list_filter = ("is_client", "is_staff", "created", "modified")


admin.site.register(User, CustomUserAdmin)
