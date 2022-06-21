from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from users.utils import CustomUserManager
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    updated_at = datetime.now()
    username = models.CharField(unique=False, null=True, max_length=200)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    objects = CustomUserManager()
