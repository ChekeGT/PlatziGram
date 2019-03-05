"""Posts app admin configurations module."""

# Django

from django.contrib import admin

# Models
from .models import Post


class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
