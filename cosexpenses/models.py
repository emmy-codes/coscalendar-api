from django.db import models
from django.apps import apps
from django.core.validators import MinValueValidator


class CosExpense(models.Model):
    # connects the expense to a specific cosplay
    cosplay = models.ForeignKey(
        apps.get_model("cosplans", "Cosplay"),
        on_delete=models.CASCADE,
        related_name="expenses"
    )
    item_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(
        max_digits=8, decimal_places=2, validators=[MinValueValidator(0)]
    )
    product_link = models.URLField(blank=True, null=True)

    def total_cost(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return f"{self.quantity} x {self.item_name} for {self.cosplay}"