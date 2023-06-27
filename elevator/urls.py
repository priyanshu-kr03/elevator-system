from django.urls import path, include

from .api_views import BuildingConfigurationCreateAPIView, ElevatorListAPIView

urlpatterns = [
    path('building-configuration/', BuildingConfigurationCreateAPIView.as_view(), name='building-configuration-create'),
    path('elevators-status/<uuid:building>', ElevatorListAPIView.as_view(), name='elevator-status-list-view')
]
