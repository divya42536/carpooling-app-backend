from django.urls import path
from .views import ride_list_create,  get_ride_detail

urlpatterns= [
    path('rides/', ride_list_create, name='ride-list-create'),
    # path('rides/', get_ride_list, name='get-ride-list'),
    path('rides/<int:pk>/', get_ride_detail, name='get-ride-detail'),
]