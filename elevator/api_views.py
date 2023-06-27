import random

from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

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


class RequestElevatorView(APIView):
    def post(self, request):
        # Taking out the request data
        building_id = request.data.get('building')
        floor = request.data.get('floor')
        direction = request.data.get('direction')
        position_of_elevator = 2
        if direction == 2:
            position_of_elevator = 1
        elevators = None
        if direction == 1:  # If person want to go up
            elevators = Elevator.objects.filter(Q(building=building_id, floor__lte=floor, status=position_of_elevator)
                                                | Q(status=3)).exclude(status=4)
        elif direction == 2:  # If person want to go down
            elevators = Elevator.objects.filter(Q(building=building_id, floor__gte=floor, status=position_of_elevator)
                                                | Q(status=3)).exclude(status=4)

        if not elevators.exists():
            elevators = Elevator.objects.filter(building=building_id).exclude(status=4)
            if elevators.exists():
                requested_elevator = random.choice(elevators)
                serializer = ElevatorSerializer(requested_elevator)
                response = Response(serializer.data)
                requested_elevator.status = direction
                requested_elevator.floor = floor
                requested_elevator.save()
                return response
            else:
                return Response({"message: Elevators are not in funtion"})
        else:
            requested_elevator = random.choice(elevators)
            serializer = ElevatorSerializer(requested_elevator)
            response = Response(serializer.data)
            requested_elevator.status = direction
            requested_elevator.floor = floor
            requested_elevator.save()
            return response
