from django.contrib import admin
from django.urls import path, include
from .import views
# from .forms import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('homepage/', views.homepage_view, name='homepage'),
    path('user_login/', views.login_view, name='user_login'),
    path('user_logout/', views.logout_view, name='user_logout'),
    path('customer_register/', views.customer_register_view,
         name='customer_register'),
    path('customer_account/', views.customer_account_view, name='customer_account'),
    path('customer_edit_account/', views.customer_edit_account_view,
         name='customer_edit_account'),
    path('customer_add_address/', views.customer_add_address_view,
         name='customer_add_address'),
    path('customer_edit_address/', views.customer_edit_address_view,
         name='customer_edit_address'),
    path('pharmacist_register/', views.pharmacist_register_view,
         name='pharmacist_register'),
    path('pharacist_account/', views.pharmacist_account_view,
         name='pharmacist_account'),
    path('medicine_listing/', views.medicine_listing_view, name='medicine_listing'),
    path('medicine_details/<int:id>/',
         views.medicine_details_view, name='medicine_details'),
    path('search_medicine_listing ', views.search_medicine_listing_view,
         name='search_medicine_listing'),
    path('new_page/', views.new_page_view, name='new_page')
]
