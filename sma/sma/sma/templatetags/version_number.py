from django import template
from django.conf import settings

register = template.Library()

# settings value
@register.simple_tag
def version_number():
    return getattr(settings, "VERSION", "")