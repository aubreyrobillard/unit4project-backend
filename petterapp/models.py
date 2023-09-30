from django.db import models

from django.db import models

# Create your models here.
class Petter(models.Model):
    photo=models.CharField(max_length=300)
    name=models.CharField(max_length=200)
    birthday=models.CharField(max_length=200)
    sex=models.CharField(max_length=200)
    breed=models.CharField(max_length=200)
    color=models.CharField(max_length=200)
    spayed=models.BooleanField(max_length=200)
    microchipped=models.BooleanField(max_length=200)
    foodBrand=models.CharField(max_length=200)
    foodName=models.CharField(max_length=200)
    foodAmount=models.CharField(max_length=200)
    foodFrequency=models.CharField(max_length=200)
    medicationName=models.CharField(max_length=200)
    medicationDosage=models.CharField(max_length=200)
    medicationFrequency=models.CharField(max_length=200)
    vetName=models.CharField(max_length=200)
    vetLocation=models.CharField(max_length=200)
    vetPhone=models.CharField(max_length=200)
    vetWebsite=models.CharField(max_length=200)