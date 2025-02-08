from django import forms
from django.core.validators import MinLengthValidator, RegexValidator


# class DemoForm(forms.Form):
#     # Basic Fields
#     name = forms.CharField()
#     email = forms.EmailField()
#     pin_code = forms.IntegerField()


#     #Additional Fields Types
#     age = forms.FloatField()
#     date_of_birth = forms.DateField()
#     appointment_time = forms.TimeField()
#     appointment_datetime = forms.DateTimeField()
#     is_subscribed = forms.BooleanField()
#     agree_terms = forms.NullBooleanField()


#     # #Choice Field
#     # gender = forms.ChoiceField(choices=[('M', 'Male'),
#     #                                     ('F', 'Female'),
#     #                                     ('O', 'Others')])

#     #Field Type Examples
#     GENDER_CHOICES = [
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('O', 'Other')
#     ]

#     #Choice Field
#     gender = forms.ChoiceField(choices=GENDER_CHOICES)

#     interests = forms.MultipleChoiceField(choices=[('tech', 'Technology'),
#                                                    ('art', 'Art'), 
#                                                    ('sports', 'Sports')])
    
#     #File and Url Fields
#     profile_image = forms.ImageField()
#     resume = forms.FileField()
#     website = forms.URLField()

#     #Other Specialized Fields
#     phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$')
#     password = forms.CharField(widget=forms.PasswordInput())
#     slug = forms.SlugField()
#     ip_address = forms.GenericIPAddressField()
#     rating = forms.DecimalField()






    #Fields Argument Example

# class DemoForm(forms.Form):
#     # Basic Fields
#     name = forms.CharField(
#         label="Full Name",                           #Sets label displayed next to the field
#         max_length=100,                              #Limits input length to 100 characters
#         label_suffix=':',                            #Sets the suffix after the label (default is ':')
#         initial="Enter your full name",              #Sets an initial placeholder value
#         help_text = "Enter ypur legal name here",    #Provides guidance for the user
#         validators=[MinLengthValidator(3)]           #Validates that input has at least 3 characters
#     )
#     email = forms.EmailField(
#         label="Email Address",                       #Set a user-friendly label for thisemail field
#         disabled=True,                               #Disables field input (useful for readonly fields)
#     )
#     pin_code = forms.IntegerField(
#         label="Pin Code",                            #Sets the field label
#         min_value=100000,                            #Ensures minimum value is 100000
#         max_value=999999,                            #Ensures maximum value is 999999
#         error_messages={
#               'min_value': "Pin code must be at least 6 digits.",
#               'max_value': "Pin code cannot be more than 6 digits."
# }
# )
#     #Additional Fields Types
#     age = forms.FloatField(
#         label="Age",                                 #Sets the label for the age field
#         min_value=0                                  #Ensures a non-negative age
#     )
#     date_of_birth = forms.DateField(
#         label="Date of Birth",                       #Sets label for date field
#         required=False,                              #Field is optional
#         help_text="Enter your birth date in YYYY-MM-DD format"          #Guidance text 
#     )
#     appointment_time = forms.TimeField(
#         label="Appointment Time",                    #Sets label for time field
#         required=False                               #Field is optional
#     )
#     appointment_datetime = forms.DateTimeField(
#         label="Appointment Date and Time",           #Sets label for datetime field
#         required=False                               #Field is optional
#     )
#     is_subscribed = forms.BooleanField(
#         label="Subscribe to Newsletter",             #Sets label for boolean field
#         required=False                               #Field is optional
#     )
#     agree_terms = forms.NullBooleanField(
#         label="Do you agree with terms",             #Sets label for a three-state boolean field
#     )


#     #Field Type Examples
#     GENDER_CHOICES = [
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('O', 'Other')
#     ]

#     #Choice Field
#     gender = forms.ChoiceField(
#         label="Gender",                              #Sets label for gender field
#         choices=GENDER_CHOICES      
#     )

#     #Field Type Examples
#     INTEREST_CHOICES = [('tech', 'Technology'),
#                  ('art', 'Art'), 
#                  ('sports', 'Sports')]

#     #Interest Field
#     interests = forms.MultipleChoiceField(
#         label="Interests",                           #Sets label for multiple-choice field
#         choices=INTEREST_CHOICES,
#         required=False                               #Field is optional
#     )
    
#     #File and Url Fields
#     profile_image = forms.ImageField(
#         label="Profie Image",                        #Sets label for image upload
#         required=False                               #Field is optional
#     )
#     resume = forms.FileField(
#         label="Upload Resume",                        #Sets label for file upload
#         required=False                                #Field is optional
#     )
#     website = forms.URLField(
#         label="Profie Image",                        #Sets label for URL field
#         required=False                               #Field is optional
#     )

