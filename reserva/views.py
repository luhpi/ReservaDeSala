# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from forms import SolicitanteForm
# AtividadeForm, ReservaForm
# from django.shortcuts import render
from .models import Solicitante
# , Atividade
# from apoio.models import Reserva

# Create your views here.


def solicitante(request):
    template = loader.get_template('reserva/reserva.html')
    context = {}
    result = ""
    if request.method == 'POST':
        sol = SolicitanteForm(request.POST)
        context = {'solicitante': sol,
                   'result': result}
        try:
            solicitante = Solicitante(
                curso=sol.cleaned_data['curso'],
                nome_sol=sol.cleaned_data['nome_sol'],
                tel=sol.cleaned_data['tel'],
                email=sol.cleaned_data['email'],
            )
            solicitante.save()
            return HttpResponse(template.render(request, context))
        except Exception as e:
            context = {
                'error': e
            }
            return HttpResponse(template.render(request, context))


def atividade(request):
    return HttpResponse('<h1> isso é atividade </h1>')


def reserva(request):
    return HttpResponse('<h1> isso é reserva </h1>')
