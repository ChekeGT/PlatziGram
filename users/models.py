"""Users app models module."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    website = models.URLField(blank=True, max_length=200)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(blank=True, max_length=20)
    email = models.EmailField(unique=True)
    picture = models.ImageField(blank=True, null=True, upload_to='users/pictures')

    followers = models.ManyToManyField('self', symmetrical=False,related_name='following')

    def __str__(self):
        """Returns the username."""

        return self.username

    def follow(self, user):
        """Function that allows this model to follow an user.
        Receive two parameters:
            -self --> The user who called this function and who is going to follow another.
            -user --> The user who will start to be followed.
        """

        try:

            self.following.add(user)
            user.followers.add(self)

        except Exception as e:

            print(type(e).__name__)
            return False
        else:
            return True

    def unfollow(self, user):
        """Function that allows this model to unfollow an user.
        Receive two parameters:
            -self --> The user who called this function to stop following another.
            -user --> The user who is going to stop being followed
        """

        try:
            self.following.remove(user)
            user.followers.remove(self)

        except Exception as e:
            print(type(e).__name__)
            return False

        else:
            return True