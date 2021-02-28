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

class Hospital(models.Model):
    name = models.CharField(max_length=70, unique=True)
    address = models.CharField(max_length=200)
    location = models.CharField(max_length=50)
    speciality = models.CharField(max_length=70)
    timings = models.CharField(max_length=70)

class Doctor(models.Model):
    contactno=models.IntegerField()
    education=models.CharField(max_length=100)
    speciality=models.CharField(max_length=100) 
    userID=models.ForeignKey(UserDetails,on_delete=models.CASCADE)

class SkinDisease(models.Model):
    name = models.CharField(max_length=70, unique=True)
    image1 = models.ImageField(upload_to = "images/")
    image2 = models.ImageField(upload_to = "images/")
    image3 = models.ImageField(upload_to = "images/")
