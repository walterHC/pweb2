from django.urls import path
from . import views


urlpatterns = [
        path('addDestination', views.addDestination, name="addDestination")
    ]
