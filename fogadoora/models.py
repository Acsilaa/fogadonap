from django.db import models
from django.contrib.auth import User

class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    first = models.IntegerField()
    last = models.IntegerField()

# class Person():
#     name = models.CharField(max_length=50)

# class Parent(Person, models.Model):
#     child = models.CharField() #mert több gyermeke is lehet

# class Student(Person, models.Model):
#     clazz = models.CharField(max_length=4)
#     parent = models.IntegerField()


# class Formteacher(Person, models.Model):
#     clazz = models.CharField(max_length=4)

# class Classes(models.Model):
#     pass

# class Appointments(models.Model):
#     pass

# class TeachingInClass(models.Model):
#     pass

