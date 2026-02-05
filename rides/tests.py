from django.test import TestCase
from users.models import Person
from rides.models import Ride
import pytest
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
from django.utils import timezone

@pytest.mark.django_db
def test_ride_data():
    person = Person.objects.create(
        username="divya123",
        password="password123",
        first_name="Divya",
        last_name="Potnuru",
        email="divya@example.com",
        phone="1234567890"
    )
    earliest_time = timezone.now()
    latest_time = earliest_time + timedelta(hours=1)
    ride = Ride.objects.create(
        carpooler=person,
        ride_type="OFFER",
        start_location="Issaquah",
        end_location="Bothell",
        earliest_time= earliest_time ,
        latest_time=latest_time,
        available_seats=1
    )

    # Act: create a dictionary like your API response
    ride_dict = {
        "id": ride.id,
        "ride_type": ride.ride_type,
        "start_location": ride.start_location,
        "end_location": ride.end_location,
        "earliest_time": ride.earliest_time.isoformat(),
        "latest_time": ride.latest_time.isoformat(),
        "available_seats": ride.available_seats,
        "created_at": ride.created_at.isoformat(),
        "carpooler": ride.carpooler.id
    }

    # Assert
    assert ride_dict["ride_type"] == "OFFER"
    assert ride_dict["start_location"] == "Issaquah"
    assert ride_dict["end_location"] == "Bothell"
    assert ride_dict["available_seats"] == 1
    assert ride_dict["carpooler"] == person.id


#ride type must be Offer or Request
@pytest.mark.django_db
def test_ride_inavalid_type():
    person = Person.objects.create(
        username="user_invalid",
        password="pass123",
        first_name="Invalid",
        last_name="User",
        email="invalid@example.com",
        phone="1231231234"
    )

    start_time = datetime.now()
    end_time = start_time + timedelta(hours=1)

    ride = Ride(
        carpooler=person,
        ride_type="INVALID",  # not OFFER or REQUEST
        start_location="A",
        end_location="B",
        earliest_time=start_time,
        latest_time=end_time
    )

    # Act + Assert
    with pytest.raises(ValidationError):
        ride.full_clean()  


#Available seats can not be be None
@pytest.mark.django_db
def test_ride_available_seats_not_none_Offer():
    # Arrange
    person = Person.objects.create(
        username="driver1",
        password="pass123",
        first_name="Driver",
        last_name="One",
        email="driver1@example.com",
        phone="1112223333"
    )

    earliest_time = timezone.now()
    latest_time = earliest_time + timedelta(hours=1)

    # Act + Assert
    ride = Ride(
        carpooler=person,
        ride_type="OFFER",
        start_location="CityA",
        end_location="CityB",
        earliest_time=earliest_time,
        latest_time=latest_time,
        available_seats=None
    )

    # Assert
    with pytest.raises(ValidationError):
        ride.full_clean() 


#latest time cannot be less than earliest time 
@pytest.mark.django_db
def test_ride_time_validation():
    # Arrange
    person = Person.objects.create(
        username="user_time",
        password="pass123",
        first_name="Time",
        last_name="User",
        email="time@example.com",
        phone="9998887777"
    )

    start_time = datetime.now()
    end_time = start_time - timedelta(hours=1)

    ride = Ride(
        carpooler=person,
        ride_type="REQUEST",
        start_location="StartCity",
        end_location="EndCity",
        earliest_time=start_time,
        latest_time=end_time
    )

    # Act + Assert
    with pytest.raises(ValidationError):
        ride.full_clean()