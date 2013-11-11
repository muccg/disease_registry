from datetime import datetime

from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.base import View
from django.core.exceptions import ObjectDoesNotExist

from report_utils import BaseReport

import json

import csv

class PatientReport(View, BaseReport):
    NAME = "DMD_Report"
    
    def get(self, request, *args, **kwargs):
        from django.http import HttpResponse
        from django.conf import settings
        from datetime import datetime
        import csv

        if not request.user.is_superuser:
            return HttpResponseRedirect('/')

        response = HttpResponse(mimetype="text/csv")
        writer = csv.writer(response)

        report = PatientReport()

        app_name = settings.INSTALL_NAME
        report_name = report.NAME
        run_date = datetime.now().strftime('%b-%d-%I%M%p-%G')
        
        report.write_with(writer)
        
        response['Content-Disposition'] = 'attachment; filename=%s_%s_%s.csv' % (app_name, report_name, run_date)

        return response

    def query(self):
        diagnosis = Diagnosis.objects.by_working_group(self.working_group)
        diagnosis = diagnosis.select_related('motorfunction', 'steroids', 'surgery', 'heart', 'heartmedication', 'respiratory')
        return diagnosis
    
    """
    Temporary mockup data
    """
    def get_data(self):
        json_data=open('dmd/dmd/patient.json')
        return json.load(json_data)

    """
    TODO: dynamicaly generated spec for report
    """    
    def get_spec(self):
        return [['Patient ID', 'patient_id'], ['State', 'address.state']]