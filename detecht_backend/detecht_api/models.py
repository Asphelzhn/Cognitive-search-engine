from django.db import models


# Create your models here.

#By OskarH
class User(models.Model):
    userID = models.IntegerField()
    userName = models.TextField(max_length=50)
    firstName = models.TextField(max_length=50)

#end OskarH

