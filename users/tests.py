from django.test import TestCase
from django.db import IntegrityError
from users.models import Person
from django.contrib.auth.hashers import check_password
import pytest

@pytest.mark.django_db
def test_person_fields():
    # Arrange
    new_person = Person(
        id=1,
        username="divya123",
        password="password123",
        first_name="Divya",
        last_name="Potnuru",
        email="divya@example.com",
        phone="1234567890",
        is_driver=True
    )

    # Act
    username = new_person.username
    is_driver = new_person.is_driver

    # Assert
    assert new_person.id == 1
    assert username == "divya123"
    assert is_driver is True


@pytest.mark.django_db
def test_person_missing_id():
    # Arrange
    new_person = Person(
        username="divya123",
        password="password123",
        first_name="Divya",
        last_name="Potnuru",
        email="divya@example.com",
        phone="1234567890"
    )

    # Act
    person_id = new_person.id

    # Assert
    assert person_id is None


@pytest.mark.django_db
def test_person_duplicate_username():
    # Arrange
    Person.objects.create(
        username="divya123",
        password="password123",
        first_name="Divya",
        last_name="Potnuru",
        email="divya1@example.com",
        phone="1234567890"
    )

    # Act + Assert

    with pytest.raises(IntegrityError):
        Person.objects.create(
            username="divya123",
            password="password456",
            first_name="Test",
            last_name="User",
            email="divya2@gmail.com",
            phone="0987654321"
        )


@pytest.mark.django_db
def test_person_duplicate_email():
    # Arrange
    Person.objects.create(
        username="user1",
        password="password123",
        first_name="User",
        last_name="One",
        email="test@example.com",
        phone="1111111111"
    )

    # Act + Assert
    with pytest.raises(IntegrityError):
        Person.objects.create(
            username="user2",
            password="password456",
            first_name="User",
            last_name="Two",
            email="test@example.com",  # duplicate email
            phone="2222222222"
        )
