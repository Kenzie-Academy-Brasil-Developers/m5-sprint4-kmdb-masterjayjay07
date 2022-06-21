from django.contrib.auth.models import BaseUserManager
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, is_staff, is_superuser, **extra_fields):
        email = self.normalize_email(email)
        if not email:
            raise ValueError("Email field cannot be empty") 
        now = timezone.now()

        user = self.model(
            email = email,
            first_name = first_name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            is_active = True,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)

        user.save(self._db)

        return user

    def create_user(self, email, password, first_name, last_name,**extra_fields):
        return self._create_user(email, password, first_name, last_name, True, False, **extra_fields)

    def create_superuser(self, email, password, first_name, last_name,**extra_fields):
        return self._create_user(email, password, first_name, last_name, True, True, **extra_fields)        