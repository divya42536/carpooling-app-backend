from .models import Ride
from rest_framework import serializers
from users.serializers import PersonSerializer

class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = '__all__'
        read_only_fields = ['carpooler','created_at']

    def validate(self,data):
        ride_type = data.get('ride_type')
        seat_available = data.get('available_seats')
        start_lat = data.get('start_latitude')
        start_lon = data.get('start_longitude')
        end_lat = data.get('end_latitude')
        end_lon = data.get('end_longitude')
        if ride_type == 'OFFER' and seat_available is None:
            raise serializers.ValidationError("For offer rides, available seats must be specified.")
        if ride_type == 'REQUEST' and seat_available is not None:
            raise serializers.ValidationError("For request rides, available seats must not be specified.")
        if start_lat is None or start_lon is None:
            raise serializers.ValidationError("For all rides, start latitude and longitude must be specified.")
        if end_lat is None or end_lon is None:
            raise serializers.ValidationError("For all rides, end latitude and longitude must be specified.")
      
        return data