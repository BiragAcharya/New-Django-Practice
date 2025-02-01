from django.shortcuts import render

def learn_django(req):
    return render(req, 'course/django.html', {"name": "Django 5.x"})


def learn_python(req):
    return render(req, 'course/python.html')
