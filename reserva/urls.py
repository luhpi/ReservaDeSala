from django.conf.urls import url
from . import views

<<<<<<< HEAD
urlpatterns = [url(r'^solicitante$', views.solicitante, name='solicitante'),
               url(r'^atividade$', views.atividade, name='atividade'),
               url(r'^reserva$', views.reserva, name='reserva')]
=======
urlpatterns = [url(r'^/solicitante$', views.solicitante, name='solicitante'),
               url(r'^/atividade$', views.atividade, name='atividade'),
               url(r'^/reserva$', views.reserva, name='reserva')]
>>>>>>> 7c3232d7c94f0be7714c69c31c5b10370b674f8d
