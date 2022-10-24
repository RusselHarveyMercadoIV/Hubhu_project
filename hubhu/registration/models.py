from django.db import models

# Create your models here.

class User(models.Model):
    type_user = (('D', 'Default'), ('A', 'Admin'))
    username = models.CharField(max_length=25, primary_key=True)
    password = models.CharField(max_length=25)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    birthday = models.DateField()
    profile_pic = models.ImageField()
    type = models.CharField(max_length=1, choices = type_user)


class Default(User):
    mobile_number = models.IntegerField()


class Admin(User):
    privilege_level = models.IntegerField(default = 0)


