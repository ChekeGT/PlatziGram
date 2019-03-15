"""Users app views module."""

# Django
from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

# Forms
from .forms import UpdateProfileForm, SignupForm


def login_view(request) -> 'Http Response':
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
def logout_view(request) -> 'Http Response':
    logout(request)

    return redirect('login')


def signup_view(request):
    """Signup View."""
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {'form':form})


@login_required
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
