from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import *

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(max_length=200, unique=True)
    address = models.TextField(null=True)
    phone = models.BigIntegerField(null=True, unique=True)

    status = models.BooleanField(default=False)
    is_donor = models.BooleanField(default=False, null=True)
    is_receipient = models.BooleanField(default=False, null=True)
    is_hospital_stff = models.BooleanField(null=True,default=False)
    blood_group = models.CharField(max_length=6,null=True)

    is_manager = models.BooleanField(default=False, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email
    

class Bloodstock(models.Model):
    blood_type = models.CharField(max_length=5)
    quantity = models.IntegerField()