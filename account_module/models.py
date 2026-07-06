from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    avatar=models.ImageField(upload_to='images/profile',verbose_name='آواتار')