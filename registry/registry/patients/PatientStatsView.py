from django.http import HttpResponse
from django.views.generic.base import View
from django.db.models import Count

from models import Patient

import json

class PatientStatsView(View):

    def get(self, request):
        patients = Patient.objects.values('working_group__name').annotate(Count("id")).order_by()
        result = []
        
        for patient in patients:
            result.append(patient)
            
        result.append({'total' : Patient.objects.count() })
        
        response = HttpResponse(json.dumps(result), content_type='application/javascript')
        return response