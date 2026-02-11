from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rides.models import Ride
from users.models import Person
from .models import Booking
from .serializers import BookingSerializer, BookingListSerializer


@api_view(['POST'])
def book_ride(request, ride_id):
    #get ride and person details and validate
    person_id = int(request.data.get('userId'))

    if not person_id:
        return Response(
            {"error": "userId is required"},
            status=status.HTTP_400_BAD_REQUEST
        )
    try:
        ride = Ride.objects.get(id=ride_id)
        person = Person.objects.get(id=person_id)
    except (Ride.DoesNotExist, Person.DoesNotExist):
        return Response({"error":"Ride or person not found"}, status=status.HTTP_400_BAD_REQUEST)
    
    # check whether carpooler and rider are same
    if ride.carpooler == person :
        return Response({"error":"You cannot book your own ride"}, status=status.HTTP_400_BAD_REQUEST)
    
    #check whether there is already abooking in your name
    if Booking.objects.filter(ride=ride, rider=person).exists():
        return Response({"error": "You have already booked this ride"}, status=status.HTTP_400_BAD_REQUEST)
    
#   if ride.ride_type == "OFFER" and not ride.carpooler != person:  # rider booking OFFER
#         pass  
#   elif ride.ride_type == "REQUEST" and ride.carpooler == person:  # driver booking REQUEST
#         pass  

    serializer = BookingSerializer(data={'ride': ride.id}, context={'rider': person})
    if serializer.is_valid():
        booking = serializer.save(rider=person, status=Booking.STATUS_PENDING)  # assign rider here
        # if ride.ride_type == "OFFER":
        #     ride.available_seats -= 1
        #     ride.save()
        return Response(BookingSerializer(booking).data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['PATCH'])
def confirm_booking(request, booking_id):
    person_id = int(request.data.get('userId'))
    if not person_id:
        return Response(
            {"error": "userId is required"},
            status=status.HTTP_400_BAD_REQUEST
        )
    try:
        booking = Booking.objects.get(id=booking_id)
        person = Person.objects.get(id=person_id)
    except (Booking.DoesNotExist, Person.DoesNotExist):
        return Response({"error": "Booking or person not found"}, status=status.HTTP_404_NOT_FOUND)

    ride = booking.ride
    if ride.carpooler != person:
        return Response({"error": "You are not the driver of this ride"}, status=status.HTTP_403_FORBIDDEN)
    if booking.status != Booking.STATUS_PENDING:
        return Response({"error": f"Booking is not pending, It is {booking.status}"}, status=status.HTTP_400_BAD_REQUEST)
    if ride.ride_type == "OFFER" and ride.available_seats <= 0:
        return Response({"error": "No available seats for this ride."}, status=status.HTTP_400_BAD_REQUEST)

    booking.status = Booking.STATUS_CONFIRMED
    booking.save()
    if ride.ride_type == "OFFER":
        ride.available_seats -= 1
        ride.save()
    return Response({
        "booking_id": booking.id,
        "status": booking.status,
        "remaining_seats": ride.available_seats
    }, status=200)

@api_view(['PATCH'])
def cancel_booking(request, booking_id):
    person_id = int(request.data.get('userId'))
    if not person_id:
        return Response(
            {"error": "userId is required"},
            status=status.HTTP_400_BAD_REQUEST
        )
    try:
        booking = Booking.objects.get(id=booking_id)
        person = Person.objects.get(id=person_id)
    except (Booking.DoesNotExist, Person.DoesNotExist):
        return Response({"error": "Booking or person not found"}, status=status.HTTP_404_NOT_FOUND)

    if person_id not in [booking.rider.id, booking.ride.carpooler.id]:
        return Response({"error": "You are not authorized to cancel this booking"}, status=status.HTTP_403_FORBIDDEN)

    if booking.status != Booking.STATUS_CONFIRMED:
        return Response(
            {"error": "Only confirmed bookings can be cancelled"},
            status=400
        )

    booking.status = Booking.STATUS_CANCELLED
    booking.save()

    booking.ride.available_seats += 1
    booking.ride.save()
    return Response({"message": "Booking cancelled"}, status=200)

@api_view(['PATCH'])
def reject_booking(request, booking_id):
    person_id = int(request.data.get('userId'))
    if not person_id:
        return Response(
            {"error": "userId is required"},
            status=status.HTTP_400_BAD_REQUEST
        )
    try:
        booking = Booking.objects.get(id=booking_id)
        person = Person.objects.get(id=person_id)
    except (Booking.DoesNotExist, Person.DoesNotExist):
        return Response({"error": "Booking or person not found"}, status=status.HTTP_404_NOT_FOUND)

    ride = booking.ride
    if ride.carpooler != person:
        return Response({"error": "You are not the driver of this ride"}, status=status.HTTP_403_FORBIDDEN)
    if booking.status != Booking.STATUS_PENDING:
        return Response({"error": f"Booking is not pending, It is {booking.status}"}, status=status.HTTP_400_BAD_REQUEST)

    booking.status = Booking.STATUS_REJECTED
    booking.save()
    
    return Response({
        "booking_id": booking.id,
        "status": booking.status
    }, status=200)


@api_view(['GET'])
def rider_commutes(request, person_id):
    # Logic to retrieve and return the rides for a specific rider
    try:
        person = Person.objects.get(id=person_id)
    except Person.DoesNotExist:
        return Response({"error": "Person not found"}, status=404) 
       
    bookings = Booking.objects.filter(rider_id=person_id)

    serializer = BookingListSerializer(
        bookings,
        many=True,
        context={"role": "rider"}
    )
    return Response(serializer.data)

@api_view(['GET'])
def driver_commutes(request, person_id):
    # Logic to retrieve and return the rides for a specific driver
    try:
        person = Person.objects.get(id=person_id)
    except Person.DoesNotExist:
        return Response({"error": "Person not found"}, status=404)    
    bookings = Booking.objects.filter(
        ride__carpooler_id=person_id
    )

    serializer = BookingListSerializer(
        bookings,
        many=True,
        context={"role": "driver"}
    )
    return Response(serializer.data)