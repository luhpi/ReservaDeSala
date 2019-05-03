# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Solicitante(models.Model):
    curso = models.CharField(max_length=100)
    nome_sol = models.CharField(max_length=100)
    tel = models.CharField(max_length=12)
    email = models.CharField(max_length=100)


class Atividade(models.Model):
    atividade = models.CharField(max_length=100)
    data_req_ini = models.DateTimeField('data inicial')
    data_req_fim = models.DateTimeField('data final')
    solicitante = models.ForeignKey(Solicitante, on_delete=models.CASCADE)


class Reserva(models.Model):
    sala = models.CharField(max_length=30)
    servidor = models.CharField(max_length=100)
    obs = models.CharField(max_length=500)
    data_res_ini = models.DateTimeField('data inicial')
    data_res_fim = models.DateTimeField('data final')
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)
