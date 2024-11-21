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


class LoginForm(forms.Form):
    """ Class Validating Login Data"""

    ## Password Settings
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


