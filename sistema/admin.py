from django.contrib import admin
from .models import Brinquedo  # Importa o modelo Brinquedo
from .models import Cliente  # Importa o modelo Cliente
from .models import Locacao # Importa o modelo Locacao


@admin.register(Brinquedo)
class BrinquedoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'valor_locacao',
                    'ultima_limpeza', 'disponivel')
    list_filter = ('tipo', 'disponivel')
    search_fields = ('nome', 'tipo')
    
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'cpf')
    serch_fields = ('nome', 'telefone', 'cpf')

@admin.register(Locacao)
class LocacaoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'data_inicio', 'valor_total', 'status_pagamento')
    list_filter = ('status_pagamento', 'data_inicio')
    search_fields = ('cliente__nome', 'data_inicio')
    filter_horizontal = ('brinquedos',)