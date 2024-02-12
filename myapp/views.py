from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializers
from .serializers import TagSerializers
from django.contrib.auth.forms import UserCreationForm
import json
import sys
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from .filters import ProductFilter

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request): 
    if request.user.is_authenticated:
        return render(request, 'accounts/dashboard.html')
    else:
        context={} # request is the parameter that is passed to the function
        return render(request, 'accounts/home.html', context)
    



@login_required(login_url='login')
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account was created for " + user +" Sucessfully!! ")
                return redirect('login')

        context ={"form":form}
        return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == "POST":
             username = request.POST.get('username')
             password = request.POST.get('password')

             user = authenticate(request, username=username, password=password)
             if user is not None:
                   login(request, user)
                   return redirect('home')
             else:
                messages.info(request, "Username or Password is uncorrect!! Please try again")
        context ={}
        return render(request, 'accounts/login.html', context)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')

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


def dashboard(request):
    if request.user.is_authenticated:
        products = Product.objects.all()

        myFilter = ProductFilter(request.GET, queryset=products)
        products = myFilter.qs

        total_items = products.count()
        total_categories = Product.objects.values('category').distinct().count()
        serializers = ProductSerializers(products, many=True)
        return render(request, 'accounts/dashboard.html', {'products':serializers.data, 'total_items': total_items, 'total_categories': total_categories, 'myFilter': myFilter})
    else:
        return redirect('login')
    

# Function to handle a redirect to the add product form
def redirect_to_add_product(request):
    # Redirect to the URL for adding a product
    context ={}
    return render(request, 'accounts/add_products.html', context)


