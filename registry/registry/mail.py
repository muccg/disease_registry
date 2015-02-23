from django.core.mail import send_mass_mail
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from registry.configuration.models import EmailTemplate

import os.path


def default_return_email():
    return getattr(settings, "RETURN_EMAIL", "noreply@ccg.murdoch.edu.au")

def sendNewPatientEmail(recipients, from_email=None):
    if not from_email:
        from_email = default_return_email()

    templates = getNewPatientEmailTemplate()
    
    for template in templates:
        groups = template.groups.all()
        to_email = recipients.filter(user__groups__in=groups).distinct().values_list("user__email", flat=True)
        subject = '%s: new patient registered' % settings.INSTALL_NAME.upper()
        body = template.body
        
        try:
            mass_email = []
            for email in to_email:
                mass_email.append( (subject, body, from_email, [email]) )
        
            send_mass_mail(mass_email)
        except Exception, e:
            print 'Error sending mail to user: ',to_email , ':', str(e)

def getNewPatientEmailTemplate():
    #target=1 -> registry.configuration.models.EmailTemplate.TARGETS
    return EmailTemplate.objects.filter(target=1)