from django.urls import path
from . import views

urlpatterns = [
    path('', views.agendar_locacao, name='agendar_locacao'),
    path('locacoes/', views.listar_locacoes, name='listar_locacoes'),
    path('financeiro/', views.dashboard_financeiro, name='dashboard_financeiro'),
    path('locacoes/<int:locacao_id>/editar-status/',
         views.editar_status_pagamento, name='editar_status_pagamento'),

]