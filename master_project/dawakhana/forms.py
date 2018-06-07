from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class customer_register_form(UserCreationForm):
    email = forms.EmailField(
        max_length=250, required=True, help_text="enter your email id")
    first_name = forms.CharField(
        max_length=250, required=True, help_text="enter your first name")
    last_name = forms.CharField(
        max_length=250, required=True, help_text="enter your last name")
    password1 = forms.CharField(max_length=32, widget=forms.PasswordInput,
                                help_text="passwordmust conatin a [a-z,A-Z,0-9,!-$]")
    password2 = forms.CharField(
        max_length=32, widget=forms.PasswordInput, help_text="type password same as above")
    numeric = RegexValidator(r'^[0-9]*$', 'Only [0-9] numbers are allowed')
    phone = forms.CharField(max_length=10, required=True, validators=[
                            numeric], help_text="required for OTP")

    class Meta:
        model = User
        fields = ['email', 'first_name',

                  'last_name', 'password1', 'password2', 'phone', 'customer']


class pharmacist_register_form(UserCreationForm):
    email = forms.EmailField(
        max_length=250, required=True, help_text="enter your email id")
    first_name = forms.CharField(
        max_length=250, required=True, help_text="enter your first name")
    last_name = forms.CharField(
        max_length=250, required=True, help_text="enter your last name")
    password1 = forms.CharField(max_length=32, widget=forms.PasswordInput,
                                help_text="passwordmust conatin a [a-z,A-Z,0-9,!-$]")
    password2 = forms.CharField(
        max_length=32, widget=forms.PasswordInput, help_text="type password same as above")
    numeric = RegexValidator(r'^[0-9]*$', 'Only [0-9] numbers are allowed')
    phone = forms.CharField(max_length=10, required=True, validators=[
                            numeric], help_text="required for OTP")

    class Meta:
        model = User
        fields = ['email', 'first_name',

                  'last_name', 'password1', 'password2', 'phone', 'pharmacist', 'is_active']


class user_login_form(AuthenticationForm):
    model = User
    fields = ['email', 'password1']
