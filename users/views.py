"""Users app views module."""
# Django

from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login

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
