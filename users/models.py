from django.db import models


# # Create your models here.
class Person(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    is_driver = models.BooleanField(default=False)


    def __str__(self):
        return self.username



