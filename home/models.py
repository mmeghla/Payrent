from django.db import models
from django.db.models.fields.files import ImageField
from django.shortcuts import render,redirect,HttpResponseRedirect,reverse
from django.contrib.auth.models import User
from django.conf import settings 



# post
class infor(models.Model):
    name=models.CharField(max_length=19)
    date=models.DateField(auto_now_add=True,null=True)
    phone=models.CharField(max_length=19)
    room_nn=models.CharField(max_length=100,null=True)
    ammount=models.CharField(max_length=100,null=True)
    month_details=models.CharField(max_length=100,null=True)
    

    def __str__(self):
        if len(self.name)>50:
            return self.name[:50]+"..."
        return self.name

class uploadsss(models.Model):
    username=models.CharField(max_length=19)
    name=models.CharField(max_length=19)
    date=models.DateField(auto_now_add=True)
    phone=models.CharField(max_length=19)
    address=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    details=models.TextField()
    location=models.CharField(max_length=99)
    

    def __str__(self):
        if len(self.name)>50:
            return self.name[:50]+"..."
        return self.name



    