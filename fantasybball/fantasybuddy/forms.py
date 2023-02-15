from django import forms


class AuthCodeForm(forms.Form):
    auth_code = forms.CharField(
        help_text="Enter your authentication code.", min_length=7, max_length=7
    )
