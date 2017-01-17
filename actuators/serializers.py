from actuators.models import SinglePinActuator
from rest_framework import serializers

class ActuatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SinglePinActuator
        fields = ('id', 'name', 'description', 'pin_number', 'image', 'created_at', 'updated_at', 'pin_status', 'url')