from rest_framework import status
from rest_framework.response import Response
from .serializers import RatingSerializer
from rest_framework.decorators import api_view
from .models import Rating


@api_view(['POST'])
def create_rating(request):
    serializer= RatingSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(
        {"message":"Rating submitted successfully"},
        status=status.HTTP_201_CREATED
    )
@api_view(['GET'])
def get_ratings(request):
    ratings= Rating.objects.all().order_by('-created_at')
    serializer = RatingSerializer(ratings, many=True)
    return Response(serializer.data)

# get rating for a specific ride

@api_view(['GET'])
def ratings_for_ride(request,ride_id):
    ratings= Rating.objects.filter(ride_id=ride_id)
    serializer = RatingSerializer(ratings, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_rating(request, rating_id):
    try:
        rating = Rating.objects.get(pk=rating_id)
    except Rating.DoesNotExist:
        return Response({"error": "Rating not found"}, status=404)
    rating.delete()
    return Response({"message": "Rating deleted"}, status=status.HTTP_204_NO_CONTENT)
    







# @api_view(['POST'])

# @permission_classes([IsAuthenticated])

# def create_rating(request):
#     serializer = RatingSerializer(
#         data=request.data,
#         context={'request': request}
#     )

#     serializer.is_valid(raise_exception=True)
#     rating= serializer.save()

#     return Response(
#         {
#             "message": "Rating submitted successfully"
#         },
#         status=status.HTTP_201_CREATED
#     )

# def get_user_from_token(request):
#     auth_header = request.headers.get("Authorization")  # e.g., "Token <token>"
#     if not auth_header:
#         return None
#     token = auth_header.replace("Token ", "")
#     try:
#         return Person.objects.get(token=token)
#     except Person.DoesNotExist:
#         return None

# @api_view(['POST'])
# def create_rating(request):
#     user = get_user_from_token(request)
#     if not user:
#         return Response({"detail": "Authentication credentials were not provided."}, status=401)

#     # Add user info to serializer context if needed
#     serializer = RatingSerializer(data=request.data, context={'user': user})
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response({"message": "Rating submitted successfully"}, status=status.HTTP_201_CREATED)