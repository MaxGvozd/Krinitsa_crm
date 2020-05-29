from django.db import models
from sales.models import Service_area


class Bank(models.Model):
    name = models.CharField(
        max_length=200
    )
    address = models.CharField(
        max_length=350
    )


class Currency(models.Model):
    name = models.CharField(
        max_length=200
    )
    abbreviation = models.CharField(
        max_length=4
    )
    capacity = models.PositiveSmallIntegerField(
        default=2
    )


class Bank_account(models.Model):
    number = models.CharField(
        max_length=100
    )
    currency = models.ForeignKey(
        Currency,
        on_delete=models.DO_NOTHING
    )
    bank = models.ForeignKey(
        Bank,
        on_delete=models.DO_NOTHING
    )
    start = models.DateField(
        auto_now=True
    )
    end = models.DateField(
        blank=True
    )


class Company(models.Model):
    name = models.CharField(
        max_length=200
    )
    upn = models.PositiveIntegerField(
        unique=True
    )
    address = models.CharField(
        max_length=350
    )
    bank_account = models.ForeignKey(
        Bank_account,
        related_name='accounts',
        on_delete=models.CASCADE
    )
    email = models.EmailField(
        max_length=250,
        blank=True
    )


class Contract(models.Model):
    name = models.CharField(
        max_length=250
    )
    number = models.CharField(
        max_length=30
    )
    start = models.DateField(
        auto_now=True
    )
    end = models.DateField(
        blank=True
    )
    due_date_payment = models.PositiveSmallIntegerField(
        default=45
    )


class Contact_person(models.Model):
    name = models.CharField(
        max_length=60
    )
    last_name = models.CharField(
        max_length=30,
        blank=True
    )
    birthday = models.DateField(
        blank=True
    )


class Outlet(models.Model):
    name = models.CharField(
        max_length=250
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )
    contact = models.ForeignKey(
        Contact_person,
        on_delete=models.CASCADE
    )
    address = models.CharField(
        max_length=350
    )
    telephone = models.CharField(
        max_length=10
    )
    email = models.EmailField(
        max_length=250,
        blank=True
    )
    service_area = models.ForeignKey(
        Service_area,
        on_delete=models.DO_NOTHING,
    )
