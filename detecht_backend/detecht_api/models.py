from django.db import models
from django.contrib.auth.models import (AbstractBaseUser)


# Create your models here.

# BEGIN: Code written by Armin
class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True, verbose_name="email address")
    full_name = models.CharField(max_length=255, blank=True, null=True)
    admin = models.BooleanField(default=False)  # True if user is admin
    # password
    # age


    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.full_name

    @property
    def is_admin(self):
        return self.admin
# END: Code written by Armin
