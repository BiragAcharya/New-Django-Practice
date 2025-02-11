from django.shortcuts import render
from school.forms import StudentRegistration, TeacherRegistration

def student_form_view(req):
    if req.method == 'POST':
        form = StudentRegistration(req.POST)
        if form.is_valid():
            form.save()
    else:
        form =StudentRegistration()
    return render(req, 'school/studentreg.html', {'form':form})


def teacher_form_view(req):
    if req.method == 'POST':
        form = TeacherRegistration(req.POST)
        if form.is_valid():
            form.save()
    else:
        form =TeacherRegistration()
    return render(req, 'school/teacherreg.html', {'form':form})
