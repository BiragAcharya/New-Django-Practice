from django.shortcuts import render
from datetime import datetime

# # Example 1.1 - Variable
# def learn_django(req):
#     return render(req, 'course/django.html', context= {'name': 'Django'})


# # Example 1.2 - Variable
# def learn_django(req):
#     name = 'Django'
#     duration = '4 months'
#     seats = 10
#     course_details = {'nm': name, 'du': duration, 'st': seats}
#     return render(req, 'course/django.html', course_details)



#Example 2 - Filter
# def learn_django(req):
#     return render(req, 'course/django.html', context= {'name': 'Django', 'desc': 'Django is a awesome web framework'})



# # Example 3 - Date and Time
# def learn_django(req):
#     d = datetime.now()
#     return render(req, 'course/django.html', context= {'dt':d})



# # Example 4 - Float Format
# def learn_django(req):
#     return render(req, 'course/django.html', context= {'p1': 56.24321, 'p2': 56.000, 'p3': 56.37000})



# # Example 5.1 - If Tag
# def learn_django(req):
#     return render(req, 'course/django.html', context= {'nm': True})



# # Example 5.2 - If Tag
# def learn_django(req):
#     return render(req, 'course/django.html', context= {'nm': 'Django'})


# # Example 5.3 - If Tag
# def learn_django(req):
#     return render(req, 'course/django.html', context= {'nm': 'Django', 'st':5})


# # Example 6 - For Loop Tag
# def learn_django(req):
#     student = {'names': ['Rahul', 'Sonam', 'Raj','Anu']}
#     return render(req, 'course/django.html', student)


# # Example 7
# def learn_django(req):
#     stu = {'stu1': {'name': 'Rahul', 'roll':101},
#            'stu2': {'name': 'Sonam', 'roll':102},
#            'stu3': {'name': 'Raj', 'roll':103},
#            'stu4': {'name': 'Anu', 'roll':104}
#            }
    
#     students = {'student':stu}
#     return render(req, 'course/django.html', students)



# Example 8
def learn_django(req):
    student = {'name': 'Rahul', 'roll':101}
    return render(req, 'course/django.html', {'student': student})



# Example 9
def learn_django(req):
    student = {'stu1': {'name': 'Rahul', 'roll':101},
                'stu2': {'name': 'Sonam', 'roll':102},
                'stu3': {'name': 'Raj', 'roll':103},
                'stu4': {'name': 'Anu', 'roll':104}
                }
    return render(req, 'course/django.html', {'student': student})
