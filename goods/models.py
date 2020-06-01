from django.db import models


class Warehouse(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True
    )

    def __str__(self):
        return self.name


class Volume(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True
    )
    gross_weight = models.PositiveSmallIntegerField(

    )
    net_weight = models.PositiveSmallIntegerField(

    )
    in_packaging = models.PositiveSmallIntegerField(

    )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=30
    )
    volume = models.ForeignKey(
        Volume,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name + " " + self.volume.name


class Balance(models.Model):
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
    amount = models.FloatField(
    )
