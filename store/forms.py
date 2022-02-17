from django import forms


from store.models import ProductComment


class CouponForm(forms.Form):

    coupon = forms.CharField(label='Coupon', max_length=100)


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
