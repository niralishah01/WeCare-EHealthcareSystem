from django.db import models

# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=70, unique=True)
    address = models.CharField(max_length=200)
    location = models.CharField(max_length=50)
    speciality = models.CharField(max_length=70)
    timings = models.CharField(max_length=70)
    