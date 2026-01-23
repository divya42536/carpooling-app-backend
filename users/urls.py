from django.urls import path
from users import views

urlpatterns= [
    path('hello/',views.say_hello)

]