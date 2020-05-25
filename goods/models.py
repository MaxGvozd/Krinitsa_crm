from django.db import models


class Storage(models.Model):
    name = models.CharField(
        max_length=50
    )


class Volume(models.Model):
    name = models.CharField(
        max_length=30
    )
    gross_weight = models.PositiveSmallIntegerField(

    )
    net_weight = models.PositiveSmallIntegerField(

    )
    in_packaging = models.PositiveSmallIntegerField(

    )


class Product(models.Model):
    name = models.CharField(
        max_length=30
    )

