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
    serializer = RideSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def ride_list_get(request):
    rides = Ride.objects.all()
    serializer = RideSerializer(rides, many=True)
    return Response(serializer.data)
@api_view(['GET','PUT', 'DELETE'])
def ride_detail(request,pk):
    ride = Ride.objects.get(pk=pk)

