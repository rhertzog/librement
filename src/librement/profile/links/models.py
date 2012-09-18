from django.db import models

class Link(models.Model):
    user = models.ForeignKey('auth.User', related_name='links')

    url = models.URLField()
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return u"%s <%s>" % (self.title, self.url)
