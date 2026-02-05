from django.db import models
from rides.models import Ride
from users.models import Person
from django.core.exceptions import ValidationError
# Create your models here.
class Rating(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name="ratings")
    # reviewer = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='given_ratings')
    # reviewee = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='received_ratings')
    score = models.IntegerField()  
    comment = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return f"{self.reviewer} → {self.reviewee} ({self.score})"
        return f"Rating: {self.score}"
    
    def clean(self):
        if self.score < 1 or self.score > 5:
            raise ValidationError("Score must be between 1 and 5")