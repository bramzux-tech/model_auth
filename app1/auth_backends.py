# auth_backends.py
from django.contrib.auth.backends import BaseBackend
from .models import Student

class StudentAuthenticationBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Student.objects.get(student_id=username)
            if user.check_password(password):
                return user
        except Student.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Student.objects.get(pk=user_id)
        except Student.DoesNotExist:
            return None
