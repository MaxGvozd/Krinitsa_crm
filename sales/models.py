from django.db import models
from users.models import User


class Service_area(models.Model):
    name = models.CharField(
        max_length=50
    )
    sales_plan = models.PositiveIntegerField(

    )
    salesman = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )
