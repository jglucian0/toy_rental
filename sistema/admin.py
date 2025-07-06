from django.contrib import admin
from .models import Brinquedo  # Importa o modelo Brinquedo
from .models import Cliente  # Importa o modelo Cliente


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
