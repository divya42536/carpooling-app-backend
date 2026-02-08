from rest_framework.viewsets import ModelViewSet
from .models import Person
from .serializers import PersonSerializer, LoginSerializer, RegisterSerializer
from rides.serializers import RideSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password, make_password

class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data["user"]
            return Response({
                "message": "Login successful",
                "user_id": user.id,
                "username": user.username,
                "password": user.password,
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def delete_a_user(request,person_id):
    try:
        person = Person.objects.get(pk=person_id)
    except Person.DoesNotExist:
        return Response({"error": "Person not found"}, status=404)
    person.delete()
    return Response({"message": "User deleted"}, status=status.HTTP_204_NO_CONTENT)
    



@api_view(['POST'])
def create_ride_for_person(request, person_id):
    try:
        person = Person.objects.get(pk=person_id)
    except Person.DoesNotExist:
        return Response({"error": "Person not found"}, status=404)
    serializer = RideSerializer(data=request.data)
    if serializer.is_valid():
        ride = serializer.save(carpooler=person)
        return Response(RideSerializer(ride).data, status=201)
    return Response(serializer.errors, status=400)


# @api_view(['POST'])
# def login(request):
#     username = request.data.get('username')
#     password = request.data.get('password')

#     if not username or not password:
#         return Response({"error": "Username and password required"}, status=400)

#     try:
#         user = Person.objects.get(username=username)
#     except Person.DoesNotExist:
#         return Response({"error": "Invalid credentials"}, status=400)

#     if not check_password(password, user.password):
#         return Response({"error": "Invalid credentials"}, status=400)

#     return Response({
#         "id": user.id,
#         "username": user.username,
#         "email": user.email,
#         "first_name": user.first_name,
#         "last_name": user.last_name
#     })

@api_view(['POST'])
def login(request):
    data= request.data
    username = request.data.get('username')
    # email = request.data.get('email')
    password = request.data.get('password')

    try:
        user = Person.objects.get(username=username)
    except Person.DoesNotExist:
        return Response({"error": "Invalid credentials"}, status=400)

    if not check_password(password, user.password):
        return Response({"error": "Invalid credentials"}, status=400)

    token = user.generate_token()
    return Response({"token": token, "user_id": user.id, "username": user.username})



class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            try:
                user = serializer.save()
            except Exception as e:
                return Response({
                    "message": "Registration successful",
                    "user":{
                    "FirstName": user.first_name,
                    "LastName": user.last_name,
                    "UserName": user.username,
                    "Phone": user.phone,
                    "EmailID": user.email,
                    
                    }
                }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)