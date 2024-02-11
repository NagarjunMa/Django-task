from rest_framework import serializers
from .models import Product, Tag

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','SKU','name','category','tags','in_stock','available_stock']

class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','name']

            