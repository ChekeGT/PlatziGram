"""Post app, views module."""
# Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Forms
from .forms import CreatePostForm

# Models
from .models import Post


@login_required
def post_list(request):
    """List existing posts."""
    posts = Post.objects.all().order_by('-created')
    return render(request, 'posts/feed.html', {'posts': posts})


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
