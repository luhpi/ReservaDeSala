# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-03 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='apoio',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
