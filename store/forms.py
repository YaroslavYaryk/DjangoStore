from django import forms

class CouponForm(forms.Form):

    coupon = forms.CharField(label='Coupon', max_length=100)