from django import template

register = template.Library()


@register.filter
def get_type(value):
    return f"{type(value)}"
