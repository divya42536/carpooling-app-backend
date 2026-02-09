from django.shortcuts import render
from .models import Ride
# from .models import Booking
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RideSerializer
from rest_framework import status
from datetime import datetime
from users.models import Person
from bookings.models import Booking
# Create your views here.
# logic handling path is : Request → View → Model → View → Response

# class RideListView(APIView):
#     def get(self, request):
#         rides= Ride.objects.all()
#         return Response({"rides": rides.count()})
    
# class BookRideView(APIView):
#     def post(self, request, ride_id):
#         Booking.Objects.create(
#             rider=request.User,
#             ride_id= ride_id,
#             status="CONFIRMED"
#         )
#         return Response({"message": "Ride booked"})

@api_view(['POST', 'GET']) 
def ride_list(request):
    if request.method == 'POST':
        serializer = RideSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        rides = Ride.objects.all()
        serializer = RideSerializer(rides, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE'])
def get_ride_detail(request,pk):
    try:
        ride = Ride.objects.get(id=pk)
    except Ride.DoesNotExist:
        return Response(
            {"error": "Ride not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    if request.method == 'GET':
        serializer = RideSerializer(ride, many=False)
        return Response(serializer.data)
    # elif request.method == 'PUT':
    #     serializer = RideSerializer(ride, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        ride.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def search_ride(request):
    search_start_location = request.query_params.get('start_location')
    search_end_location = request.query_params.get('end_location')
    search_earliest_datetime = request.query_params.get('earliest_datetime')
    search_latest_datetime = request.query_params.get('latest_datetime')
    search_ride_type = request.query_params.get('ride_type')

    if not all([search_start_location, search_end_location, search_earliest_datetime, search_latest_datetime, search_ride_type]):
        return Response(
            {"error": "All search parameters must be provided."},
            status=status.HTTP_400_BAD_REQUEST
        )
    try:
        # search_earliest_datetime = datetime.fromisoformat(search_earliest_datetime)
        # search_latest_datetime = datetime.fromisoformat(search_latest_datetime)
        search_earliest_datetime = datetime.fromisoformat(search_earliest_datetime.replace("Z", "+00:00"))
        search_latest_datetime = datetime.fromisoformat(search_latest_datetime.replace("Z", "+00:00"))
    except ValueError:
        return Response(
            {"error": "Invalid datetime format. Use ISO format."},
            status=status.HTTP_400_BAD_REQUEST
        )

    # If all parameters are provided, proceed with the search logic
    rides = Ride.objects.filter(
        start_location=search_start_location,
        end_location=search_end_location,
        earliest_time__lte=search_latest_datetime,
        latest_time__gte=search_earliest_datetime,
        ride_type=search_ride_type
    )

    if search_ride_type == 'OFFER':
        rides = rides.filter(available_seats__gt=0)

    serializer = RideSerializer(rides, many=True)
    return Response(serializer.data)




@api_view(['POST'])
def accept_ride_request(request, ride_request_id):
    driver_id = request.data.get("userId")

    if not driver_id:
        return Response({"error": "driverId is required"}, status=400)

    try:
        ride_request = Ride.objects.get(
            id=ride_request_id,
            ride_type="REQUEST"
        )
        driver = Person.objects.get(id=driver_id)
    except (Ride.DoesNotExist, Person.DoesNotExist):
        return Response({"error": "Ride request or driver not found"}, status=404)

    if ride_request.carpooler == driver:
        return Response({"error": "Cannot accept your own request"}, status=400)
    if ride_request.status != "PENDING":
        return Response({"error": "Request already handled"}, status=400)

    if ride_request.available_seats <= 0:
        return Response(
            {"error": "No seats available"},
            status=400
        )
    ride_request.available_seats -= 1
    ride_request.save()
    # create booking
    booking = Booking.objects.create(
        ride=ride_request,
        rider=ride_request.carpooler,
        status=Booking.STATUS_CONFIRMED
    )

    return Response({
        "bookingId": booking.id,
        "status": booking.status,
        "available_seats": ride_request.available_seats
    }, status=201)

@api_view(['POST'])
def reject_ride_request(request, ride_request_id):
    driver_id = request.data.get("userId")

    if not driver_id:
        return Response({"error": "driverId is required"}, status=400)

    # no booking created
    # optionally log rejection for analytics

    return Response({"message": "Ride request rejected"}, status=200)
