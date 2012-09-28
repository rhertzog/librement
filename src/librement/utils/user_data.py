# Copyright 2012 The Librement Developers
#
# See the AUTHORS file at the top-level directory of this distribution
# and at http://librement.net/copyright/
#
# This file is part of Librement. It is subject to the license terms in
# the LICENSE file found in the top-level directory of this distribution
# and at http://librement.net/license/. No part of Librement, including
# this file, may be copied, modified, propagated, or distributed except
# according to the terms contained in the LICENSE file.

from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User

def PerUserData(related_name=None):
    """
    Class factory that returns an abstract model attached to a ``User`` object
    that creates and destroys concrete child instances where required.

    Example usage::

        class ToppingPreferences(PerUserData('toppings')):
            pepperoni = models.BooleanField(default=True)
            anchovies = models.BooleanField(default=False)

        >>> u = User.objects.create_user('test', 'example@example.com')
        >>> u.toppings  # ToppingPreferences created automatically
        <ToppingPreferences: user=test>
        >>> u.toppings.anchovies
        False
    """

    class UserDataBase(models.base.ModelBase):
        def __new__(cls, name, bases, attrs):
            model = super(UserDataBase, cls).__new__(cls, name, bases, attrs)

            if model._meta.abstract:
                return model

            def on_create(sender, instance, created, *args, **kwargs):
                if created:
                    model.objects.create(user=instance)

            def on_delete(sender, instance, *args, **kwargs):
                model.objects.filter(pk=instance).delete()

            post_save.connect(on_create, sender=User, weak=False)
            pre_delete.connect(on_delete, sender=User, weak=False)

            return model

    class UserData(models.Model):
        user = models.OneToOneField(
            'auth.User',
            primary_key=True,
            related_name=related_name,
        )

        __metaclass__ = UserDataBase

        class Meta:
            abstract = True

        def __unicode__(self):
            return 'user=%s' % self.user.username

    return UserData
