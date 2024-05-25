from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

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
        # order by closest to due date
        ordering = ["due_date"]
    
    def __str__(self):
        return f"{self.cosplay_task} for {self.cosplay}"