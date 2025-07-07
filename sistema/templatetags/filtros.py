from django import template
from babel.dates import format_date
from datetime import datetime

register = template.Library()

MESES_EN_PT = {
    'January': 'Janeiro', 'February': 'Fevereiro', 'March': 'Março',
    'April': 'Abril', 'May': 'Maio', 'June': 'Junho',
    'July': 'Julho', 'August': 'Agosto', 'September': 'Setembro',
    'October': 'Outubro', 'November': 'Novembro', 'December': 'Dezembro',
}

DIAS_ABREVIADOS = {
    'Monday': 'Seg.', 'Tuesday': 'Ter.', 'Wednesday': 'Qua.',
    'Thursday': 'Qui.', 'Friday': 'Sex.', 'Saturday': 'Sáb.', 'Sunday': 'Dom.'
}


@register.filter
def formata_data_extenso(data):
    if not data:
        return ''

    if isinstance(data, str):
        try:
            data = datetime.strptime(data, "%Y-%m-%d").date()
        except:
            return data

    # Parte 1: Dia e mês em inglês
    dia = data.strftime('%d')
    mes_en = data.strftime('%B')
    mes_pt = MESES_EN_PT.get(mes_en, mes_en)

    # Parte 2: Dia da semana em inglês
    dia_semana_en = data.strftime('%A')
    dia_semana_pt = DIAS_ABREVIADOS.get(dia_semana_en, dia_semana_en[:3])

    return f"{dia} de {mes_pt} - {dia_semana_pt}"
