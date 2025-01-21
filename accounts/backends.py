from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.exceptions import MultipleObjectsReturned

class EmailBackend(ModelBackend):  # Corrected from ModelsBackend to ModelBackend
    """
    Custom authentication backend to authenticate users using either username or email.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Fetch the user using username or email (case-insensitive)
            user = User.objects.get(
                Q(username__iexact=username) |
                Q(email__iexact=username)
            )
        except User.DoesNotExist:
            # Return None if no matching user is found
            return None
        except MultipleObjectsReturned:
            # Handle multiple users with the same email by returning the first one
            user = User.objects.filter(email__iexact=username).order_by('id').first()
        else:
            # Check the password and if the user is active
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        return None

    def get_user(self, user_id):
        try:
            # Fetch the user by primary key (ID)
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            # Return None if the user does not exist
            return None
