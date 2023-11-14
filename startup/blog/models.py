from django.db import models

# Create your models here.


class Before_SignUp(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)


class Start(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    quote = models.TextField(blank=True, null=True)
    icon = models.FileField(upload_to='images/', blank=True, null=True)


class CallBack(models.Model):
    enter_email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    signup_email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    verify_code = models.CharField(max_length=100)


class Main(models.Model):
    username = models.CharField(max_length=100)
    logo = models.FileField(upload_to='images/', blank=True, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    search = models.CharField(max_length=100)


class Eats(models.Model):
    food = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Filters(models.Model):
    