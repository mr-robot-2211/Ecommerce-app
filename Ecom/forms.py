from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db import models
from .models import Post

PAYMENT_CHOICES={
    ('P', 'PayPal')
}

class Review(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['reviews']
 
class addmoney(forms.Form):
    money=forms.IntegerField() 
        
class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(required=False)
    shipping_zip = forms.CharField(required=False)

    billing_address = forms.CharField(required=False)
    billing_zip = forms.CharField(required=False)

    same_billing_address = forms.BooleanField(required=False)
    set_default_shipping = forms.BooleanField(required=False)
    use_default_shipping = forms.BooleanField(required=False)
    set_default_billing = forms.BooleanField(required=False)
    use_default_billing = forms.BooleanField(required=False)

    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)

class PaymentForm(forms.Form):
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)
