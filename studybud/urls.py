from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Assuming your app's name is 'my_app' (replace if different)
from base import views  # Import views from your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),  # Corrected path for root URL
]