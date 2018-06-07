from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.contrib.auth.models import User
#from django.db.models.signals import post_save
#from django.dispatch import receiver
#from datetime import datetime
#from django.core.exceptions import ValidationError
#from django.utils.translation import gettext_lazy as _
#from django.core.validators import RegexValidator
#from django.utils.encoding import python_2_unicode_compatiple
# Create your models here.


class User(AbstractUser):
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
