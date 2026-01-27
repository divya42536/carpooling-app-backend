from django.contrib import admin
from .models import Ride
from .models import Booking

# Register your models here.
@admin.register(Ride)
class Ride(admin.ModelAdmin):
    list_display = (
        "from",
        "to",
        )