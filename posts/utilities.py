"""Posts app utilities module."""

# Models
from .models import Like


def already_liked(user, post):
    """Returns if a user already liked a post."""

    return Like.objects.filter(user=user).filter(post=post).exists()


def number_of_likes(post):
    """Returns how many likes has a post."""

    return len(Like.objects.filter(post=post))
