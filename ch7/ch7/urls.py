"""
URL configuration for ch7 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
# from app1 import views as ap1
# from app2 import views as ap2

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', ap1.home, name='home'),
#     path('app1/', ap1.myapp1, name='myapp1'),
#     path('app2/', ap2.myapp2, name='myapp2'),
#     path('app3/', ap2.myapp3, name='myapp3'),
# ]


#  OR


from django.contrib import admin
from django.urls import path
from app1.views import  home, myapp1
from app2.views import  myapp2, myapp3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('app1/', myapp1, name='myapp1'),
    path('app2/', myapp2, name='myapp2'),
    path('app3/', myapp3, name='myapp3'),
]