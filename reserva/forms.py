# -*- coding: utf-8 -*-
from django import forms


class SolicitanteForm(forms.Form):
    CHOICES = ['Biomedicina',
               'Enfermagem',
               'Fisioterapia',
               'Fonoaudiologia',
               'Medicina',
               u'Nutrição',
               'Psicologia',
               u'Especialização',
               u'Residência Médica',
               u'Pós-Graduação'
               'Outro']
    curso = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    nome_sol = forms.CharField(label='Nome do solicitante', max_length=100)
    tel = forms.CharField(label='Curso', max_length=20)
    email = forms.CharField(label='Curso', max_length=100)


class AtividadeForm(forms.Form):
    atividade = forms.CharField(label='Atividade', max_length=100)
    outros = forms.CharField(max_length=100)
    data_req_ini = forms.DateField('data inicio')


class ReservaForm(forms.Form):
    sala = forms.CharField(max_length=10)
