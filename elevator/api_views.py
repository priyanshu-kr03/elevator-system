from rest_framework.generics import ListCreateAPIView

from .models import BuildingConfiguration
from .serializers import BuildingConfigurationSerializer


class BuildingConfigurationCreateAPIView(ListCreateAPIView):
    queryset = BuildingConfiguration.objects.all()
    serializer_class = BuildingConfigurationSerializer
