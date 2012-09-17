from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=30)
    password = forms.CharField()

    def clean(self):
        user = None
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)

        if user is None:
            raise forms.ValidationError(
                "Please enter a correct username and password."
            )

        if not user.is_active:
            raise forms.ValidationError("This account is not active.")

        self.cleaned_data['user'] = user

        return self.cleaned_data
