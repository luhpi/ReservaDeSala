# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
# from django.shortcuts import render

# Create your views here.


def solicitante(request):
    return HttpResponse('<h1> isso é solicitante </h1>')


def atividade(request):
    return HttpResponse('<h1> isso é atividade </h1>')


def reserva(request):
    return HttpResponse('<h1> isso é reserva </h1>')
