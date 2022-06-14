from logging import PlaceHolder
from django import forms
from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'address')
        labels = {
            'name': '',
            'email': '',
            'phone': '',
            'address': ''
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'PlaceHolder': 'Please Enter Your Name Here'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'PlaceHolder': 'Please Enter Your E-mail Here'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'PlaceHolder': 'Please Enter Your Phone Number Here'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'PlaceHolder': 'Please Enter Your Address Here'})
        }
