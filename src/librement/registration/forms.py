from django import forms
from django.contrib.auth.models import User

from librement.profile.models import Profile

class RegistrationForm(forms.ModelForm):
    password = forms.CharField()
    password_confirm = forms.CharField()

    class Meta:
        model = Profile
        fields = (
            'account_type',
            'organisation',
            'address_1',
            'address_2',
            'city',
            'region',
            'zipcode',
            'country',
        )

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password', '')
        password_confirm = self.cleaned_data['password_confirm']

        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")

        return password

    def save(self):
        user = User.objects.create_user(
            username='FIXME',
            password=self.cleaned_data['password'],
        )

        return user
