# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-03 17:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0002_auto_20190503_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='atividade',
        ),
        migrations.DeleteModel(
            name='Reserva',
        ),
    ]
