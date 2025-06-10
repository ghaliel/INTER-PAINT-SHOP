from django import forms
from .models import Order
from django.contrib.auth.forms import UserCreationForm

class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['shipping_address', 'shipping_city', 'shipping_postal_code', 'shipping_country']
        labels = {
            'shipping_address': 'Adresse',
            'shipping_city': 'Ville',
            'shipping_postal_code': 'Code Postal',
            'shipping_country': 'Pays',
        }

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Adresse e-mail', required=True)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',) 