from django.urls import path, include
from .views import create_rating, get_ratings, ratings_for_ride, delete_rating

urlpatterns = [
    path('',get_ratings),
    path('create/', create_rating, name='create_rating'),
    path('ride/<int:ride_id>/', ratings_for_ride),
    path('<int:rating_id>/', delete_rating)
    
    
]