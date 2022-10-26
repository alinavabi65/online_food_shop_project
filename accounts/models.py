from django.db import models
from django.contrib.auth.models import AbstractUser


class UserType(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)


class CustomUser(AbstractUser):
    phone = models.PositiveIntegerField(max_length=12)
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE, related_name='custom_user', )







