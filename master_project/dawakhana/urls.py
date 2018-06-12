from django.contrib import admin
from django.urls import path, include
from .import views
# from .forms import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('homepage/', views.homepage_view, name='homepage'),
    path('customer_register/', views.customer_register_view,
         name='customer_register'),
    path('pharmacist_register/', views.pharmacist_register_view,
         name='pharmacist_register'),
    path('user_login/', views.login_view, name='user_login'),
    path('user_logout/', views.logout_view, name='user_logout'),
    path('my_account/', views.my_account_view, name='my_account'),
    path('user_edit_account', views.edit_account_view, name='user_edit_account'),
    path('user_edit_address', views.edit_address_view, name='user_edit_address'),
    path('user_add_address', views.add_address_view, name='user_add_address'),

]
