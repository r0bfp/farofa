from typing import Any
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    message = models.CharField(max_length=500)
