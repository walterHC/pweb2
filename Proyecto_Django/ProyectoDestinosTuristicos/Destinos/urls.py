from django.urls import path
from . import views 


urlpatterns = [
        path('addDestination', views.addDestination, name="addDestination"),
        path('insertNewDestination', views.insertNewDestination, name="insertNewDestination"),
        path('destinationList', views.destinationList, name="listing")
    ]
