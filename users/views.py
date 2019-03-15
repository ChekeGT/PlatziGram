"""Users app views module."""
# Django

from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

# Exceptions

from django.db.utils import IntegrityError

# Local Apps

from .models import User

# Forms

from .forms import UpdateProfileForm

class UserCantBeCreated(Exception):
    """Exception for raise when a user, cant be created"""
    pass


def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return redirect(reverse('login') + '?error')
    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    logout(request)

    return redirect('login')


def signup_view(request):
    """Signup View."""
    if request.method == 'POST':
        errors = []

        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        email = request.POST['email']

        try:
            if password != password_confirmation:
                errors += 'La contraseña y su confirmacion no coinciden.\n'
                raise UserCantBeCreated("User cant be created because the password is not the same in both sides.")

            user = User.objects.create_user(username=username, password=password, email=email)

        except (IntegrityError, UserCantBeCreated):
            if User.objects.filter(username=username):
                errors += '\nEse nombre de usuario ya esta ocupado.\n'

            if User.objects.filter(email=email):
                errors += '\nEse correo electronico, ya esta en uso :(.\n'

            return redirect(reverse('signup') + f'?errors={"".join(errors)}')

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        return redirect('login')
    return render(request, 'users/signup.html')


def update_profile_view(request):
    """View that allow users to update them profiles"""
    if request.method == 'POST':
        user = request.user
        form = UpdateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            user.website = data['website']
            user.bio = data['biography']
            user.phone_number = data['phone_number']
            user.picture = data['picture']
            user.save()
            return redirect(reverse('update_profile') + '?updated')
    else:
        form = UpdateProfileForm()
    return render(request, 'users/update_profile.html', {'form': form})
