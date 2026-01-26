from django.shortcuts import render
from .models import Ride
from .models import Booking
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
# logic handling path is : Request → View → Model → View → Response

class RideListView(APIView):
    def get(self, request):
        rides= Ride.objects.all()
        return Response({"rides": rides.count()})
    
class BookRideView(APIView):
    def post(self, request, ride_id):
        Booking.Objects.create(
            rider=request.User,
            ride_id= ride_id,
            status="CONFIRMED"
        )
        return Response({"message": "Ride booked"})