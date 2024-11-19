from .models import User
from django import  forms
from django.forms import ModelForm

class SignUpForm(ModelForm):
    """ Class Validaing Sign up Data """
    password = forms.CharField(
        widget=forms.PasswordInput(),
        required=True
    )

    class Meta:
        model = User
        fields = ["name", "email", "phone", "password"]


class LoginForm(ModelForm):
    """ Class Validating Login Data"""

    ## Password Settings
    password = forms.CharField(
        widget=forms.PasswordInput(),
        required=True
    )

    class Meta:
        model = User
        fields = ["email", "password"]