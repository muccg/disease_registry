from django.forms import widgets
from django.utils.safestring import mark_safe
from django.forms.util import flatatt

class EmptyCombo(widgets.Select):
    def render(self, name, value, attrs=None, choices=()):
        final_attrs = self.build_attrs(attrs, name=name)
        output = [u'<select%s>' % flatatt(final_attrs)]
        options = None
        if options:
            output.append(options)
        output.append('</select>')
        return mark_safe(u'\n'.join(output))