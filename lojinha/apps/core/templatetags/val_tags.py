# -*- coding: utf-8 -*-
from django import template

register = template.Library()


@register.filter
def money(value):
    """Converts into a currency value"""
    value = 0 if value is None else value
    value = "%01.2f" % value
    return str(value).replace('.', ',')
money.is_safe = True
