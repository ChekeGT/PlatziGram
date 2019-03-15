"""Posts app forms module."""

# Django
from django import forms

# Model
from .models import Post


class CreatePostForm(forms.ModelForm):
    """Form that allows you to create a post."""

    class Meta:
        """Form model subclass configuration which contains the fields and the model."""
        model = Post
        fields = ('user', 'title', 'photo')
