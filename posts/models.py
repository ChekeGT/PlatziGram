"""Post app  models module."""

# Django

from django.db import models

# Models
from users.models import User


class Post(models.Model):
    """Posts Model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photograph')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return the post title and the creator username."""
        return f'{self.title} by @{self.user.username}'
