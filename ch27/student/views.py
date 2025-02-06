from django.shortcuts import render
from student.forms import Registration, Login

def registration(req):
    fm = Registration()
    return render(req, 'student/registration.html', {'form': fm})


def login(req):
    ln = Login()
    return render(req, 'student/login.html', {'form': ln})