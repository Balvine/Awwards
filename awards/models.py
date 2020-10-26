from django.contrib.auth.models import User
import datetime as dt
from django.db import models
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

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    post_save.connect(save_user_profile, sender=User)

    def save_profile(self):
        self.save()

    def del_profile(self):
        self.delete()

    @classmethod
    def get_by_id(cls, user_id):
        profile = Profile.objects.get(user_id=user_id)
        return profile

    def __str__(self):
        return self.bio


class Project(models.Model):
    """
    Class that contains Project details
    """
    title = models.CharField(max_length=20)
    landing_page = models.ImageField(upload_to='images/')
    description = models.TextField()
    link = models.URLField(max_length=100)
    rating = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_pro(self):
        self.save()

    def del_pro(self):
        self.delete()

