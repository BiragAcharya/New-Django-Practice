from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=256)
    city = models.CharField(max_length=71)