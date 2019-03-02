"""Users app models module."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    website = models.URLField(blank=True, max_length=200)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(blank=True, null=True, max_length=20)

    picture = models.ImageField(blank=True, null=True, upload_to='users/pictures')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
