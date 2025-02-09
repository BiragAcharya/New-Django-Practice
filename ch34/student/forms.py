from django import forms

class Registration(forms.Form):
    name = forms.CharField(error_messages={'required': 'Name is required'}, min_length=3, max_length=50)
    email = forms.EmailField(error_messages={'required': 'Email is required'}, min_length=5, max_length=50)
    password = forms.CharField(error_messages={'required': 'Password is required'} , widget=forms.PasswordInput, min_length=8, max_length=50)

   