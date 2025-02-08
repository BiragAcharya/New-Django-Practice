from django import forms

# #Clean and Validate  Field Specific
# class Registration(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)

#     def clean_name(self):
#         # name_value = self.cleaned_data.get('name')
#         name_value = self.cleaned_data['name']
#         if len(name_value) < 3:
#             raise forms.ValidationError('Enter more than or equal 3 char')
#         return name_value
    

#     def clean_email(self):
#         email_value = self.cleaned_data['email']
#         if len(email_value) < 16:
#             raise forms.ValidationError('Enter more than or equal 16 char')
#         return email_value
    


#Clean and Validate Django Form all at once
class Registration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        name_value = cleaned_data.get('name')
        email_value = cleaned_data.get('email')

        if name_value and len(name_value) < 3:
            self.add_error('name', 'Enter more than or equal to 3 characters')

        if email_value and len(email_value) < 16:
            self.add_error('email', 'Enter more than or equal to 16 characters')
        
        return cleaned_data