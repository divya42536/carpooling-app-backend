from django.shortcuts import render
from django.http import HttpResponse
from .models import Rider
from .models import Driver
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
#    def post(self, request, ride_id):
#         Booking.Objects.create(
#             rider=request.User,
#             ride_id= ride_id,
#             status="CONFIRMED"
#         )
#         return Response({"message": "Ride booked"})

class RiderInfo(APIView):
    def post(self, request, rider_id,FirstName,LastName,Email,Phone):
        Rider.Objects.create(
            rider=request.Rider,
            rider_id= rider_id,
            FirstName= Rider.FirstName,
            LastName= Rider.LastName,
            Email= Rider.Email,
            Phone= Rider.Phone
        )
        return Response({"message": "Rider details"})
