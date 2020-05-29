from django.db import models
from goods.models import Warehouse, Product, Volume
from companies.models import Company, Contract, Outlet
from users.models import User


class Sale(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.DO_NOTHING
    )
    contract = models.ForeignKey(
        Contract,
        on_delete=models.DO_NOTHING
    )
    outlet = models.ForeignKey(
        Outlet,
        on_delete=models.DO_NOTHING
    )
    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.DO_NOTHING
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.DO_NOTHING
    )
    volume = models.ForeignKey(
        Volume,
        on_delete=models.DO_NOTHING
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING
    )
    due_date = models.DateTimeField(

    )
