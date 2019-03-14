"""Users app middlewares module."""

# Django
from django.shortcuts import redirect,reverse


class ProfileCompletionMiddleware:
    """
    Middleware that ensures a registered user has a profile picture
    and if he doesnt have it redirects him to add it in a view
    for updating his profile.
    """

    def __init__(self, get_response):
        """Middleware intialization function."""
        self.get_response = get_response

    def __call__(self, request):
        """Code that will be called before every view.
        it will check that user had a profile picture
        """
        banned_urls = [reverse('logout'), reverse('update_profile')]
        if not request.user.is_anonymous and request.path not in banned_urls:
            if not request.user.picture:
                return redirect(reverse('update_profile') + '?not_profile_picture')

        response = self.get_response(request)
        return response
