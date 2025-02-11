from django.contrib import admin
from student.models import Profile

# admin.site.register(Profile)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','email', 'password')


# admin.site.register(Profile)
