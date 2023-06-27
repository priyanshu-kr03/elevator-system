from django.urls import path, include

from .api_views import BuildingConfigurationCreateAPIView, ElevatorListAPIView, RequestElevatorView

urlpatterns = [
    path('building-configuration/', BuildingConfigurationCreateAPIView.as_view(), name='building-configuration-create'),
    path('request-elevator/', RequestElevatorView.as_view(), name='request-elevator'),
    path('elevators-status/<uuid:building>', ElevatorListAPIView.as_view(), name='elevator-status-list-view'),
]
