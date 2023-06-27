import uuid

from django.db import models

from .choices import STATUS_CHOICES, DOOR_STATUS_CHOICES


class BuildingConfiguration(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=100)
    num_floors = models.PositiveIntegerField()
    num_lifts = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)


class Elevator(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    building = models.ForeignKey(BuildingConfiguration, on_delete=models.DO_NOTHING)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    door_status = models.IntegerField(choices=DOOR_STATUS_CHOICES, default=1)
    floor = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)

