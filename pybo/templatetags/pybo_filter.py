from django import template

register = template.Library()


@register.filter
def sub(value, reg):
    return value - reg


@register.filter
def div(value, reg):
    return value // reg