#     #Other Specialized Fields
#     phone_number = forms.RegexField(
#         label="Phone Number",                        #Sets label for Phone Number
#         regex=r'^\+?1?\d{9,15}$',                    #Regex pattern ensures valid phone format
#         error_messages={                             #Custom error message if regex fails
#             'invalid': 'Enter a valid phone number, e.g, +123456789.'
#         })                    
#     password = forms.CharField(
#         label="Password",                            #Sets label for Password
#         max_length=50,                               #Limits input to 50 characters
#         widget=forms.PasswordInput(),                #Masks input for password security
#         validators=[MinLengthValidator(8)],          #Minimum length validation for password
#         error_messages={                             #Custom error
#             'min_length': 'Password must be at least 8 characters long'}    
#         ),               
#     slug = forms.SlugField(
#         label="Slug",                                #Sets label for slug field
#         max_length=50                                #Limits input to 50 characters
#     )
#     ip_address = forms.GenericIPAddressField(
#         label="IP Address",                          #Sets label for IP Address
#         protocol='both',                             #Allows for both IPv4 and IPv6 addresses
#         unpack_ipv4=False,                           #Maintains IPv4 addresses in standard form
#         localize=True,                               #Formsts the IP address according to locate
#     )
#     rating = forms.DecimalField(
#         label="Rating",                             #Sets label for decimal field
#         max_digits=3,                               #Allows upto 3 digits, e.g. 9.5
#         decimal_places=1,                           #Specifies 1 decimal place for rating
#         min_value=0,                                #Sets minimum allowed value
#         max_value=10,                               #Sets maximum allowed value
#         initial=5.0,                                #Sets an initial rating value
#         help_text="Provide a rating between 0 and 10",  
#         localize=True                               #Localizes the number format based on user locale
#     )







#Widget Example

class DemoForm(forms.Form):
    # Text Input Widgets
    name = forms.CharField(
        #Basic tect input widget
        widget=forms.TextInput(attrs={'placeholder':'Type here....', 'class': 'mycss'}),
    )
    password = forms.CharField(
       widget=forms.PasswordInput(
            attrs={'placeholder':'Enter Password'})                    #Password Widget
    )
    key = forms.CharField(
        #Hidden input widget for storing non-visible data
       widget=forms.HiddenInput()                                      #Password Widget
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder':'name@example.com'})                  #Email widget             #Password Widget                         #Disables field input (useful for readonly fields)
    )
    URL = forms.URLField(
        widget=forms.URLInput(
            attrs={'placeholder':'https://example.com'})                  #URL widget             #Password Widget                         #Disables field input (useful for readonly fields)
    )
    pin_code = forms.IntegerField(
        #Number input with min/max attributes
        widget=forms.NumberInput(attrs={'min':'0', 'max': '100'})                  #URL widget             #Password Widget                          #Disables field input (useful for readonly fields)
    )
    DOB = forms.DateField(
        #Date time wdget with place holder
        widget=forms.DateInput(attrs={'type':'date',"placeholder": 'YYYY-MM-DD'})                  #URL widget             #Password Widget                         #Disables field input (useful for readonly fields)
    )
    meeting_time = forms.TimeField(
        #Time widget with placeholder
        widget=forms.TimeInput(attrs={'type':'time',"placeholder": 'HH-MM-SS'})                  #URL widget             #Password Widget                         #Disables field input (useful for readonly fields)
    )
    datetime_field = forms.DateTimeField(
        #DateTime widget for both date and time
        widget=forms.DateTimeInput(attrs={'type':'datetime-local',"placeholder": 'YYYY-MM-DD HH:MM:SS'})                  #URL widget             #Password Widget                         #Disables field input (useful for readonly fields)
    )
    description = forms.CharField(
        #Textarea widget
        widget=forms.Textarea(attrs={"placeholder": 'Enter multiple lines of text....'})                  #URL widget             #Password Widget                         #Disables field input (useful for readonly fields)
    )
    boolean_field = forms.BooleanField(
        #Checkbox widget
        widget=forms.CheckboxInput()
    )
    null_boolean_field = forms.NullBooleanField(
        #Dropdown with Yes, No, Wnknown options
        widget=forms.NullBooleanSelect()
    )

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    choice_field = forms.ChoiceField(
        # dropdown
        choices=GENDER_CHOICES,
        widget=forms.Select()
    )

    INTEREST_CHOICES = [('tech', 'Technology'),
        ('art', 'Art'), 
        ('sports', 'Sports')
    ]
    multiple_choice_field = forms.MultipleChoiceField(
        # dropdown
        choices=INTEREST_CHOICES,
        widget=forms.SelectMultiple()
    )
    radio_choice_field = forms.ChoiceField(
        #radio buttons
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect()
    )
    
    file_field = forms.FileField(
        widget=forms.FileInput()
    )
    image_field = forms.ImageField(
        widget=forms.ClearableFileInput()
    )
    slug_field = forms.SlugField(
         widget=forms.TextInput(attrs={'placeholder':'my-slug'})
    )
    ip_address_field = forms.GenericIPAddressField(
         widget=forms.TextInput(attrs={'placeholder':'127.0.0.1'})
    )
    time_duration_field = forms.DurationField(
         widget=forms.TextInput(attrs={'placeholder':'hh:mm:ss'})
    )
    decimal_field = forms.DecimalField(
        label="Decimal Field",
        max_digits=5,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'step':'0.1'})
    )
    split_date_time = forms.SplitDateTimeField(
        label="Split Date and Time Field",
        #Widget that provides two fields for date and time
        widget=forms.SplitDateTimeWidget()
    )
    split_hidden_date_time = forms.SplitDateTimeField(
        label="Hidden DateTime Field",
        #Hidden widget for split datetime
        widget=forms.SplitHiddenDateTimeWidget()
    )
    