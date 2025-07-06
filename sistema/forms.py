from django import forms
from .models import Locacao
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class LocacaoForm(forms.ModelForm):
    class Meta:
        model = Locacao
        fields = ['cliente', 'brinquedos', 'data_inicio', 'data_fim', 'valor_total', 'status_pagamento', 'observacoes']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
        }
        
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
