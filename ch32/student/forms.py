from django import forms
from django.core import validators

def starts_with_s(value):
    if value[0] != 's':
        raise forms.ValidationError("Email should starts with s")


class Registration(forms.Form):
    #Built-In Validators
    name = forms.CharField(validators=[validators.MinLengthValidator(3),
                                       validators.MaxLengthValidator(15)
                                    ])
    
    #Custom Validators
    email = forms.EmailField(validators=[starts_with_s])
    password = forms.CharField(widget=forms.PasswordInput)

   