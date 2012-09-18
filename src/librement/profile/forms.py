from django import forms
from django.contrib.auth.models import User

from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'display_name',
            'biography',
            'rss_url',
        )

class URLForm(forms.ModelForm):
    username = forms.RegexField(regex=r'^[\w-]+$')

    class Meta:
        model = User
        fields = (
            'username',
        )

class PictureForm(forms.Form):
    picture = forms.ImageField()

    def __init__(self, user, *args, **kwargs):
        self.user = user

        super(PictureForm, self).__init__(*args, **kwargs)

    def save(self):
        self.user.profile.picture.save(
            self.cleaned_data['picture']
        )
        self.user.profile.save()
