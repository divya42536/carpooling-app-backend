from django.shortcuts import render
from .models import Ride
# from .models import Booking
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RideSerializer
from rest_framework import status

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

@api_view(['POST']) 
def ride_list_create(request):
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

# @api_view(['GET'])
# def get_ride_list(request):
#     rides = Ride.objects.all()
#     serializer = RideSerializer(rides, many=True)
#     return Response(serializer.data)
@api_view(['GET','PUT', 'DELETE'])
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
    elif request.method == 'PUT':
        serializer = RideSerializer(ride, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        ride.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET'])
# def search_ride(request):
#     search_start_location = request.get