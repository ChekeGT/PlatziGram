"""Post app, views module."""
# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, RedirectView
from django.urls import reverse_lazy
from django.http import JsonResponse

# Forms
from .forms import CreatePostForm

# Models
from .models import Post, Like

# Utilities
from .utilities import already_liked, number_of_likes


class PostListView(LoginRequiredMixin, ListView):
    """Class based view that manages the feed(List of Posts)."""
    model = Post
    ordering = ('-created',)
    template_name = 'posts/feed.html'
    context_object_name = 'posts'
    paginate_by = 30

    def get_queryset(self):
        """Returns the list of posts filtered."""

        posts = self.filter_posts(super(PostListView, self).get_queryset())

        for post in posts:
            post.likes = number_of_likes(post)
            # Boolean that indicates if the request user has already liked this post.
            post.liked_by_me = already_liked(self.request.user, post)

        return posts

    def filter_posts(self, posts):
        """
            Modify the queryset of posts either by showing all
            in case we don't follow anyone, or by showing only
            our own and those of the people we follow.
         """
        user = self.request.user
        own_posts = posts.filter(user=user)

        following = user.following.all()
        if following:

            following_posts = posts.filter(user__in=following)
            if following_posts and own_posts:

                posts = [following_posts, own_posts]

            elif following_posts:
                posts = following_posts

            elif own_posts:
                posts = own_posts

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

    def get_object(self, queryset=None):
        """Returns the post object by default but it adds the number of like it has."""
        post = super(PostDetailView, self).get_object(queryset)
        post.likes = number_of_likes(post)

        # Boolean that indicates if the request user has already liked this post.
        post.liked_by_me = already_liked(self.request.user, post)

        return post


class LikePostView(LoginRequiredMixin, RedirectView):
    """View that makes the like process asynchronous"""

    def get(self, request, *args, **kwargs):
        """
        If a publication is'nt liked by a user it
        likes it and returns a JsonResponse.
        """
        json_response = {}
        try:
            post_pk = kwargs['pk']
            user = self.request.user

            post = Post.objects.get(pk=post_pk)

            if already_liked(user=user, post=post):
                Like.objects.get(post=post, user=user).delete()
                json_response['liked'] = False
                json_response['unliked'] = True

            else:
                Like.objects.create(post=post, user=user)
                json_response['liked'] = True
                json_response['unliked'] = False

        except Exception as e:
            json_response['status'] = 400

        else:
            json_response['status'] = 200

        return JsonResponse(json_response)
