from django.db import models
from users.models import User


class Service_area(models.Model):
    name = models.CharField(
        max_length=100
    )
    sales_plan = models.PositiveIntegerField(
        unique_for_month=True
    )
    salesman = models.ManyToManyField(
        User,
        related_name='user_teams'
    )
    created_on = models.DateField(
        auto_now=True
    )
    created_by = models.ForeignKey(
        User,
        related_name='area_created',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

    def get_users(self):
        return ",".join(
            [str(_el) for _el in list(self.users.values_list('id', flat=True))]
        )
