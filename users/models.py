from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User')
    )

    username = models.CharField(max_length = 100)
    email = models.EmailField(unique = True)
    phoneNo = models.CharField(max_length=10)
    role = models.CharField(max_length=10, choices = ROLE_CHOICES, default = 'user')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phoneNo']

    def __str__(self):
        return self.email