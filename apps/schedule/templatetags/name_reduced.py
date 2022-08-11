from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def first_name_reduced(full_name):
    name = full_name.split(' ')[0]

    return name
