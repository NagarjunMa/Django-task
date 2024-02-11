from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("products/", views.retrieveProducts, name="retrieveProducts"),
    path("product/<str:pk>", views.retrieveDetail, name="retrieveDetail"),
    path("product/create/", views.createProduct, name="createProduct"),
    path("product/update/<str:pk>", views.updateProduct, name="updateProduct"),
    path("product/delete/<str:pk>", views.deleteProduct, name="deleteProduct"),

]