# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):
    usuario = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)
    apoio = models.BooleanFieldbool()
