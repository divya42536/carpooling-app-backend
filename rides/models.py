from django.db import models
# from users.models import User

# # Create your models here.
# class Ride(models.Model):
#     driver= models.ForeignKey('users.User', on_delete=models.CASCADE)
#     start_location= models.CharField(max_length=100)
#     end_location= models.CharField(max_length=100)
#     date= models.DateTimeField()
#     available_seats= models.ImageField()

# class Booking(models.Model):
#     rider= models.ForeignKey(User, on_delete=models.CASCADE)
#     ride= models.ForeignKey(Ride, on_delete=models.CASCADE)
#     status= models.CharField(max_length=20)
