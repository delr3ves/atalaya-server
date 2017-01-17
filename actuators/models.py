from __future__ import unicode_literals

from django.core.validators import MaxValueValidator
from django.db import models
from atalaya_server.settings import UPLOAD_FILES_TO
from gpiozero import OutputDevice


class SinglePinActuator(models.Model):

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=4095)
    image = models.FileField(upload_to=UPLOAD_FILES_TO)
    pin_number = models.IntegerField(validators=[MaxValueValidator(27)], unique=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def pin_status(self):
        return OutputDevice(self.pin_number).is_active

