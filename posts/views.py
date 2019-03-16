"""Post app, views module."""
# Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

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


@login_required
def create_post(request) -> 'Http Response':
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = CreatePostForm()

    return render(request, 'posts/create.html', {'form': form})


class PostDetailView(LoginRequiredMixin, DetailView):
    """Manages the view of a Post, and shows its details."""
    model = Post
    template_name = 'posts/detail.html'
    context_object_name = 'post'
    slug_field = 'title'
    slug_url_kwarg = 'title'
