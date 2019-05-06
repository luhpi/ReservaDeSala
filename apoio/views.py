# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
# from django.shortcuts import render
from reserva.models import Solicitante, Atividade
from .models import Reserva, Apoio
from django.template import loader
# from django.shortcuts import render

# Create your views here.


def apoio(request):
    template = loader.get_template('apoio/apoio.html')
    aux = Apoio.objects.count()
    ultimo_form = []
    try:
        ultimo_form.append(Solicitante.objects.get(id=aux))
        ultimo_form.append(Atividade.objects.get(id=aux))
        ultimo_form.append(Reserva.objects.get(id=aux))
        context = {
           'ultimo_form': ultimo_form
        }
        return HttpResponse(template.render(context, request))
    except Exception as e:
        context = {
            'erro': e
        }
        return HttpResponse(template.render(context, request))
