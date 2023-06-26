import uuid

from django.db import models


class BuildingConfiguration(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=100)
    num_floors = models.PositiveIntegerField()
    num_lifts = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
