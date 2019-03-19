"""Users app views module."""

# Django
from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, FormView, UpdateView

# Models
from .models import User
from posts.models import Post

# Forms
from .forms import SignupForm


class ProfileDetailView(LoginRequiredMixin, DetailView):
    """Class based view that manages the detail of a user profile."""
    template_name = 'users/profile_detail.html'
    model = User
    queryset = User.objects.all()
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        """
            Insert the posts created by the user
            in the context data tho show them
            on the template.
        """
        context = super(ProfileDetailView, self).get_context_data()
        user = context['user']

        posts = Post.objects.filter(user=user)
        context['posts'] = posts

        return context


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


class SignupView(FormView):
    """View that manages the register of new users in the website."""

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('login')

    def form_valid(self, form) -> 'Http Response Redirect':
        """
        If the form is valid this function will be executed and will save the form.
        After that it will redirect the user to the value in success_url.
        """
        form.save()
        return super(SignupView, self).form_valid(form)


class UpdateProfileView(UpdateView):
    """Manages the view with which a user can update their profile."""

    template_name = 'users/update_profile.html'
    model = User
    fields = ['website', 'bio', 'phone_number', 'picture']

    def get_object(self, queryset=None) -> 'User':
        """Returns the user that is making the request."""
        return self.request.user

    def get_success_url(self) -> 'str':
        """Returns a reversed url, to the users profile template."""
        username = self.object.username
        return reverse_lazy('profile_detail', args=[username])
