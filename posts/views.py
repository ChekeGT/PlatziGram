"""Post app, views module."""
# Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

# Forms
from .forms import CreatePostForm

# Models
from .models import Post


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    ordering = ('-created',)
    template_name = 'posts/feed.html'
    context_object_name = 'posts'


@login_required
def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = CreatePostForm()

    return render(request, 'posts/create.html', {'form': form})
