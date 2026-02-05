from django.db import models
from users.models import Person
from django.core.exceptions import ValidationError

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
    
    def clean(self):
        # Ensure latest_time >= earliest_time
        if self.latest_time < self.earliest_time:
            raise ValidationError("latest_time cannot be earlier than earliest_time")

        # Business rule: Offer rides must have available seats
        if self.ride_type == "OFFER" and self.available_seats is None:
            raise ValidationError("Offer rides must have available seats")



