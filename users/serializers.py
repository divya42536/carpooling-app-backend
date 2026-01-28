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

    def validate(self, data):
        is_driver = data.get("is_driver", False)
        car_number = data.get("car_number")
        driver_license = data.get("driver_license")

        if is_driver == True:

            if not car_number or not driver_license:
                raise serializers.ValidationError({
                    "car_number": "Required for drivers",
                     "driver_license": "Required for drivers"
               } )

        return data

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)

class LoginSerializer(serializers.Serializer):
    username= serializers.CharField()
    password=serializers.CharField(write_only=True)

    def validate(self, data):
        username= data.get("username")
        password= data.get("password")

        try:
            user = Person.objects.get(username=username)
        except Person.DoesNotExist:
            raise serializers.ValidationError("Invalid username or password")

        if not check_password(password, user.password):
            raise serializers.ValidationError("Invalid username or password")

        data["user"] = user
        return data