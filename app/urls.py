from django.contrib import admin
from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('base/', views.base, name="base"),
    path('', views.getHome, name="home"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logoutPage, name="logout"),
    path('search/', views.searchProduct, name="search"),
    path('category/', views.category, name="category"),
    path('detail/', views.detail, name="detail"),
    path('address/', views.Continue1, name="address"),
    path('information/', views.Information, name="information"),
    path('information_address/', views.information_address, name="information_address"),
    path('deleteAddress/<int:pk>/', views.deleteAddress, name="deleteAddress"),  
    path('addAddress/', views.addAddress, name="addAddress"),
    path('editAddress/<int:pk>/', views.editAddress, name="editAddress"),  
    path('my_order/', views.myOrder, name="myOrder"),
    path('delete_my_order/<int:pk>/', views.deletemyOrder, name="delete_myOrder"),  
    path('editAddress/<int:pk>/', views.editAddress, name="editAddress"),
    path('addAddress/', views.addAddress, name="addAddress"),


    # Phần admin
    path('manage/', views.Manage, name="manage"),
    path('home_manage/', views.homeManage, name="home_manage"),
    path('manageSlide/', views.manageSlide, name="manageSlide"),
    path('manageOrder/', views.manageOrder, name="manageOrder"),

    path('  /', views.manageProduct, name="manageProduct"),
    path('addProduct/', views.addProduct, name="addProduct"),
    path('editProduct/<int:pk>/', views.editProduct, name="editProduct"),  # Chỉnh sửa dòng này
    path('deleteProduct/<int:pk>/', views.deleteProduct, name="deleteProduct"),  # Chỉnh sửa dòng này
    path('viewProduct/', views.viewProduct, name="viewProduct"),
    path('manageCategory/', views.manageCategory, name="manageCategory"),
    path('addCategory/', views.addCategory, name="addCategory"),
    path('editCategory/<int:pk>/', views.editCategory, name="editCategory"),  # Chỉnh sửa dòng này
    path('deleteCategory/<int:pk>/', views.deleteCategory, name="deleteCategory"),  # Chỉnh sửa dòng này

    path('manageUser/', views.manageUser, name="manageUser"),

    # API
    path('api/products/', CreateProductAPI.as_view(), name='create-product-api'),
    path('api/products/<int:pk>/', UpdateProductAPI.as_view(), name='update-product-api'),  # Chỉnh sửa dòng này
    path('api/category/', CreateCategoryAPI.as_view(), name='create-category-api'),
    path('api/category/<int:pk>/', UpdateCategoryAPI.as_view(), name='update-category-api'),  # Chỉnh sửa dòng này
]
