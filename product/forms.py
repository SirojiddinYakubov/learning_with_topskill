from django import forms
from django.forms import TextInput, EmailInput

from product.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                # 'style': 'max-width: 300px;',
                'placeholder': 'Name'
            }),
            'email': EmailInput(attrs={
                'class': "form-control",
                # 'style': 'max-width: 300px;',
                'placeholder': 'Email'
            }),
            'phone': TextInput(attrs={
                'class': "form-control",
                # 'style': 'max-width: 300px;',
                'placeholder': 'Phone'
            }),
            'message': TextInput(attrs={
                'class': "form-control",
                # 'style': 'max-width: 300px;',
                'placeholder': 'Message'
            }),
        }
