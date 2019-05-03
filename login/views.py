# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from forms import UserForm
from .models import User

# Create your views here.


def login(request):
    template = loader.get_template('login.html')
    if request.method == 'POST':
        user = UserForm(request.POST)
        context = {'user': user,
                   'result': ""}
        print(user)
        if user.is_valid():
            try:
                aux = User.objects.get(usuario=user.cleaned_data['usuario'])
                if(aux.senha == user.cleaned_data['senha']):
                    return redirect('/formulario/solicitante')
                else:
                    result = "Senha incorreta"
                    context = {'user': user,
                               'result': result}
                    return HttpResponse(template.render(context, request))
            except Exception as e:
                result = e
                result = "Usuario não existe"
                context = {'user': user,
                           'result': result}
                return HttpResponse(template.render(context, request))

    else:
        user = UserForm()
    context = {'user': user}
    return HttpResponse(template.render(context, request))
