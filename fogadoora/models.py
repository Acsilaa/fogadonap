from django.db import models
from django.contrib.auth.models import User

class defuser(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    group = models.IntegerField()

class ClassificationAsText(models.Model):
    classification = models.CharField(max_length=20)

class Teacher(models.Model):
    userID = models.IntegerField()

class TeacheableSubjects(models.Model):
    teacher = models.IntegerField()
    english = models.BooleanField(default=0)
    german = models.BooleanField(default=0)
    literature = models.BooleanField(default=0)
    mathematics = models.BooleanField(default=0)
    history = models.BooleanField(default=0)
    arts = models.BooleanField(default=0)

class Student(models.Model):
    clazz = models.CharField(max_length=5)
    parent = models.IntegerField()

class Parent(models.Model):
    userID = models.IntegerField()
    children = models.CharField(max_length=20) #str=array, separated by ','

class Formteacher(models.Model):
    userID = models.IntegerField()
    clazz = models.CharField(max_length=5)

class TeachersOfClass(models.Model):
    teacher = models.IntegerField()
    clazz = models.CharField(max_length=5)

class Appointments(models.Model):
    teacher = models.IntegerField()
    _from = models.IntegerField()
    to = models.IntegerField()
    parent = models.IntegerField()

class Allowance(models.Model):
    teacher = models.IntegerField()
    isAllowed = models.BooleanField(default=1)

