"""Posts app urls configuration."""

# Django
from django.urls import path

# Views
from posts.views import PostListView, create_post, PostDetailView


urlpatterns = [
    path('', PostListView.as_view(), name='feed'),
    path('posts/new/', create_post, name='create_post'),
    path('posts/<str:title>/', PostDetailView.as_view(), name='post_detail')
]