from django.db import models
from rides.models import Ride
from users.models import Person
# Create your models here.
class Rating(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    rater = models.ForeignKey(Person, related_name='ratings_given', on_delete=models.CASCADE)
    ratee = models.ForeignKey(Person, related_name='ratings_received', on_delete=models.CASCADE)
    score = models.IntegerField()  # e.g., 1-5
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)