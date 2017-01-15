from __future__ import unicode_literals

from django.db import models

class Actuator(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=4095)
    image = models.CharField
    pin_number = models.IntegerField
    created_at = models.DateTimeField('date published')
    updated_at = models.DateTimeField('date published')
