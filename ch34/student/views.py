from django.shortcuts import render
from student.forms import Registration
from django.http import HttpResponseRedirect
from student.models import Profile

def register(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print("Hello--------------")

            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pw = form.cleaned_data['password']

            # # Save data into database
            # user = Profile(name = nm, email=em, password=pw)
            # user.save()

            # Update data into database
            user = Profile(id=1, name = nm, email=em, password=pw)
            user.save()

            # Delete data from database
            user = Profile(id=1)
            user.delete()


            return HttpResponseRedirect('/student/register/')
    else:
        form = Registration()
    return render(request, 'student/register.html', {'form': form})
