from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
from datetime import datetime
# from django.core.exceptions import ValidationError
# from django.utils.translation import gettext_lazy as _
# from django.core.validators import RegexValidator
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

user_title = (('MR.', 'Mr.'), ('MRS.', 'Mrs.'),)
user_gender = (('MALE', 'Male'), ('FEMALE', 'female'),)
med_type = (('SYRUP', 'Syrup Bottle'), ('TABLETS', 'Tablets'),
            ('CAPSULES', 'Capsules'))
address_country = (('INDIA', 'India'), ('BANGLADESH',
                                        'Bangladesh'), ('PAKISTAN', 'Pakistan'),)


class User(AbstractUser):
    title = models.CharField(
        verbose_name='Title', choices=user_title, max_length=4, blank=True, default="")
    age = models.PositiveSmallIntegerField(
        verbose_name='Age', blank=False, default=18, choices=[(x, x) for x in range(18, 92)])
    gender = models.CharField(
        verbose_name='Gender', choices=user_gender, max_length=7, blank=True, default="")
    company = models.CharField(
        verbose_name='Comapny Name', max_length=350, blank=True, default="")
    dlno = models.CharField(
        verbose_name='Drug License no.', max_length=250, blank=True, default="")
    gstno = models.CharField(
        verbose_name='GSTIN no.', max_length=15, blank=True, default="")
    area_of_intrest = models.CharField(
        verbose_name='Area Of Intrest', max_length=360, blank=True, default="")
    username = models.CharField(
        verbose_name='Username', max_length=250, blank=False, unique=False)
    email = models.EmailField(
        verbose_name='Email Address', max_length=255, blank=False, unique=True)
    customer = models.BooleanField(default=False)
    pharmacist = models.BooleanField(default=False)
    is_active = models.BooleanField('active', default=True)
    phone = models.CharField(max_length=10, blank=False,
                             null=False, default='0')
    USERNAME_FIELD = 'email'
    # Username & Password are required by default.
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


@python_2_unicode_compatible
class Address(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_query_name='address')
    title = models.CharField(
        verbose_name='Title', choices=user_title, max_length=4, blank=False, default='Mr.')
    first_name = models.CharField(
        verbose_name='Fisrt Name', max_length=250, blank=False, unique=False, default=' ')
    last_name = models.CharField(
        verbose_name='Last Name', max_length=250, blank=False, unique=False, default='')
    phone = models.CharField(
        max_length=10, blank=False, null=False, default='0')

    street_address = models.CharField(
        verbose_name='Street Address', max_length=250, blank=False, unique=False)
    city = models.CharField(verbose_name='City',
                            max_length=250, blank=False, unique=False)
    country = models.CharField(verbose_name='Country', choices=address_country,
                               max_length=250, blank=False, unique=False, default=" ")
    pincode = models.CharField(
        max_length=6, verbose_name='Pin-Code', blank=False, default=" ")

    def __str__(self):
        return u" {} | {} " .format(self.user.email, self.street_address)


class Medicine(models.Model):
    m_name = models.CharField(
        verbose_name='Medicine Name', max_length=550, blank=False)
    mc_name = models.CharField(
        verbose_name='Medicine Company Name', max_length=950, blank=False)
    m_type = models.CharField(
        verbose_name='Medicine Type', max_length=550, blank=False, choices=med_type)
    mb_quantity = models.CharField(
        verbose_name='Single Box Quantity', blank=False, max_length=550, default="0")
    ms_quantity = models.PositiveSmallIntegerField(
        verbose_name='Stock Quantity', blank=False, default="0")
    description = models.TextField(
        verbose_name='Medicine Description', max_length=950, blank=False)
    max_price = models.PositiveSmallIntegerField(
        verbose_name='MRP Of Medicine', blank=False, default="0")
    our_price = models.PositiveSmallIntegerField(
        verbose_name='Pharmacist Price Of Medicine', blank=False, default="0")
    Discount = models.PositiveSmallIntegerField(
        verbose_name='Discount On Price', blank=False, default="0")

    def __str__(self):
        return self.m_name


class Salt(models.Model):
    medicine = models.ManyToManyField(
        Medicine, related_query_name='salt', related_name='salt')
    s_name = models.CharField(verbose_name='Salt Name',
                              max_length=250, blank=False)
    s_quantity = models.CharField(verbose_name='Salt Quantity',
                                  max_length=250, blank=False, default=" ")

    def __str__(self):
        return self.s_name
