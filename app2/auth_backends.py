# vendors/auth_backends.py
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import Staff

class StaffAuthenticationBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        Authenticate a staff by username (email) and password.
        """
        try:
            # Attempt to retrieve the staff by username (email)
            staff = Staff.objects.get(username=username)

            # Check the hashed password
            if staff.check_password(password):
                return staff
        except Staff.DoesNotExist:
            return None

    def get_user(self, user_id):
        """
        Retrieve a staff by their primary key.
        """
        try:
            return Staff.objects.get(pk=user_id)
        except Staff.DoesNotExist:
            return None
