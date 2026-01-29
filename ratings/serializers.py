from rest_framework import serializers
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['score','comment']
    
    def validate_score(Self, value):
        if not 1 <= value <= 5:
            raise serializers.ValidationError("Score must be between 1 and 5.")
        return value
    
    def create(self, validated_data):
        ride = self.context['ride']
        user = self.context['request'].user

        # Determine who is rating whom
        if user == ride.driver:
            validated_data['rater'] = ride.driver
            validated_data['ratee'] = ride.rider
        elif user == ride.rider:
            validated_data['rater'] = ride.rider
            validated_data['ratee'] = ride.driver
        else:
            raise serializers.ValidationError("You are not part of this ride.")

        validated_data['ride'] = ride
        return super().create(validated_data)



    
