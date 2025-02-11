from django.shortcuts import render
from student.forms import Registration
from django.http import HttpResponseRedirect
from student.models import Profile

# def register(request):
#     if request.method == 'POST':
#         form = Registration(request.POST)
#         if form.is_valid():

#             nm = form.cleaned_data['name']
#             em = form.cleaned_data['email']
#             pw = form.cleaned_data['password']
#             cpw = form.cleaned_data['confirm_password']

#             print('Name:', nm)
#             print('Email:', em)
#             print('Password:', pw)
#             print('Confirm Password:', cpw)

#             # #Syntax:- save(commit=False/True


#             # #Saving data into database)
#             # pr = Profile(name=nm, email=em, password=pw)
#             # pr.save()

#             # #Update data from database)
#             # pr = Profile(id=1, name=nm, email=em, password=pw)
#             # pr.save()

#             # #Delete data from database
#             # pr = Profile(id=1)
#             # pr.delete()


#             return HttpResponseRedirect('/student/register/')



# By another way
def register(request):
    if request.method == 'POST':
        obj= Profile.objects.get(id=2)
        form = Registration(request.POST, instance=obj)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/student/register/')

    else:
        form = Registration()
    return render(request, 'student/register.html', {'form': form})
