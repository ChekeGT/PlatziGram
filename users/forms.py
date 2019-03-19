"""Users app forms module."""


# Django
from django import forms

# Models
from .models import User


class SignupForm(forms.Form):
    """Form to validate and creates a User."""
    username = forms.CharField(min_length=1, max_length=50, required=True)

    password = forms.CharField(
        min_length=5,
        max_length=100,
        widget=forms.PasswordInput(),
        required=True
    )
    password_confirmation = forms.CharField(
        min_length=5,
        max_length=100,
        widget=forms.PasswordInput(),
        required=True
    )

    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    email = forms.EmailField(max_length=200, required=True)

    def clean_username(self) -> 'cleaned data':
        """It ensures that the picked username isn't used by other person."""
        data = self.cleaned_data
        username = data['username']

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El nombre de usuario que elegiste ya esta ocupado.')

        return username

    def clean_email(self) -> 'cleaned data':
        """It ensures that the picked email isn't used by other person."""
        data = self.cleaned_data
        email = data['email']

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email que has proporcionado, ya se encuentra en uso por otro usuario.')

        return email
    
    def clean(self) -> 'cleaned data':
        """Verifies that password and its confirmation are equals."""
        data = super(SignupForm, self).clean()

        password = data.get('password')
        password_confirmation = data.get('password_confirmation')

        if password != password_confirmation:
            raise forms.ValidationError('La contraseña y su confirmacion no coinciden.')
        return data

    def save(self) -> None:
        """Saves a User object with cleaned data in the database."""
        data = self.cleaned_data
        data.pop('password_confirmation')

        User.objects.create_user(**data)
