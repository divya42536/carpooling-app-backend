from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonViewSet, LoginView, create_ride_for_person, delete_a_user

router = DefaultRouter()
router.register(r'persons', PersonViewSet, basename='person')


urlpatterns = [
    path('', include(router.urls)),

    path("login/", LoginView.as_view(), name="login"),
    path('users/<int:person_id>/', delete_a_user),
    path("persons/<int:person_id>/rides/", create_ride_for_person, name="create_ride_for_person"),
]