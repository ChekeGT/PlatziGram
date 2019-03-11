"""Users app views module."""
# Django
from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required


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


@login_required()
def logout_view(request):
    logout(request)

    return redirect('login')
