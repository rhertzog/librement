from django.contrib.auth.backends import ModelBackend

from .models import Email

class LibrementBackend(ModelBackend):
    def authenticate(self, email=None, password=None):
        try:
            email = Email.objects.get(email__iexact=email)

            if email.user.check_password(password):
                return email.user

        except Email.DoesNotExist:
            return None
