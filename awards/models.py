from django.db import models
from django.http import HttpResponse
from django.contrib.auth.models import User
# import datetime as dt
# from django.db import models
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# import numpy as np
# Create your models here.



class Profile(models.Model):
    """
    Class that contains Profile details
    """
    profile_pic = models.ImageField(upload_to='images/', blank=True)
    bio = models.TextField()
    contact = models.CharField(max_length=30, blank=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
