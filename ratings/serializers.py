from rest_framework import serializers
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'ride','score','comment']
    
    # def validate(self, data):
    #     request = self.context['request']
    #     ride = data['ride']
    #     user = request.user

    #     if user not in [ride.driver, ride.rider]:
    #         raise serializers.ValidationError("You were not part of this ride.")

    #     if user == ride.driver:
    #         data['reviewee'] = ride.rider
    #     else:
    #         data['reviewee'] = ride.driver

    #     data['reviewer'] = user
    #     return data

    # def create(self, validated_data):
    #     return Rating.objects.create(**validated_data)



    
