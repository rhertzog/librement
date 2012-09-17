from django.contrib.auth.backends import ModelBackend

from .models import Email

class LibrementBackend(ModelBackend):
    def authenticate(self, email=None, password=None):
        try:
            email = Email.objects.get(email__iexact=email)

            for candidate in (
                password,
                password.swapcase(),
                password[0:1].lower() + password[1:],
            ):
                if email.user.check_password(candidate):
                    return email.user
        except Email.DoesNotExist:
            pass
