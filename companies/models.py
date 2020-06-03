from django.db import models


class Bank(models.Model):
    name = models.CharField(
        max_length=200
    )
    address = models.CharField(
        max_length=350,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.abbreviation


class Bank_account(models.Model):
    number = models.CharField(
        max_length=28
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
        null=True,
        blank=True
    )

    def __str__(self):
        return self.number


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
        null=True,
        blank=True
    )
    due_date_payment = models.PositiveSmallIntegerField(
        default=45
    )

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(
        max_length=200
    )
    upn = models.PositiveIntegerField(
        unique=True,
        null=True,
        blank=True
    )
    address = models.CharField(
        max_length=350,
        null=True,
        blank=True
    )
    bank_account = models.ForeignKey(
        Bank_account,
        related_name='accounts',
        on_delete=models.CASCADE
    )
    email = models.EmailField(
        max_length=250,
        null=True,
        blank=True
    )
    contract = models.ForeignKey(
        Contract,
        related_name='contracts',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Contact_person(models.Model):
    first_name = models.CharField(
        max_length=60
    )
    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )
    birthday = models.DateField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.first_name


class Outlet(models.Model):
    name = models.CharField(
        max_length=250
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.DO_NOTHING
    )
    contact = models.ForeignKey(
        Contact_person,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    address = models.CharField(
        max_length=350,
        null=True,
        blank=True
    )
    telephone = models.CharField(
        max_length=10,
        null=True,
        blank=True
    )
    email = models.EmailField(
        max_length=250,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
