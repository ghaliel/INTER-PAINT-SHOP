from django import forms
from .models import Order, UserProfile, StaffPlanning
from django.contrib.auth.forms import UserCreationForm

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Nom complet',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Votre nom complet'
        })
    )
    email = forms.EmailField(
        label='Adresse email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'votre.email@exemple.com'
        })
    )
    subject = forms.CharField(max_length=200)
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Votre message...'
        })
    )

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

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['address', 'city', 'postal_code', 'country', 'phone_number']

class StaffPlanningForm(forms.ModelForm):
    class Meta:
        model = StaffPlanning
        fields = ['date', 'start_time', 'end_time', 'task_description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
            'task_description': forms.Textarea(attrs={'rows': 3}),
        } 