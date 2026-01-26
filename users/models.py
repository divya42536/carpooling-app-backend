from django.db import models

# Create your models here.
class Rider(models.Model):
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Email=models.CharField(max_length=30)
    Phone=models.IntegerField(max_length=15)

class Driver(models.Model):
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Email= models.CharField(max_length=30)
    Phone= models.IntegerField(max_length=30)
    CarNumber= models.charField(max_length=30)
    DriverLicense= models.charField(max_length=30)




