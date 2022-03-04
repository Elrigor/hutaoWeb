from django import template

register = template.Library()

@register.simple_tag
def get_mundo():
    return "Mundo"


''' 

EN EL HTML

{% load discord %}
{% get_mundo as mundo %}


<h1>hola {{mundo}}</h1>

'''