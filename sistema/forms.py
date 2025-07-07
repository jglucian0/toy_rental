from django import forms
from .models import Locacao, Cliente
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class LocacaoForm(forms.ModelForm):
    class Meta:
        model = Locacao
        fields = [
            'cliente', 'brinquedos', 'data_inicio', 'data_fim',
            'valor_total', 'status_pagamento', 'observacoes'
        ]
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'brinquedos': forms.SelectMultiple(attrs={'class': 'form-select', 'id': 'id_brinquedos'}),
            'data_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'data_fim': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'valor_total': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_valor_total'}),
            'status_pagamento': forms.Select(attrs={'class': 'form-select'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        
    def clean(self):
        cleaned_data = super().clean()
        brinquedos = cleaned_data.get('brinquedos')
        data_inicio = cleaned_data.get('data_inicio')
        data_fim = cleaned_data.get('data_fim')

        if data_inicio and data_fim and brinquedos:
            for brinquedo in brinquedos:
                conflitos = Locacao.objects.filter(
                    brinquedos=brinquedo,
                    data_inicio__lte=data_fim,
                    data_fim__gte=data_inicio,
                )
                if self.instance.pk:
                    conflitos = conflitos.exclude(pk=self.instance.pk)

                if conflitos.exists():
                    raise ValidationError(
                        _(f"🚫 O brinquedo '{brinquedo.nome}' já está alugado neste período.")
                    )
        return cleaned_data


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'cpf', 'email', 'endereco']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
        }

class LocacaoAdminForm(forms.ModelForm):
    class Meta:
        model = Locacao
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        data_inicio = cleaned_data.get('data_inicio')
        data_fim = cleaned_data.get('data_fim')
        brinquedos = cleaned_data.get('brinquedos')

        if data_inicio and data_fim and brinquedos:
            for brinquedo in brinquedos:
                conflitos = Locacao.objects.filter(
                    brinquedos=brinquedo,
                    data_inicio__lte=data_fim,
                    data_fim__gte=data_inicio,
                )
                if self.instance.pk:
                    conflitos = conflitos.exclude(pk=self.instance.pk)

                if conflitos.exists():
                    raise ValidationError(
                        _(f"O brinquedo '{brinquedo.nome}' já está alugado neste período.")
                    )
        return cleaned_data
