from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    is_driver = models.BooleanField(default=False)


class DriverProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car_number = models.CharField(max_length=30)
    driver_license = models.CharField(max_length=30)



