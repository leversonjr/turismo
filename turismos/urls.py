'''Define padrões de url para Turismos'''

from django.urls import path
from . import views


urlpatterns = [
    #Pagina Inicial
    path('', views.index, name='index'),

    #Pagina de Contato
    path('contato/', views.contato, name='contato'),

# Pagina sobre a Empresa
    path('sobre/', views.sobre, name='sobre'),

    #Pagina sobre pacotes turisticos
    path('pacotes/', views.pacotes, name='pacotes'),

]