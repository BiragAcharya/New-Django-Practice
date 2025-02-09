from django import forms

# class Registration(forms.Form):
#     name = forms.CharField(error_messages=
#                            {'required': 'Name is required'},
#                             min_length=3, max_length=50)
    
#     email = forms.EmailField(error_messages=
#                              {'required': 'Email is required'},
#                                min_length=5, max_length=50)
    
#     password = forms.CharField(error_messages=
#                                {'required': 'Password is required'},
#                                  widget=forms.PasswordInput,
#                                    min_length=8, max_length=50)


from student.models import Profile

class Registration(forms.ModelForm):
    name= forms.CharField(max_length=50, required=False)
    confirm_password = forms.CharField()

    class Meta:
        model = Profile
        fields=['name', 'email',  'password']
        labels = {'name': 'Enter Name', 'email': 'Enter Email'}
        error_messages = {
            'email':{'required': 'Email is required'}
        }
        widgets ={
            'password': forms.PasswordInput(attrs={'class':'pwdclass'}),
            'name': forms.TextInput(attrs={'class':'myclass', 'placeholder': 'Yaha name lekh'})
        }
    
   