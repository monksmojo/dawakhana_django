from django import forms
from .models import *
from django.forms import ModelForm, Widget
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
user_title = (('MR.', 'Mr.'), ('MRS.', 'Mrs.'),)
user_gender = (('MALE', 'Male'), ('FEMALE', 'female'), )
address_country = (('INDIA', 'India'), ('BANGLADESH',
                                        'Bangladesh'), ('PAKISTAN', 'Pakistan'),)


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
    dlno = forms.CharField(max_length=250, required=True, validators=[
        numeric], help_text="needed for OTP")
    gstno = forms.CharField(max_length=15, required=True, validators=[
        numeric], help_text="please enter GST no.")
    area_of_intrest = forms.CharField(
        max_length=350, required=True, help_text="please enter your area of intrest")
    company = forms.CharField(
        max_length=350, required=True, help_text="please enter your company name")

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1',
                  'password2', 'phone', 'pharmacist', 'is_active', 'dlno', 'gstno', 'area_of_intrest', 'company']


class user_login_form(forms.ModelForm):
    email = forms.EmailField(
        max_length=250, required=True, help_text="enter your email id")
    password1 = forms.CharField(max_length=32, widget=forms.PasswordInput,
                                help_text="passwordmust conatin a [a-z,A-Z,0-9,!-$]")

    class Meta:
        model = User
        fields = ['email', 'password1', ]


class edit_account_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['title', 'gender', 'age', 'first_name', 'last_name']


class address_form(forms.ModelForm):
    title = forms.ChoiceField(required=True, choices=user_title)
    numeric = RegexValidator(r'^[0-9]*$', 'Only [0-9] numbers are allowed')
    phone = forms.CharField(max_length=10, required=True, validators=[
                            numeric], help_text="required for OTP")
    pincode = forms.CharField(max_length=9, required=True,
                              help_text="enter your area pin code", validators=[numeric])

    class Meta:
        model = Address
        fields = ['title', 'first_name', 'last_name', 'phone', 'street_address', 'city', 'country',
                  'pincode']
