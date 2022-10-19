from django.db import models
from tulip.settings import AUTH_USER_MODEL

# Create your models here.

class Subject(models.Model):
    ''' Model for Subjects'''
    subject_name = models.CharField(max_length=20)
    def __str__(self):
        return str(self.subject_name)


class Teacher(models.Model):
    ''' Model for Teachers'''
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    teacher_name =  models.CharField(max_length=50)
    teacher_subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return str(self.teacher_name)

class Student(models.Model):
    ''' Model for Students'''
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=50)
    student_teachers = models.ManyToManyField(Teacher)

    def __str__(self):
        return str(self.student_name)
