import datetime

from django import template

from pytz import timezone

register = template.Library()

@register.filter
def date_format(value):
    try:
        date = datetime.datetime.fromtimestamp(value)
        return date
    except:
        return value
