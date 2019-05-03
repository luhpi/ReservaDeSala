from django.conf.urls import url
from . import views

urlpatterns = [url(r'^solicitante', views.solicitante),
               url(r'^atividade',  views.atividade),
               url(r'^reserva', views.reserva),
               ]
