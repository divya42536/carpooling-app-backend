from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Ride
from .serializers import RatingSerializer
from rides.serializers import RideSerializer
class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer

    @action(detail=True, methods=['post'])
    def rate(self, request, *args, **kwargs):
        ride = self.get_object()
        serializer = RatingSerializer(
            data=request.data,
            context={'ride': ride, 'request': request}
        )
        serializer.is_valid(raise_exception=True)
        rating = serializer.save()
        return Response(RatingSerializer(rating).data, status=status.HTTP_201_CREATED)
