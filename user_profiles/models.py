from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class UserProfile(models.Model):
    cosplayer = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    user_bio = models.TextField(blank=True)
    # profile_image = models.ImageField(
    #     upload_to='images/', default='../dpdnmyvepbgzchl71fjv'
    # )
    fave_cosplay = models.CharField(max_length=255, blank=True)
    next_convention = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.cosplayer}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(cosplayer=instance)


post_save.connect(create_profile, sender=User)
