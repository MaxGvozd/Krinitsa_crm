from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    telephone = models.CharField(
        null=True
    )
