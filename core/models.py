from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from datetime import datetime
from .manager import *

class Bloodstock(models.Model):
    blood_type = models.CharField(max_length=5)
    quantity = models.IntegerField()

    def __str__(self):
        return self.blood_type


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
    blood_group = models.ForeignKey(Bloodstock, on_delete=models.CASCADE, null=True)

    is_manager = models.BooleanField(default=False, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email
    

class Order(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    bloodgroup = models.ForeignKey(Bloodstock, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    address = models.TextField()
    idproff = models.CharField(max_length=200)
    idtype = models.CharField(max_length=100)
    contactno = models.BigIntegerField()
    emer_contactno = models.BigIntegerField()
    orderdate = models.DateTimeField(default=datetime.now, null=True)
    deliverdate = models.DateField()
    delivertime = models.CharField(max_length=10)
    deliverymode = models.CharField(max_length=100)
    status = models.BooleanField(default=False) 


class Blooddonation(models.Model):
    donate_userid = models.ForeignKey(User, on_delete=models.CASCADE)
    donate_date = models.DateField()
    donate_time = models.CharField(max_length=10)
    disease = models.TextField(null=True)

class Offlinedelivery(models.Model):
    delivery_date = models.DateField()
    delivery_time = models.TimeField()
    delivery_address = models.TextField()
    message = models.TextField()
    orderid = models.ForeignKey(Order, on_delete=models.CASCADE)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)    