from django.contrib.auth.models import AbstractUser
from django.db import models
from krinitsa.utils import ROLES


class User(AbstractUser):
    telephone = models.CharField(
        max_length=10,
        null=True,
        blank=True
    )
    role = models.CharField(
        max_length=50,
        choices=ROLES
    )

    class Meta:
        ordering = ['username', 'date_joined']


class Avatar(models.Model):
    user = models.ForeignKey(User, related_name='avatars', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img')
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = 'create_at'
        ordering = ['create_at']

    def __str__(self):
        return f'{self.user.username} avatar'
