from django.contrib import admin

# Register your models here.
@admin.register(Ride)
class Ride(admin.ModelAdmin):
    list_display = (
        "from",
        "to",
        )