from django import template
from datetime import datetime

register = template.Library()

@register.filter
def mostra_duracao(value1, value2):
    if isinstance(value1, datetime) and isinstance(value2, datetime):
        dias = (value1 - value2).days
        if dias == 1 ou == 0:
            texto = 'Dia'


    return "Ainda não foi devolvido"