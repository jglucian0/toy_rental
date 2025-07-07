from django import template
from babel.dates import format_date
from datetime import datetime

register = template.Library()

DIAS_ABREVIADOS = {
    'segunda-feira': 'Seg.',
    'terça-feira': 'Ter.',
    'quarta-feira': 'Qua.',
    'quinta-feira': 'Qui.',
    'sexta-feira': 'Sex.',
    'sábado': 'Sáb.',
    'domingo': 'Dom.',
}


@register.filter
def formata_data_extenso(data):
    if not data:
        return ''

    # Formata: "16 de julho"
    data_formatada = format_date(data, format="d 'de' MMMM", locale='pt_BR')

    # Descobre o dia da semana
    dia_semana = format_date(data, 'EEEE', locale='pt_BR').lower()
    abreviado = DIAS_ABREVIADOS.get(dia_semana, dia_semana[:3].capitalize())

    return f"{data_formatada.capitalize()} - {abreviado}"
