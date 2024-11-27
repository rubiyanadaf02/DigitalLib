from django.db import models

# Create your models here.
class Login(models.Model):
    email=models.TextField(max_length=25)
    password=models.TextField(max_length=12)