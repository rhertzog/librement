from django.db import models

class Email(models.Model):
    user = models.ForeignKey('auth.User', related_name='emails')

    email = models.EmailField(unique=True)

    def __unicode__(self):
        return u"%s" % self.email
