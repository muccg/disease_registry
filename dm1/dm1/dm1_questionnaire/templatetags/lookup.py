from django.template import Library

register = Library()

@register.filter()
def lookup(form, field):
    return form[field].data