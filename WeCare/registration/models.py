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

class Doctor(models.Model):
    contactno=models.IntegerField()
    education=models.CharField(max_length=100)
    speciality=models.CharField(max_length=100) 
    userID=models.ForeignKey(UserDetails,on_delete=models.CASCADE)

class Hospital(models.Model):
    name = models.CharField(max_length=70, unique=True)
    address = models.CharField(max_length=500)
    location = models.CharField(max_length=50)
    speciality = models.CharField(max_length=70)
    timings = models.CharField(max_length=70)   
