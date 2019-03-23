"""Post app, views module."""
# Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

# Forms
from .forms import CreatePostForm

# Models
from .models import Post


class PostListView(LoginRequiredMixin, ListView):
    """Class based view that manages the feed(List of Posts)."""
    model = Post
    ordering = ('-created',)
    template_name = 'posts/feed.html'
    context_object_name = 'posts'
    paginate_by = 30

    def get_queryset(self):
        """
        Modify the queryset of posts either by showing all
        in case we don't follow anyone, or by showing only
        our own and those of the people we follow.
        """
        user = self.request.user

        posts = super(PostListView, self).get_queryset()
        own_posts = posts.filter(user=user)

        following = user.following.all()
        if following:

            following_posts = posts.filter(user__in=following)
            if following_posts:

                return following_posts + own_posts

        return posts


class CreatePostView(LoginRequiredMixin, CreateView):
    """Manages the view with which a user can create a post."""

    template_name = 'posts/create.html'
    model = Post
    queryset = Post.objects.all()
    form_class = CreatePostForm
    context_object_name = 'post'
    success_url = reverse_lazy('feed')


class PostDetailView(LoginRequiredMixin, DetailView):
    """Manages the view of a Post, and shows its details."""
    model = Post
    template_name = 'posts/detail.html'
    context_object_name = 'post'
    slug_field = 'pk'
    slug_url_kwarg = 'pk'
