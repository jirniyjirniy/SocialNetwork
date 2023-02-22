from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class UserNet(AbstractUser):
    '''Custom User Model'''
    middle_name = models.CharField(max_length=50)
    first_login = models.DateField(null=True)
    phone = models.CharField(max_length=14)
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)
