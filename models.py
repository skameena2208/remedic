from django.db import models

# Create your models here.
class Contact_1(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.TextField()
    message=models.TextField()
class Contact_2(models.Model):
    name= models.CharField(max_length=50)
    email=models.EmailField()
    mobile=models.BigIntegerField()
    gender=models.CharField(max_length=30)
    address=models.TextField()
    pincode=models.IntegerField()
    image=models.FileField()
    password=models.CharField(max_length=50)
    status=models.CharField(max_length=400,default='pending')