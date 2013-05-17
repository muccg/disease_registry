from django.core.mail import send_mail
from django.conf import settings
import os.path


def default_return_email():
    return getattr(settings, "RETURN_EMAIL", "noreply@ccg.murdoch.edu.au")

def sendNewPatientEmail(to_email, from_email=None):
    if not from_email:
        from_email = default_return_email()

    subject = '%s: new patient registered' % settings.INSTALL_NAME.upper()
    body = 'New pateint has been registerd\r\n\r\n'
    body += 'Thank you'
    try:
        send_mail(subject, body, from_email, to_email,fail_silently = False)
    except Exception, e:
        print 'Error sending mail to user: ',to_email , ':', str(e)