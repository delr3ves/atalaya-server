from __future__ import unicode_literals

from django.core.validators import MaxValueValidator
from django.db import models
from atalaya_server.settings import UPLOAD_FILES_TO
from gpiozero import OutputDevice


class Actuator(models.Model):

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=4095)
    image = models.FileField(upload_to=UPLOAD_FILES_TO)
    pin_number = models.IntegerField(validators=[MaxValueValidator(27)])
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __init__(self, *args, **kwargs):
        super(Actuator, self).__init__(*args, **kwargs)

        self.gpio_output = OutputDevice(self.pin_number)

    @property
    def pin_status(self):
        return self.gpio_output.is_active

    def toggle(self):
        self.gpio_output.toggle()

