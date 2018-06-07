from django.contrib import admin
from django.urls import path, include
from .import views
from .forms import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('homepage/', views.homepage_view, name='homepage'),
    path('customer_register/', views.customer_register_view,
         name='customer_register'),
    path('pharmacist_register/', views.pharmacist_register_view,
         name='pharmacist_register'),
    path('user_login/', auth_views.login,
         {'template_name': 'dawakhana/user_login.html', 'authentication_form': user_login_form}, name='user_login'),
]
