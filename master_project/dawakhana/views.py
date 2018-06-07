from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from .forms import *
from .models import *
# Create your views here.


def homepage_view(request):
    return render(request, 'dawakhana/index.html',)


# user registration model
def customer_register_view(request):
    c_form = customer_register_form(request.POST or None)
    context = {
        "c_form": c_form
    }
    if c_form.is_valid():
        c_user = c_form.save(commit=False)
        username = c_form.cleaned_data.get("username")
        password = c_form.cleaned_data.get("password1")
        email = c_form.cleaned_data.get("email")
        customer = c_form.cleaned_data.get("customer")
        c_user.customer = True
        c_user.set_password(password)
        c_user.save()
        new_c_user = authenticate(
            username=username, password=password, email=email)
        login(request, new_c_user)
        return redirect('homepage')

    return render(request, 'dawakhana/customer_register.html', context)


# pharmacist registration form
def pharmacist_register_view(request):
    p_form = pharmacist_register_form(request.POST or None)
    context = {
        "p_form": p_form
    }
    if p_form.is_valid():
        p_user = p_form.save(commit=False)
        username = p_form.cleaned_data.get("username")
        password = p_form.cleaned_data.get("password1")
        email = p_form.cleaned_data.get("email")
        pharmacist = p_form.cleaned_data.get("pharmacist")
        active = p_form.cleaned_data.get("is_active")
        p_user.active = False
        p_user.pharmacist = True
        p_user.set_password(password)
        p_user.save()
        new_p_user = authenticate(
            username=username, password=password, email=email)
        login(request, new_p_user)
        return redirect('homepage')

    return render(request, 'dawakhana/pharmacist_register.html', context)
