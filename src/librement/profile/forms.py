from django import forms
from django.contrib.auth.models import User

from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'display_name',
            'biography',
        )

class URLForm(forms.ModelForm):
    username = forms.RegexField(regex=r'^[\w-]+$')

    class Meta:
        model = User
        fields = (
            'username',
        )
