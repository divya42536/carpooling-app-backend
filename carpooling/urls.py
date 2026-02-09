"""
URL configuration for carpooling project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.http import JsonResponse

# Optional: API root view to list all endpoints
def api_root(request):
    return JsonResponse({
        "users": "/api/users/",
        "rides": "/api/rides/",
        "ratings": "/api/ratings/",
        "bookings": "/api/bookings/",
    })

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # App endpoints
    path('api/users/', include('users.urls')),
    path('api/rides/', include('rides.urls')),
    path('api/ratings/', include('ratings.urls')),
    path('api/bookings/', include('bookings.urls')),

    # Redirect /api/ to API root JSON
    path('api/', api_root),  # now visiting /api/ returns JSON of all endpoints

    # Optional: redirect root '/' to /api/ or a welcome page
    path('', RedirectView.as_view(url='/api/', permanent=False)),
]



# from django.contrib import admin
# from django.urls import path, include
# from django.views.generic import RedirectView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/users/', include('users.urls')),
#     path('api/rides/', include('rides.urls')),
#     path('api/ratings/', include('ratings.urls')),
#     path('api/bookings/', include('bookings.urls')),

#     path('', RedirectView.as_view(url='/api/', permanent=False)),
    
    
# ]
