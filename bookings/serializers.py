from .models import Booking
from rest_framework import serializers
from rides.serializers import RideSerializer


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['rider', 'status', 'booked_at']


    def validate(self, data):
        ride = data.get('ride')
        rider = self.context.get('rider')
        if not ride:
            raise serializers.ValidationError("Ride information is required.")
        if ride.carpooler == rider:
            raise serializers.ValidationError("Rider cannot book their own ride.")
        if ride.ride_type == "OFFER" and ride.available_seats <= 0:
            raise serializers.ValidationError("No available seats for this ride.")
        return data