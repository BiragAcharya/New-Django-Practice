from django.shortcuts import render
from student.forms import Registration, Login

def registration(req):
    # fm = Registration(field_order=['email', 'city'])      #orders the form attributes! if constructor is not commented, them it wont be applied, constuctor will be called
    fm = Registration()
    return render(req, 'student/registration.html', {'form': fm})


def login(req):
    # fm = Login(auto_id='sonam_%s')
    # fm = Login(auto_id=True)
    
    # fm = Login(label_suffix='=')

    # fm = Login(initial={'email':'sonam@example.com',
    #                     'password': '12345'})


    #Implementing above all at once
    # fm = Login(auto_id='sonam_%s', label_suffix='=', initial={'email':'sonam@example.com',
    #                     'password': '12345'})
    

    fm = Login()
    return render(req, 'student/login.html', {'form': fm})