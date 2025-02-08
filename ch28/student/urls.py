from django.urls import path
from student.views import registration, address, login

urlpatterns = [
    path('register/', registration, name='registration'),
    path('address/', address, name='address'),
    path('login/', login, name='login'),


]
