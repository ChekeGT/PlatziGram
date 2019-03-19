"""Urls configuration of Users app."""

# Django
from django.urls import path

# Views
from users.views import login_view, logout_view, ProfileDetailView, SignupView, UpdateProfileView

urlpatterns = [
    # Profile.
    path('profile/@<str:username>/', ProfileDetailView.as_view(), name='profile_detail'),

    # Management of user.
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('update_profile/', UpdateProfileView.as_view(), name='update_profile'),
]