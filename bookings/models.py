from django.db import models
from rides.models import Ride
from users.models import Person


# Create your models here.
class Booking(models.Model):
    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELLED = "cancelled"

    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELLED, "Cancelled"),
    ]   

    rider = models.ForeignKey(Person, on_delete=models.CASCADE)
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    booked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('rider', 'ride')
        ordering = ['-booked_at']

    def __str__(self):
        return f"Booking({self.rider}, {self.ride}, {self.status})"
