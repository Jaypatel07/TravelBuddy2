# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-05-24 18:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TripApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='trip_members',
            new_name='trip_attendants',
        ),
    ]
