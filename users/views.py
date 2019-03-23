"""Users app views module."""

# Django
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView

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

    def get(self, request, *args, **kwargs):
        """
         Manages the necessary processes to follow
         or stop following a profile,
         besides that inherits its parent functionality
         and passing that, follows the same normal
         operation, which means return the render.
         """
        profile_user = self.get_object()
        request_user = request.user
        if 'follow' in request.GET:
            profile_user.followers.add(request.user)
            request_user.following.add(profile_user)

        elif 'unfollow' in request.GET:
            profile_user.followers.remove(request.user)
            request_user.following.remove(profile_user)

        return super(ProfileDetailView, self).get(request, args, kwargs)

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


class PlatzigramLoginView(LoginView):
    """Class Based View that manages the login of the users."""
    template_name = 'users/login.html'
    redirect_authenticated_user = True


class PlatzigramLogoutView(LoginRequiredMixin, LogoutView):
    """Class Based View that manages the logout of the users."""
    pass


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


class UpdateProfileView(LoginRequiredMixin, UpdateView):
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
