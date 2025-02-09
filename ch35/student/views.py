from django.shortcuts import render
from student.forms import Registration
from django.http import HttpResponseRedirect
from student.models import Profile

def register(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():

            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pw = form.cleaned_data['password']

            print('Name:', nm)
            print('Email:', em)
            print('Password:', pw)

            return HttpResponseRedirect('/student/register/')
    else:
        form = Registration()
    return render(request, 'student/register.html', {'form': form})
