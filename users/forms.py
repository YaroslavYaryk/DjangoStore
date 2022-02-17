from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.conf import settings
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    """ Registrating form class """

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User

        fields = ("first_name", "last_name",
                  "email", "password1", "password2",)
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }


class LoginUserForm(AuthenticationForm):
    """ Login form class """

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}))
    email = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = User

        fields = ("email", "password",)
