from django_yadt import YADTImageField
from django_enumfield import EnumField

from django.db import models

from librement.utils.user_data import PerUserData

from .enums import AccountEnum, CountryEnum

class Profile(PerUserData('profile')):
    account_type = EnumField(AccountEnum, default=AccountEnum.INDIVIDUAL)

    biography = models.TextField()
    display_name = models.CharField(max_length=100)

    organisation = models.CharField(max_length=100, blank=True)

    address_1 = models.CharField(max_length=150, blank=True)
    address_2 = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)
    zipcode = models.CharField(max_length=100, blank=True)

    country = EnumField(CountryEnum, default=CountryEnum.US)

    picture = YADTImageField(variants={
        'thumbnail': {
            'width': 150,
            'height': 150,
            'format': 'jpeg',
            'crop': True,
        },
    }, cachebust=True)

    rss_url = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.display_name
