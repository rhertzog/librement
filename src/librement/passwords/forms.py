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
