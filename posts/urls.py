"""Posts app urls configuration."""

# Django
from django.urls import path

# Views
from posts.views import PostListView, CreatePostView, PostDetailView


urlpatterns = [
    path('', PostListView.as_view(), name='feed'),
    path('posts/new/', CreatePostView.as_view(), name='create_post'),
    path('posts/<int:pk>/<str:title>/', PostDetailView.as_view(), name='post_detail')
]