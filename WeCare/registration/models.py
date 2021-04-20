from django.db import models
# from pytz import timezone
from django.utils import timezone

class UserDetails(models.Model):
    name=models.CharField(max_length=50,unique=True)
    emailID=models.EmailField()
    password=models.CharField(max_length=15)
    IsAdmin=models.BooleanField()
    IsDoctor=models.BooleanField()

class Hospital(models.Model):
    name = models.CharField(max_length=70, unique=True)
    address = models.CharField(max_length=500)
    location = models.CharField(max_length=50)
    pincode=models.IntegerField(default=380001)
    speciality = models.CharField(max_length=70)
    timings = models.CharField(max_length=70)   

class Doctor(models.Model):
    contactno=models.IntegerField()
    education=models.CharField(max_length=100)
    speciality=models.CharField(max_length=100)
    associate_hospital=models.ForeignKey(Hospital,on_delete=models.CASCADE,null=True) 
    userID=models.ForeignKey(UserDetails,on_delete=models.CASCADE)

class Disease(models.Model):
    name=models.CharField(max_length=50,unique=True)
    Symptoms=models.CharField(max_length=300)
    Description=models.CharField(max_length=1000)
    Cause=models.CharField(max_length=500)

class SkinDisease(models.Model):
    name = models.CharField(max_length=70, unique=True)
    image1 = models.ImageField(upload_to = "images/")
    image2 = models.ImageField(upload_to = "images/")
    image3 = models.ImageField(upload_to = "images/")

class DiseaseTreatment(models.Model):
    Disease_id=models.ForeignKey(Disease,on_delete=models.CASCADE)
    description=models.CharField(max_length=1000)
    duration=models.CharField(max_length=100)

class SearchSymptomRecord(models.Model):
    symptom=models.CharField(max_length=50)
    searchcount=models.IntegerField(default=0)
    searchdate=models.DateTimeField(default=timezone.now)

class SearchDiseaseResult(models.Model):
    diseasename=models.ForeignKey(Disease,on_delete=models.CASCADE)
    searchcount=models.IntegerField(default=0)
    searchdate=models.DateTimeField(default=timezone.now)


class Questions(models.Model):
    que_text=models.CharField(max_length=2000,unique=True)
    date_posted=models.DateTimeField(default=timezone.now)

class Answers(models.Model):
    ans_text=models.CharField(max_length=3000)
    que_text=models.ForeignKey(Questions,on_delete=models.CASCADE,default=2)
    date_posted=models.DateTimeField(default=timezone.now)

class Pharmacy(models.Model):
    name=models.CharField(max_length=2000,unique=True)
    location=models.CharField(max_length=2000)
    

