# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-15 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actuators', '0002_auto_20170115_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='actuator',
            name='image',
            field=models.FileField(default=1, upload_to=b'/data/upload/'),
            preserve_default=False,
        ),
    ]