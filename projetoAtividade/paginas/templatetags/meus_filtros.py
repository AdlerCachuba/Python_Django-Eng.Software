from django import template
from datetime import date

register = template.Library()

@register.filter(name="remover")
def remover(texto,r):
    return texto.replace(r,"")


@register.filter(name="verificardddpr")
def verificardddpr(telefone):
    ddd = telefone[0:4]
    if(ddd== "44"):
        return True
    else:
        return False


@register.filter(name="filtroDataFinal")
def filtroDataFinal(datafinal):
    if(datafinal < date.today()):
        return False 
    else:
        return True
