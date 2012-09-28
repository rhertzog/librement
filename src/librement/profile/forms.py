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
