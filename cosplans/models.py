from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Cosplay(models.Model):
    cosplay_name = models.CharField(max_length=100)
    # may add image upload to plan later on
    def __str__(self):
        return self.cosplay_name
    
    # calculation of expenses on each cosplay
    def total_expenses(self):
        CosExpense = apps.get_model('cosexpenses', 'CosExpense')
        total = self.expenses.aggregate(Sum('unit_price'))['unit_price__sum']
        return total or 0


class CosPlan(models.Model):
    # the title of the cosplay associated with the task
    cosplayer = models.ForeignKey(User, on_delete=models.CASCADE)
    cosplay = models.ForeignKey(Cosplay, on_delete=models.CASCADE)
    # the title of the to-do task
    cosplay_task = models.CharField(max_length=200)
    """ due date from the task which is calculated when clicking the date 
    in the calendar
    """
    due_date = models.DateField()
    cosplay_notes = models.TextField(blank=True)

    class Meta:
        # composite key to ensure uniqueness using cosplay_name and cosplay
        unique_together = ("cosplayer", "cosplay_task")
        # order by closest to due date
        ordering = ["due_date"]

    def __str__(self):
        return f"{self.cosplay_task} for {self.cosplayer}"