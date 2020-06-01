from django.db import models


class Service_area(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True
    )
    sales_plan = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    created_on = models.DateField(
        auto_now=True
    )

    def __str__(self):
        return self.name
