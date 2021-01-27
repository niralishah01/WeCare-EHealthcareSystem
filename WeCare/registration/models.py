from django.db import models

class UserDetails(models.Model):
    name=models.CharField(max_length=50,unique=True)
    emailID=models.EmailField()
    password=models.CharField(max_length=15)
    IsAdmin=models.BooleanField()
    IsDoctor=models.BooleanField()

class Disease(models.Model):
    name=models.CharField(max_length=50,unique=True)
    Symptoms=models.CharField(max_length=300)
    Description=models.CharField(max_length=1000)
    Cause=models.CharField(max_length=500)
