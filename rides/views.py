from django.shortcuts import render
from .models import Ride
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class RideListView(APIView):
    def get(self, request):
        rides= Ride.objects.all()
        return Response({"rides": rides.count()})
