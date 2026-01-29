from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ride_list,  get_ride_detail,search_ride
# from ratings.views import RideViewSet

# router = DefaultRouter()
# router.register(r'rides', RideViewSet, basename='ride')

urlpatterns= [
    path('rides/', ride_list, name='ride-list'),
    # path('rides/', get_ride_list, name='get-ride-list'),
    path('rides/<int:pk>/', get_ride_detail, name='get-ride-detail'),
    path('rides/search/', search_ride, name='search-rides'),
    # path('', include(router.urls)),
]