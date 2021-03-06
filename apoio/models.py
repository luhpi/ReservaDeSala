# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from reserva.models import Atividade
from django.db import models

# Create your models here.


class Apoio(models.Model):
    data_res_ini = models.DateTimeField('data inicial')
    data_res_fim = models.DateTimeField('data final')
    alunos = models.IntegerField()
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)


class Reserva(models.Model):
    sala = models.CharField(max_length=30)
    servidor = models.CharField(max_length=100)
    obs = models.CharField(max_length=500)
