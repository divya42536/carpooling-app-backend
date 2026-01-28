from django.db import models
from django.contrib.auth.hashers import make_password


# # Create your models here.
class Person(models.Model):

    # ROLE_CHOICES = (
    #     ("rider", "Rider"),
    #     ("driver", "Driver"),
    # )

    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    is_driver = models.BooleanField(default=False)
    # role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    car_number = models.CharField(max_length=50, null=True, blank=True)
    driver_license = models.CharField(max_length=50, null=True, blank=True)

    


    def __str__(self):
        return self.username



