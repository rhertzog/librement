from local import *

# Django's tests require the use of the standard ModelBackend
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)

# Don't use bcrypt to run tests
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.SHA1PasswordHasher',
)

