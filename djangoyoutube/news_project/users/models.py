from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=200)
    jobs = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    image = models.ImageField(upload_to='users/', null=True, blank=True)

    def __str__(self):
        return self.username
