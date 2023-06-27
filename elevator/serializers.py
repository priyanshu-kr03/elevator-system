from rest_framework import serializers

from .models import BuildingConfiguration, Elevator


class BuildingConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingConfiguration
        fields = "__all__"

    # When we add building configuration based of number of elevator,
    # here we are creating that number of entry in Elevator Model
    def create(self, validated_data):
        try:
            building_obj = super().create(validated_data=validated_data)
            for elevator in range(validated_data["num_lifts"]):
                elevator_obj = ElevatorSerializer(
                    data={
                        "building": building_obj.id
                    }
                )
                elevator_obj.is_valid(raise_exception=True)
                elevator_obj.save()
            return building_obj
        except Exception as e:
            raise Exception("Error in creating elevator model", e)


class ElevatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elevator
        fields = "__all__"
