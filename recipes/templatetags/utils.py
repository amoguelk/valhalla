from django import template

register = template.Library()

FRACTIONS = {
    "25": "1/4",
    "5": "1/2",
    "75": "3/4",
    "3": "1/3",
    "6": "2/3",
    "125": "1/8",
    "375": "3/8",
    "625": "5/8",
    "875": "7/8",
}


@register.filter
def get_type(value):
    return f"{type(value)}"


@register.filter
def to_common_fraction(value: float):
    sval = str(value)
    if "." not in sval:
        return sval
    whole, decimal = sval.split(".")

    if decimal == "0":
        return whole

    if decimal.startswith("3"):
        decimal = "3"
    elif decimal.startswith("6"):
        decimal = "6"

    if int(whole) < 10 and decimal in FRACTIONS:
        if int(whole) > 0:
            return f"{whole} {FRACTIONS[decimal]}"
        return FRACTIONS[decimal]
    return sval
