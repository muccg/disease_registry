from datetime import datetime

from django.http import HttpResponse
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.db.models import Q

from registry.genetic.models import Variation
from registry.patients.models import Patient
from dmd.dmd.models import Diagnosis, MotorFunction

class GeneticReport(View):
    
    age_range = [
        ('02.09.2009', '01.01.2100'),
        ('02.09.2006', '01.09.2009'),
        ('02.09.2003', '01.09.2006'),
        ('02.09.2000', '01.09.2003'),
        ('02.09.1997', '01.09.2000'),
        ('02.09.1994', '01.09.1997'),
        ('01.01.1900', '01.09.1994')
    ]
    
    @method_decorator(login_required)
    def get(self, request):
        varations = Variation.objects.get_containing('protein_variation', ['X', '*'])

        for ages in self.age_range:
            patients_from_variation = [v.molecular_data.patient for v in varations]
            patients = Patient.objects.filter(id__in=[patient.id for patient in patients_from_variation])
            patients = patients.filter(date_of_birth__range=[self.str_to_date(ages[0]), self.str_to_date(ages[1])])

            diagnosis = Diagnosis.objects.filter(patient__in=patients)

            print '\n---%s - %s --- total: %s' % (ages[0], ages[1], patients.count())
            print 'ambulant         %s' % diagnosis.filter(motorfunction__walk=True).count()
            print 'nonambulant      %s' % diagnosis.filter(motorfunction__walk=False).count()
            print 'ambulantunknown  %s\n' % diagnosis.filter(motorfunction__walk__isnull=True).count()

            print 'on_steroids      %s' % diagnosis.filter(steroids__current=True).count()
            print 'not_on_steroids  %s' % diagnosis.filter(steroids__current=False).filter(steroids__previous=0).count()
            print 'unknown          %s\n' % diagnosis.filter(steroids__current__isnull=True).count()

            #To be confirmed with Leanne
            ventilation_query = Q(respiratory__invasive_ventilation='Y') | Q(respiratory__non_invasive_ventilation='Y')
            print 'ventialation_yes %s' % diagnosis.filter(ventilation_query).count()
            print 'ventialation_no  %s' % diagnosis.filter(~ventilation_query).count()
            print 'unknown          %s\n' % diagnosis.filter(respiratory__invasive_ventilation__isnull=True).count()
            
            print 'yes_clinical_trails  %s\n' % diagnosis.filter(clinicaltrials__isnull=False).count()
            print 'unknown_clinical_trails  %s\n' % diagnosis.filter(clinicaltrials__isnull=True).count()
        
        return HttpResponse('Done')

    def str_to_date(self, value):
        return datetime.strptime(value , '%d.%m.%Y').date()