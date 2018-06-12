from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from .forms import *
from .models import *
from django.http import *
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseNotAllowed
from django.db.models import Q
from django.contrib import messages
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
        #login(request, new_p_user)
        return redirect('homepage')

    return render(request, 'dawakhana/pharmacist_register.html', context)


def login_view(request):
    logout(request)
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password1']
        new_user = authenticate(request, email=email, password=password)
        if new_user is not None:
            if new_user.is_active:
                login(request, new_user)
                return redirect('my_account')
            else:
                return HttpResponse('inactive profile')

    login_form = user_login_form()
    context = {'login_form': login_form}
    return render(request, 'dawakhana/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('homepage')


def my_account_view(request):
    id = request.user.pk
    user = User.objects.get(pk=id)
    user.save()
    user_sa = Address.objects.filter(user_id=id)
    # user_sa= user shipping address.
    # user_sa.save()
    context = {"user_sa": user_sa,
               "user": user,
               }
    return render(request, 'dawakhana/my_account.html', context)


def edit_account_view(request):  # edit useraccount view
    if request.method == 'POST':
        ea_form = edit_account_form(request.POST, instance=request.user)
        if ea_form.is_valid():
            ea_form.save()
            return redirect('my_account')
        else:
            messages.error(request, ('please correct the error below'))
            return redirect('user_edit_account')
    ea_form = edit_account_form(instance=request.user)
    context = {'ea_form': ea_form}
    return render(request, 'dawakhana/edit_account_information.html', context)


def edit_address_view(request):
    id = request.user.pk
    # editing of user default address
    user_address = Address.objects.get(user_id=id)
    if request.method == 'POST':
        user_sa_form = address_form(
            request.POST, instance=user_address)
        if user_sa_form.is_valid():
            user_sa_form.save()
            return redirect('my_account')
        else:
            messages.error(request, ("please enter a valid address"))
            return redirect('user_edit_address')
    user_sa_form = address_form(instance=user_address)
    context = {'user_sa_form': user_sa_form}
    return render(request, 'dawakhana/edit_user_address.html', context)


def add_address_view(request):
    id = request.user.pk
    user = User.objects.get(pk=id)
    if request.method == 'POST':

        new_address = user.address.create(phone=request.POST['phone'], last_name=request.POST['last_name'], first_name=request.POST['first_name'], title=request.POST['title'], street_address=request.POST['street_address'], city=request.POST['city'],
                                          country=request.POST['country'], pincode=request.POST['pincode'],)
        new_address.save()
        return redirect('my_account')
    user_sa_form = address_form(instance=user)
    context = {'user_sa_form': user_sa_form}
    return render(request, 'dawakhana/add_user_address.html', context)
