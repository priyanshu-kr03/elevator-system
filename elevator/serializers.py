from rest_framework import serializers

from .models import BuildingConfiguration


class BuildingConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingConfiguration
        fields = "__all__"
