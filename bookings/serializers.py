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
    

class BookingListSerializer(serializers.ModelSerializer):    
    ride_id = serializers.IntegerField(source='ride.id')
    start_location = serializers.CharField(source='ride.start_location')
    end_location = serializers.CharField(source='ride.end_location')
    earliest_time = serializers.DateTimeField(source='ride.earliest_time')
    latest_time = serializers.DateTimeField(source='ride.latest_time')
    driver_name = serializers.CharField(source='ride.carpooler.first_name')

    class Meta:
        model = Booking
        fields = [
            'id',
            'status',
            'booked_at',
            'ride_id',
            'start_location',
            'end_location',
            'earliest_time',
            'latest_time',
            'driver_name',
        ]