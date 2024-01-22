from django import template
register = template.Library()


@register.filter
def date_format(value, format="%Y-%m-%d %H:%M:%S"):

    return value.strftime(format)
