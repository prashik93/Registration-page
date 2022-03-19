from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Registration(models.Model):
    name = models.CharField(max_length=23)
    dob = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    gender = models.CharField(max_length=12)
    flat = models.IntegerField()
    street = models.CharField(max_length=45)
    country = models.CharField(max_length=12)
    img = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name