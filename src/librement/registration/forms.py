from django import forms
from django.contrib.auth.models import User

from librement.profile.enums import AccountEnum

from librement.profile.models import Profile

class RegistrationForm(forms.ModelForm):
    email = forms.EmailField()

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

    def clean_organisation(self):
        val = self.cleaned_data['organisation']

        account_type = self.cleaned_data.get('account_type')

        if account_type != AccountEnum.INDIVIDUAL and val == '':
            raise forms.ValidationError(
                "Required field for company/non-profit accounts"
            )

        return val

    def save(self):
        user = User.objects.create_user(
            username='FIXME',
            password=self.cleaned_data['password'],
        )

        return user
