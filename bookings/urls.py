from django.urls import path
from .views import book_ride, confirm_booking, cancel_booking, reject_booking

urlpatterns = [
    path('rides/<int:ride_id>/bookings/<int:person_id>/', book_ride, name="book-ride"),
    path('bookings/<int:booking_id>/confirm/<int:person_id>/', confirm_booking, name="confirm-booking"),
    path('bookings/<int:booking_id>/cancel/<int:person_id>/', cancel_booking, name="cancel-booking"),
    path('bookings/<int:booking_id>/reject/<int:person_id>/', reject_booking, name="reject-booking"),
]
