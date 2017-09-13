"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User

class Player(User):
    contact = models.CharField(max_length = 15)
    rank = models.SmallIntegerField(null=True,blank=True)


