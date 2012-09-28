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

from email_from_template import send_mail

from django import forms

from librement.account.models import Email

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        val = self.cleaned_data['email']

        try:
            return Email.objects.get(
                email=val,
                user__is_active=True,
            )
        except Email.DoesNotExist:
            raise forms.ValidationError(
                "That email address does not exist."
            )

    def save(self):
        email = self.cleaned_data['email']

        send_mail(
            (email.email,),
            'passwords/forgot_password.email',
            {'user': email.user},
        )

class ResetPasswordForm(forms.Form):
    password = forms.CharField(required=False)
    password_confirm = forms.CharField(required=False)

    def __init__(self, user, *args, **kwargs):
        self.user = user

        super(ResetPasswordForm, self).__init__(*args, **kwargs)

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

    def save(self):
        self.user.set_password(self.cleaned_data['password'])
        self.user.save()
