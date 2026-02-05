import pytest
from django.utils import timezone
from datetime import timedelta
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from users.models import Person
from rides.models import Ride
from bookings.models import Booking

@pytest.mark.django_db
def test_create_booking():
    # Arrange: create a rider and a ride
    rider = Person.objects.create(
        username="rider1",
        password="pass123",
        first_name="Rider",
        last_name="One",
        email="rider1@example.com",
        phone="1112223333"
    )

    driver = Person.objects.create(
        username="driver1",
        password="pass123",
        first_name="Driver",
        last_name="One",
        email="driver1@example.com",
        phone="4445556666"
    )

    earliest_time = timezone.now()
    latest_time = earliest_time + timedelta(hours=1)
    ride = Ride.objects.create(
        carpooler=driver,
        ride_type="OFFER",
        start_location="CityA",
        end_location="CityB",
        earliest_time=earliest_time,
        latest_time=latest_time,
        available_seats=2
    )

    # Act: create a booking
    booking = Booking.objects.create(rider=rider, ride=ride)

    # Assert
    assert booking.rider == rider
    assert booking.ride == ride
    assert booking.status == "pending"
    assert str(booking) == f"Booking({rider}, {ride}, pending)"


@pytest.mark.django_db
def test_booking_default_status():
    # Arrange
    rider = Person.objects.create(
        username="rider2",
        password="pass123",
        first_name="Rider",
        last_name="Two",
        email="rider2@example.com",
        phone="2223334444"
    )
    driver = Person.objects.create(
        username="driver2",
        password="pass123",
        first_name="Driver",
        last_name="Two",
        email="driver2@example.com",
        phone="5556667777"
    )

    earliest_time = timezone.now()
    latest_time = earliest_time + timedelta(hours=2)
    ride = Ride.objects.create(
        carpooler=driver,
        ride_type="OFFER",
        start_location="CityX",
        end_location="CityY",
        earliest_time=earliest_time,
        latest_time=latest_time,
        available_seats=1
    )

    booking = Booking.objects.create(rider=rider, ride=ride)

    # Assert default status
    assert booking.status == Booking.STATUS_PENDING


@pytest.mark.django_db
def test_unique_booking_constraint():
    # Arrange
    rider = Person.objects.create(
        username="rider3",
        password="pass123",
        first_name="Rider",
        last_name="Three",
        email="rider3@example.com",
        phone="3334445555"
    )
    driver = Person.objects.create(
        username="driver3",
        password="pass123",
        first_name="Driver",
        last_name="Three",
        email="driver3@example.com",
        phone="6667778888"
    )

    earliest_time = timezone.now()
    latest_time = earliest_time + timedelta(hours=1)
    ride = Ride.objects.create(
        carpooler=driver,
        ride_type="OFFER",
        start_location="CityStart",
        end_location="CityEnd",
        earliest_time=earliest_time,
        latest_time=latest_time,
        available_seats=3
    )

    Booking.objects.create(rider=rider, ride=ride)

    # Act + Assert: creating another booking with same rider + ride should fail
    with pytest.raises(IntegrityError):
        Booking.objects.create(rider=rider, ride=ride)


@pytest.mark.django_db
def test_booking_status_choices_validation():
    # Arrange
    rider = Person.objects.create(
        username="rider4",
        password="pass123",
        first_name="Rider",
        last_name="Four",
        email="rider4@example.com",
        phone="4445556666"
    )
    driver = Person.objects.create(
        username="driver4",
        password="pass123",
        first_name="Driver",
        last_name="Four",
        email="driver4@example.com",
        phone="7778889999"
    )

    earliest_time = timezone.now()
    latest_time = earliest_time + timedelta(hours=1)
    ride = Ride.objects.create(
        carpooler=driver,
        ride_type="OFFER",
        start_location="CityStart",
        end_location="CityEnd",
        earliest_time=earliest_time,
        latest_time=latest_time,
        available_seats=2
    )

    # Act
    booking = Booking(rider=rider, ride=ride, status="invalid_status")

    # Assert
    with pytest.raises(ValidationError):
        booking.full_clean()
