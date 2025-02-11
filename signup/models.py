from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, name, email, password=None):
        """Creates and returns a regular user."""
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user = self.model(name=name, email=email)
        user.set_password(password)  # Hashes the password
        user.is_active = True  # Ensure the user is active by default
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password):
        """Creates and returns a superuser with all permissions."""
        user = self.create_user(name, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255, blank=False, null=False, default='Unknown')
    email = models.EmailField(unique=True, db_index=True)  # Improved lookup performance
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Required for admin access

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email
