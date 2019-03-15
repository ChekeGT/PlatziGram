"""Users app forms module."""


# Django
from django import forms


class UpdateProfileForm(forms.Form):
    picture = forms.ImageField(required=True)
    website = forms.URLField(max_length=200)
    biography = forms.CharField(max_length=1000)
    phone_number = forms.CharField(max_length=20)
