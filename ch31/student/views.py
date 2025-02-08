from django.shortcuts import render
from student.forms import Registration
from django.http import HttpResponseRedirect

def register(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print("Hello--------------")

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print('Name:', name)
            print('Email:', email)
            print('Password:', password)
            return HttpResponseRedirect('/student/register/')
    else:
        form = Registration()
    return render(request, 'student/register.html', {'form': form})
