from django.db import models
from django.contrib.auth.models import User


class CosPlan(models.Model):
    cosplayer = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    # the name of the cosplay character associated with the task
    cosplay = models.CharField(max_length=100)
    # the title of the to-do task
    cosplan_task = models.CharField(max_length=200)
    """ due date from the task which is calculated when clicking the date
    in the calendar
    """
    due_date = models.DateField()
    cosplan_details = models.TextField(blank=True)

    class Meta:
        # order by closest to due date
        ordering = ["due_date"]

    def __str__(self):
        return f"{self.cosplan_task} for {self.cosplay}"
