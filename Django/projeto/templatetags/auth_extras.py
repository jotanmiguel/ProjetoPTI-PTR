from django import template
from django.contrib.auth.models import Group
import re

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    try:
        group =  Group.objects.get(name=group_name)
    except Group.DoesNotExist:
        return False

    return group in user.groups.all()

@register.filter(name='to_float')
def to_float(value):
    return float(value)

@register.filter
def total_sum(value):
    value = str(value)
    temp_val = value.split(' ')
    sum = 0.00
    
    for val in temp_val:
        sum += float(val[:-1])

    return sum

@register.filter
def to_bytes(value, encoding='utf-8'):
    return value.encode(encoding)