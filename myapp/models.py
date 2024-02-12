from django.db import models
from rest_framework import serializers

# Create your models here.

class Product(models.Model):
    SKU = models.CharField(max_length=100,unique=True)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    tags = models.ManyToManyField('Tag',blank=True)
    in_stock = models.BooleanField(default=True)
    available_stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name