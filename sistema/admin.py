from django.contrib import admin
from .models import Brinquedo  # Importa o modelo Brinquedo


@admin.register(Brinquedo)
class BrinquedoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'valor_locacao',
                    'ultima_limpeza', 'disponivel')
    list_filter = ('tipo', 'disponivel')
    search_fields = ('nome', 'tipo')
