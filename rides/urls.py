from django.urls import path
from .views import ride_list,  get_ride_detail,search_ride

urlpatterns= [
    path('rides/', ride_list, name='ride-list'),
    # path('rides/', get_ride_list, name='get-ride-list'),
    path('rides/<int:pk>/', get_ride_detail, name='get-ride-detail'),
    path('rides/search/', search_ride, name='search-rides'),
]