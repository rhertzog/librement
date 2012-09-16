from django_enumfield import EnumField

from librement.utils.user_data import PerUserData

from .enums import CountryEnum

class Profile(PerUserData('profile')):
    country = EnumField(CountryEnum)
