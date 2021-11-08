from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from store.models import ProductComment


class CouponForm(forms.Form):

    coupon = forms.CharField(label='Coupon', max_length=100)


class RegisterUserForm(UserCreationForm):
    """ Registrating form class """

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}))
    # captcha = CaptchaField(label='Solve next conundrum',
    #                        error_messages={'invalid': 'Wrong answer'})

    class Meta:
        model = User

        fields = ( "first_name", "last_name", "username",
                  "email", "password1", "password2",)
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }

class LoginUserForm(AuthenticationForm):
    """ Login form class """

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}))
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = User

        fields = ("username", "password",)


class ProductCommentForm(forms.ModelForm):
    """Leaving comment form"""

    comment = forms.CharField(label="Comment", widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "cols": 30,
            "rows": 5})
    )

    class Meta:
        model = ProductComment

        fields = ("comment",)

