from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class UserProfile(models.Model):
    cosplayer = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    user_bio = models.TextField(blank=True)
    profile_image = models.ImageField(
        upload_to='images/', default='../dpdnmyvepbgzchl71fjv'
    )

    class Meta:
        ordering = ['created_at']
        
    def __str__(self):
        return f"{self.cosplayer}'s profile"

def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(cosplayer=instance)

post_save.connect(create_profile, sender=User)


class Cosplay(models.Model):
    cosplay_name = models.CharField(max_length=100)

    def __str__(self):
        return self.cosplay_name


class CosPlan(models.Model):
    # the title of the cosplay associated with the task
    cosplay = models.ForeignKey(Cosplay, on_delete=models.CASCADE)
    # the title of the to-do task
    cosplay_task = models.CharField(max_length=200)
    """ due date from the task which is calculated when clicking the date 
    in the calendar
    """
    due_date = models.DateField()
    cosplay_notes = models.TextField()
    
    class Meta:
        # composite key to ensure uniqueness using cosplay_name and cosplay
        unique_together = ("cosplay", "cosplay_task")
    
    def __str__(self):
        return f"{self.cosplay_task} for {self.cosplay}"