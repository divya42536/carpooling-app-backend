from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonViewSet, LoginView, create_ride_for_person, delete_a_user, RegisterView

router = DefaultRouter()
router.register(r'users', PersonViewSet, basename='users')


urlpatterns = [
    path('', include(router.urls)),

    path("login/", LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name='register'),
    path('<int:person_id>/', delete_a_user),
    path("persons/<int:person_id>/rides/", create_ride_for_person, name="create_ride_for_person"),
    
]