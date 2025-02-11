
from django.urls import path
from school.views import student_form_view, teacher_form_view

urlpatterns = [
    path('s/', student_form_view, name='student_form_view'),
    path('t/', teacher_form_view, name='teacher_form_view'),

]
