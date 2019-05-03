from django.conf.urls import url
from . import views

urlpatterns = [url(r'^solicitante$', views.solicitante, name='solicitante'),
               url(r'^atividade$', views.atividade, name='atividade'),
               url(r'^apoio$', views.apoio, name='apoio'),
               url(r'^reserva$', views.reserva, name='reserva')]
