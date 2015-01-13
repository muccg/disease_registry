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
        
        jsonp_response = "%s(%s)" % (request.GET.get("callback"), json.dumps(result))
        
        response = HttpResponse(jsonp_response, content_type='application/json')
        return response