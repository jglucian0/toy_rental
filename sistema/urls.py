from django.urls import path
from . import views

urlpatterns = [
    path('', views.agendar_locacao, name='agendar_locacao'),
    path('locacoes/', views.listar_locacoes, name='listar_locacoes'),
]