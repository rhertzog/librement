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

class AccountForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'organisation',
            'address_1',
            'address_2',
            'city',
            'region',
            'zipcode',
            'country',
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

class PasswordForm(forms.Form):
    password_old = forms.CharField()
    password = forms.CharField()
    password_confirm = forms.CharField()

    def __init__(self, user, *args, **kwargs):
        self.user = user

        super(PasswordForm, self).__init__(*args, **kwargs)

    def save(self):
        self.user.set_password(self.cleaned_data['password'])
        self.user.save()

    def clean_password_old(self):
        val = self.cleaned_data['password_old']

        if not self.user.check_password(val):
            raise forms.ValidationError(
                "Password is not correct."
            )

        return val

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password', '')
        password_confirm = self.cleaned_data['password_confirm']

        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")

        if len(password) < 8:
            raise forms.ValidationError(
                "Password must be at least 8 characters"
            )

        return password
