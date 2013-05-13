from django import template

register = template.Library()

@register.filter(name='zip')
def agrupar(primeira_lista, segunda_lista):
    return zip(primeira_lista, segunda_lista)
