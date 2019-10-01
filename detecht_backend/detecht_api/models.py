from django.db import models


# Create your models here.
class User(models.Model):
    userName = models.TextField(max_length=50)
    firstName = models.TextField(max_length=50)

