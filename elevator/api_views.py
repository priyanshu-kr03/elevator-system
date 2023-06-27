from rest_framework.generics import ListCreateAPIView, ListAPIView

from .models import BuildingConfiguration, Elevator
from .serializers import BuildingConfigurationSerializer, ElevatorSerializer


class BuildingConfigurationCreateAPIView(ListCreateAPIView):
    queryset = BuildingConfiguration.objects.all()
    serializer_class = BuildingConfigurationSerializer


class ElevatorListAPIView(ListAPIView):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

    def get_queryset(self):
        building_uuid = self.kwargs['building']
        queryset = Elevator.objects.filter(building__id=building_uuid)
        return queryset
