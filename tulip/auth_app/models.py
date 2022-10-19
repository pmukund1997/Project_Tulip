from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    ''' User class added user role attribute to classify users into diferrent roles '''

    USER_TYPE_CHOICES = (
      (1, 'student'),
      (2, 'teacher'),
      (5, 'admin'),
    )

    user_role = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    REQUIRED_FIELDS = ["user_role"]

    def __str__(self):
        return str(self.username)



