import pytest
from django.utils import timezone
from rides.models import Ride
from users.models import Person
from ratings.models import Rating
from datetime import timedelta, datetime
from django.core.exceptions import ValidationError


@pytest.mark.django_db
def test_create_rating_with_comment():
    # Arrange: create a Person
    person = Person.objects.create(
        username="divya123",
        password="pass123",
        first_name="Divya",
        last_name="Potnuru",
        email="divya@example.com",
        phone="1234567890"
    )

    # Arrange: create a Ride
    earliest_time = timezone.now()
    latest_time = earliest_time + timedelta(hours=1)
    ride = Ride.objects.create(
        carpooler=person,
        ride_type="OFFER",
        start_location="CityA",
        end_location="CityB",
        earliest_time=earliest_time,
        latest_time=latest_time,
        available_seats=2
    )

    # Act: create a Rating
    rating = Rating.objects.create(
        ride=ride,
        score=5,
        comment="Great ride!"
    )

    # Assert
    assert rating.score == 5
    assert rating.comment == "Great ride!"
    assert rating.ride == ride
    assert str(rating) == "Rating: 5"


@pytest.mark.django_db
def test_create_rating_without_comment():
    # Arrange
    person = Person.objects.create(
        username="user_no_comment",
        password="pass123",
        first_name="User",
        last_name="NoComment",
        email="nocomment@example.com",
        phone="1112223333"
    )

    earliest_time = timezone.now()
    latest_time = earliest_time + timedelta(hours=1)
    ride = Ride.objects.create(
        carpooler=person,
        ride_type="REQUEST",
        start_location="CityX",
        end_location="CityY",
        earliest_time=earliest_time,
        latest_time=latest_time
    )

    # Act
    rating = Rating.objects.create(
        ride=ride,
        score=4
        # no comment provided
    )

    # Assert
    assert rating.comment == ""  # blank is allowed
    assert rating.score == 4
    assert rating.ride == ride
    assert str(rating) == "Rating: 4"


@pytest.mark.django_db
def test_rating_score_validation():
    # Arrange
    person = Person.objects.create(
        username="user_invalid_score",
        password="pass123",
        first_name="Invalid",
        last_name="Score",
        email="invalidscore@example.com",
        phone="9998887777"
    )

    earliest_time = timezone.now()
    latest_time = earliest_time + timedelta(hours=1)
    ride = Ride.objects.create(
        carpooler=person,
        ride_type="OFFER",
        start_location="StartCity",
        end_location="EndCity",
        earliest_time=earliest_time,
        latest_time=latest_time,
        available_seats=1
    )

    # Act + Assert
    rating = Rating(
        ride=ride,
        score=6  # assuming max should be 5, min 1
    )
    
    with pytest.raises(ValidationError):
        rating.full_clean()


