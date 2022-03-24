from django import forms
from django.forms.widgets import TextInput, NumberInput, EmailInput, Textarea
from .models import ContactRequest

# Your forms here.
class ContactForm(forms.ModelForm):
    # name = forms.CharField(error_messages={'required': 'This field is required'})
    # email = forms.CharField(error_messages={'required': 'This field is required'})
    # phone = forms.CharField(error_messages={'required': 'This field is required'})
    # message = forms.CharField(error_messages={'required': 'This field is required'})

    class Meta:
        model = ContactRequest
        fields = [
            'name',
            'email',
            'phone',
            'message'
        ]

        required = [
            'name',
            'email',
            'phone',
            'message'
        ]


        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'name',
                    'placeholder': 'Your name'
                }
            ),

            'email': EmailInput(
                attrs={
                    'class': 'form-control',
                    'id': 'email',
                    'placeholder': 'Your Email'
                }
            ),

            'phone': NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'phone',
                    'placeholder': 'Your Phone'
                }
            ),

            'message': Textarea(
                attrs={
                    'class': 'form-control',
                    'id': 'message',
                    'placeholder': 'Your Message'
                }
            ),
        }