from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rides.models import Ride
from users.models import Person
from .models import Booking
from .serializers import BookingSerializer

# @api_view(['POST'])
# def book_ride(request, ride_id, person_id):
#     # Get the ride and person
#     try:
#         ride = Ride.objects.get(pk=ride_id)
#         person = Person.objects.get(pk=person_id)
#     except (Ride.DoesNotExist, Person.DoesNotExist):
#         return Response({"error": "Ride or person not found"}, status=status.HTTP_404_NOT_FOUND)

#     # Prevent booking own ride
#     if ride.carpooler == person:
#         return Response({"error": "You cannot book your own ride"}, status=status.HTTP_400_BAD_REQUEST)

#     # Prevent double booking
#     if Booking.objects.filter(ride=ride, rider=person).exists():
#         return Response({"error": "You have already booked this ride"}, status=status.HTTP_400_BAD_REQUEST)

#     # Role matching (optional, for OFFER/REQUEST)
#     if ride.ride_type == "OFFER" and not ride.carpooler != person:  # rider booking OFFER
#         pass  # okay
#     elif ride.ride_type == "REQUEST" and ride.carpooler == person:  # driver booking REQUEST
#         pass  # okay

#     #Use serializer to validate other data
#     serializer = BookingSerializer(data={'ride': ride.id})
#     if serializer.is_valid():
#         booking = serializer.save(rider=person)  # assign rider here

#         # Reduce seats for OFFER rides
#         if ride.ride_type == "OFFER":
#             ride.available_seats -= 1
#             ride.save()

#         return Response(BookingSerializer(booking).data, status=status.HTTP_201_CREATED)

#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)