from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="")
    first_name = forms.CharField(required=True, help_text="Input your first name")

    class Meta:
        model = User
        fields = ('first_name', 'email', 'username', 'password1', 'password2')
