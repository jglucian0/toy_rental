from django.db import models

# Create your models here.
# Será criado meu banco de dados para armazenar os dados do sistema
class Brinquedo(models.Model):
    TIPO_BRINQUEDO = (
        ('toboga', 'Tobogã Inflável'),
        ('cama_elastica', 'Cama Elástica'),
        ('piscina_bolas', 'Piscina de Bolas'),
    )

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_BRINQUEDO)
    valor_locacao = models.DecimalField(max_digits=8, decimal_places=2)
    ultima_limpeza = models.DateField()
    disponivel = models.BooleanField(default=True)
    observacoes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    cpf = models.CharField(max_length=11, unique=True)
    endereco = models.TextField()

    def __str__(self):
        return f'{self.nome} - {self.telefone}'
    

class Locacao(models.Model):
    STATUS_PAGAMENTO = [
        ('pendente', 'Pendente'),
        ('pago', 'Pago'),
        ('parcialmente_pago', '30% Pago'),
        ('cancelado', 'Cancelado'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    brinquedos = models.ManyToManyField(Brinquedo)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    valor_total = models.DecimalField(max_digits=8, decimal_places=2)
    status_pagamento = models.CharField(
        max_length=20, choices=STATUS_PAGAMENTO, default='pendente')
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Locação de {self.cliente.nome} - {self.data_inicio} a {self.data_fim}'
