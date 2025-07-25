from django.urls import path
from . import views

urlpatterns = [
    path('', views.agendar_locacao, name='agendar_locacao'),
    path('locacoes/', views.listar_locacoes, name='listar_locacoes'),
    path('financeiro/', views.dashboard_financeiro, name='dashboard_financeiro'),
    path('locacoes/<int:locacao_id>/editar-status/',
         views.editar_status_pagamento, name='editar_status_pagamento'),
    path('locacoes/<int:locacao_id>/excluir/',
         views.excluir_locacao, name='excluir_locacao'),
    path('locacoes/<int:locacao_id>/enviar_whatsapp/',
         views.enviar_confirmacao_whatsapp, name='enviar_confirmacao_whatsapp'),
    path('clientes/cadastrar/', views.cadastrar_cliente, name='cadastrar_cliente'),

]