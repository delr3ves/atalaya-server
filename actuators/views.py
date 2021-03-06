from django.http import HttpResponse
from rest_framework import viewsets
from actuators.models import Actuator
from actuators.serializers import ActuatorSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the actuators index.")


class ActuatorsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Actuator.objects.all()
    serializer_class = ActuatorSerializer