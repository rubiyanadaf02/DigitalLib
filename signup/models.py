from django.db import models

# Create your models here.
class Signup(models.Model):
    name=models.TextField(max_length=50)
    email=models.TextField(max_length=50)
    password=models.TextField(max_length=15)
    cpass=models.TextField(max_length=15)