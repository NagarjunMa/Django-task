from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path("products/", views.retrieveProducts, name="retrieveProducts"),
    path("product/<str:pk>", views.retrieveDetail, name="retrieveDetail"),
    path("product/create/", views.createProduct, name="createProduct"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("product/update/<str:pk>", views.updateProduct, name="updateProduct"),
    path("product/delete/<str:pk>", views.deleteProduct, name="deleteProduct"),
    path("register/", views.registerPage, name="register"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path('redirect/add_product/', views.redirect_to_add_product, name='redirect_add_product'),
]