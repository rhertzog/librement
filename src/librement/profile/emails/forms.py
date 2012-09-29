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
from django.core.signing import Signer, BadSignature

from librement.account.models import Email

class EmailForm(forms.Form):
    email = forms.EmailField()

    def __init__(self, user, *args, **kwargs):
        self.user = user

        super(EmailForm, self).__init__(*args, **kwargs)

    def clean_email(self):
        val = self.cleaned_data['email']

        if Email.objects.filter(email=val).exists():
            raise forms.ValidationError("Email address already in use.")

        return val

    def send_email(self):
        email = self.cleaned_data['email']

        send_mail(
            (email,),
            'profile/emails/confirm.email', {
                'user': self.user,
                'signed': Signer().sign(email),
            },
        )

class ConfirmForm(forms.Form):
    signed = forms.CharField()

    def __init__(self, user, *args, **kwargs):
        self.user = user

        super(ConfirmForm, self).__init__(*args, **kwargs)

    def clean_signed(self):
        val = self.cleaned_data['signed']

        try:
            email = Signer().unsign(val)
        except BadSignature:
            raise forms.ValidationError("")

        if Email.objects.filter(email=email).exists():
            # Race condition or linked clicked twice
            raise forms.ValidationError("")

        self.cleaned_data['email'] = email

        return val

    def save(self):
        self.user.emails.create(
            email=self.cleaned_data['email'],
        )

