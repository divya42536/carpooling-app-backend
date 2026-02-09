from django.urls import path
from .views import book_ride, confirm_booking, cancel_booking, driver_commutes, reject_booking, rider_commutes

urlpatterns = [
    path('rides/<int:ride_id>/bookings/', book_ride, name="book-ride"),
    path('bookings/<int:booking_id>/confirm/', confirm_booking, name="confirm-booking"),
    path('bookings/<int:booking_id>/cancel/', cancel_booking, name="cancel-booking"),
    path('bookings/<int:booking_id>/reject/', reject_booking, name="reject-booking"),
    path('bookings/rider/<int:person_id>/', rider_commutes),
    path('bookings/driver/<int:person_id>/', driver_commutes),
]
