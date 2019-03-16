"""Posts app urls configuration."""

# Django
from django.urls import path

# Views
from posts.views import post_list, create_post


urlpatterns = [
    path('', post_list, name='feed'),
    path('posts/new/', create_post, name='create_post'),
]