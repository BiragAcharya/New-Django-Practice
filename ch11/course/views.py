from django.shortcuts import render

# Create your views here.
def learn_django(req):
    # return render(req, template_name, context=dic_name, 
    #               context_type=MIME_TYPE, status=None, using=None)

    coursename = {'cname': 'Django 3'}    #dictionary making
    return render(req, 'course/django.html', context=coursename)  #context nalekhda pani huncha

        # OR

    # return render(req, 'course/django.html', {'cname': 'Django 3'})


def learn_fastapi(req):
    seats = 10
    coursedetails ={
        'cName': 'Fast Api', 
        'version':' 3.0', 
        'st': seats}  #seats is variable not value, so no inverted comma
    return render(req, 'course/fastapi.html', coursedetails)