from django.db import models


#By OskarH
class User(models.Model):
    userID = models.IntegerField() #could be removed since and id automaticly is generated. the id starts from 1 and is incrementing for each new tuple.
    userName = models.TextField(max_length=50)
    firstName = models.TextField(max_length=50)

#end OskarH

