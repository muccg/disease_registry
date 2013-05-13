from django.template import Library

register = Library()

@register.filter
def format(value, arg):
    """
    Alters default filter "stringformat" to not add the % at the front,
    so the variable can be placed anywhere in the string.
    """
    
    try:
        return (unicode(arg)) % value
    except (ValueError, TypeError):
        return u''