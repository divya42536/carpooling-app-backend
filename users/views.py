from django.shortcuts import render
from django.http import HttpResponse
from .models import Rider
from .models import Driver
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class RiderInfo(APIView):
    def post(self, request):
        rider = Rider.objects.create(
            first_name=request.data.get("first_name"),
            last_name=request.data.get("last_name"),
            email=request.data.get("email"),
            phone=request.data.get("phone"),
        )

        return Response(
            {
                "message": "Rider created successfully",
                "rider_id": rider.id
            },
            status=status.HTTP_201_CREATED
        )
class DriverInfo(APIView):
    def post(self, request):
        driver = Driver.objects.create(
            first_name=request.data.get("first_name"),
            last_name=request.data.get("last_name"),
            email=request.data.get("email"),
            phone=request.data.get("phone"),
            car_number=request.data.get("car_number"),
            driver_license=request.data.get("driver_license"),
        )

        return Response(
            {
                "message": "Driver created successfully",
                "driver_id": driver.id
            },
            status=status.HTTP_201_CREATED
        )

    

    

