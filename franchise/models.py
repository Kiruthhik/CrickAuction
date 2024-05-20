# franchise/models.py

from django.contrib.auth.models import User
from django.db import models

class FranchiseProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #email = models.EmailField(unique=True)
    liscence = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.user.username
