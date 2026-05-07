from django import template

register = template.Library()

FRACTIONS = {"25": "1/4", "5": "1/2", "75": "3/4", "33": "1/3", "66": "2/3"}


@register.filter
def get_type(value):
    return f"{type(value)}"


@register.filter
def to_common_fraction(value: float):
    if value % 1 == 0:
        return str(value)
    whole, decimal = str(value).split(".")
    if int(whole) < 10 and decimal in FRACTIONS:
        if int(whole) > 0:
            return f"{whole} {FRACTIONS[decimal]}"
        return FRACTIONS[decimal]
    return str(value)
