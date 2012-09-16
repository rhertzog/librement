from django.db import models

from django_enumfield import EnumField

from librement.utils.user_data import PerUserData

from .enums import AccountEnum, CountryEnum

class Profile(PerUserData('profile')):
    account_type = EnumField(AccountEnum)

    country = EnumField(CountryEnum)
