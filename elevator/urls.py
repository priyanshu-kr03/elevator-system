from django.urls import path, include

from .api_views import BuildingConfigurationCreateAPIView

urlpatterns = [
    path('building-configuration/', BuildingConfigurationCreateAPIView.as_view(), name='building-configuration-create')
]
