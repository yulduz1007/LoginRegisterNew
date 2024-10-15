from django.db import models
from django.db.models import Model


# Create your models here.


class Event(Model):
    pass


class Product(Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

