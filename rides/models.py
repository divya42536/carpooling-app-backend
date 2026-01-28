from django.db import models
from users.models import Person

# Create your models here.
class Ride(models.Model):
    RIDE_TYPE_CHOICES = [('OFFER', 'Offer ride'), # driver offers a ride
                         ('REQUEST', 'Request ride')] # riderrequests a ride
    carpooler = models.ForeignKey(Person, on_delete=models.CASCADE)
    ride_type= models.CharField(max_length=10, choices=RIDE_TYPE_CHOICES)

    start_location= models.CharField(max_length=100)
    end_location= models.CharField(max_length=100)
    earliest_time= models.DateTimeField()
    latest_time= models.DateTimeField()
    available_seats= models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.start_location} to {self.end_location}"


# class Booking(models.Model):
#     rider= models.ForeignKey(User, on_delete=models.CASCADE)
#     ride= models.ForeignKey(Ride, on_delete=models.CASCADE)
#     status= models.CharField(max_length=20)
