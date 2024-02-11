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
    

# class TagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tag
#         fields = ['name']

# class ProductSerializer(serializers.ModelSerializer):
#     tags = TagSerializer(many=True, read_only=True)
#     class Meta:
#         model = Product
#         fields = ['SKU','name','category','tags','in_stock','available_stock']

# class ProductCreateUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ['SKU','name','category','tags','in_stock','available_stock']  
        
#     # Override the create and update methods to handle the ManyToMany field 
#     def create(self, validated_data):
#         tags = validated_data.pop('tags')
#         product = Product.objects.create(**validated_data)
#         for tag in tags:
#             tag, created = Tag.objects.get_or_create(name=tag['name'])
#             product.tags.add(tag)
#         return product

#     def update(self, instance, validated_data):
#         tags = validated_data.pop('tags')
#         product = super().update(instance, validated_data)
#         product.tags.clear()
#         for tag in tags:
#             tag, created = Tag.objects.get_or_create(name=tag['name'])
#             product.tags.add(tag)
#         return product  