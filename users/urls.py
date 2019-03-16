"""Urls configuration of Users app."""

# Django
from django.urls import path

# Views
from users.views import login_view, logout_view, signup_view, update_profile_view, ProfileDetailView

urlpatterns = [
    # Profile.
    path('profile/@<str:username>/', ProfileDetailView.as_view(), name='profile_detail'),

    # Management of user.
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('update_profile/', update_profile_view, name='update_profile'),
]