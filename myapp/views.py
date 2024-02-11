from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializers
from .serializers import TagSerializers
import json
import sys

# Create your views here.
def home(request):  # request is the parameter that is passed to the function
    print(sys.path)
    return HttpResponse("Hello, World!")


@api_view(['GET'])
def retrieveProducts(request):
        products = Product.objects.all()
        serializer = ProductSerializers(products, many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
def retrieveDetail(request,pk):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializers(product)
        return Response(serializer.data)

@api_view(['POST'])
def createProduct(request):
    data = request.data
    serializer = ProductSerializers(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['POST'])
def updateProduct(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializers(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def deleteProduct(request,pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response("Product deleted successfully")
