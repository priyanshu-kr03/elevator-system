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
        # Taking out data from request body
        building_id = request.data.get('building')
        floor = request.data.get('floor')
        direction = request.data.get('direction')
        status_of_elevator = 2
        if direction == 2:
            status_of_elevator = 1
        elevators = None
        # If a person wants to go UP then we are fetching is there any lift whose status DOWN(status=2)
        # or is there any lift which is ideal(status=4) and excluding all those lifts which are under maintenance
        if direction == 1:
            elevators = Elevator.objects.filter(Q(building=building_id, floor__lte=floor) & (Q(status=status_of_elevator)
                                                | Q(status=3))).exclude(status=4)
        elif direction == 2:
            # If a person wants to go DOWN then we are fetching is there any lift whose status UP(status=1)
            # or is there any lift which is ideal(status=4) and excluding all those lifts which are under maintenance
            elevators = Elevator.objects.filter(Q(building=building_id, floor__gte=floor) & (Q(status=status_of_elevator)
                                                | Q(status=3))).exclude(status=4)

        # If there are no lift available then we are just taking out a random lift from available lifts and changing
        # status and floor of the lift accordingly
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
        # If there are multiple lifts available then we are just taking out a random lift from them and changing
        # status and floor of the lift accordingly
        else:
            requested_elevator = random.choice(elevators)
            serializer = ElevatorSerializer(requested_elevator)
            response = Response(serializer.data)
            requested_elevator.status = direction
            requested_elevator.floor = floor
            requested_elevator.save()
            return response
