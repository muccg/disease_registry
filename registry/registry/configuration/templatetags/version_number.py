from django import template

register = template.Library()

# settings value
@register.simple_tag
def version_number(app_name):
    module = __import__(app_name)
    return module.VERSION