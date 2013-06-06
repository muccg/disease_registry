from django.shortcuts import render
from django.conf import settings
from django.template import RequestContext

from registry.configuration.models import ConsentForm

def index(request):
    consent_form_au = ConsentForm.objects.get(country='AU')
    consent_form_nz = ConsentForm.objects.get(country='NZ')
    
    return render(request, 'dm1/index.html', {
            'media_url': settings.MEDIA_URL,
            'consent_form_au': consent_form_au.form,
            'consent_form_nz': consent_form_nz.form
        }, 
        context_instance=RequestContext(request))