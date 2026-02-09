from rest_framework import serializers
from django.contrib.auth.hashers import check_password
from .models import Person
from django.contrib.auth.hashers import make_password

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
        extra_kwargs = {
            "password": {"write_only": True}
        }

    # def validate(self, data):
    #     is_driver = data.get("is_driver", False)
    #     car_number = data.get("car_number")
    #     driver_license = data.get("driver_license")

    #     if is_driver == True:

    #         if not car_number or not driver_license:
    #             raise serializers.ValidationError({
    #                 "car_number": "Required for drivers",
    #                  "driver_license": "Required for drivers"
    #            } )

    #     return data

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)
    
    def average_rating(self):
        ratings = self.ratings_received.all()
        if ratings.exists():
            return sum(r.score for r in ratings) / ratings.count()
        return None

# class LoginSerializer(serializers.Serializer):
#     username= serializers.CharField()
#     password=serializers.CharField(write_only=True)

#     def validate(self, data):
#         username= data.get("username")
#         password= data.get("password")

#         try:
#             user = Person.objects.get(username=username)
#         except Person.DoesNotExist:
#             raise serializers.ValidationError("Invalid username or password")

#         if not check_password(password, user.password):
#             raise serializers.ValidationError("Invalid username or password")

#         data["user"] = user
#         return data

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
        
        # Debug logging
        print(f"Login attempt - Username: '{username}' (length: {len(username)})")
        print(f"Login attempt - Password: '{password}' (length: {len(password)})")

        try:
            user = Person.objects.get(username=username)
            print(f"User found: {user.username}")
            print(f"Stored password hash: {user.password[:50]}...")
        except Person.DoesNotExist:
            print("User not found in database")
            raise serializers.ValidationError("Invalid username or password")

        password_match = check_password(password, user.password)
        print(f"Password match result: {password_match}")
        
        if not password_match:
            print("Password check failed!")
            raise serializers.ValidationError("Invalid username or password")

        data["user"] = user
        return data
    

class RegisterSerializer(serializers.ModelSerializer):
    confirmpassword = serializers.CharField(write_only=True)

    class Meta:
        model = Person
        fields = ['username', 'password', 'confirmpassword', 'first_name', 'last_name', 'email', 'phone']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def validate_username(self, value):

        if Person.objects.filter(username=value).exists():
            raise serializers.ValidationError("A user with this username already exists")
        return value

    def validate_email(self, value):
        if Person.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists")
        return value

    def validate(self, data):
        if data['password'] != data['confirmpassword']:
            raise serializers.ValidationError({"password": "Password and confirm password do not match"})
        return data

    def create(self, validated_data):
        validated_data.pop('confirmpassword')
        validated_data['password'] = make_password(validated_data['password'])
        return Person.objects.create(**validated_data)