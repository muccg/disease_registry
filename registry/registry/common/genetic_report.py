import csv

from datetime import datetime

from django.http import HttpResponse
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.db.models import Q

from registry.genetic.models import Variation
from registry.patients.models import Patient

class GeneticReport(View):
    
    age_range = [
        ['Up to 3 years', '02.09.2009', '01.01.2100'],
        ['Aged 4 to 6', '02.09.2006', '01.09.2009'],
        ['Aged 7 to 9', '02.09.2003', '01.09.2006'],
        ['Aged 10 to 12', '02.09.2000', '01.09.2003'],
        ['Aged 13 to 15', '02.09.1997', '01.09.2000'],
        ['Aged 16 to 18', '02.09.1994', '01.09.1997'],
        ['Aged 19 and over', '01.01.1900', '01.09.1994']
    ]
    
    spec = [
        ['Protein Variation', 'proteinvariation'],
        ['Gene', 'gene'],
        ['Exon', 'exon'],
        ['DNA Variation', 'dna_variation'],
        ['All exons tested deletions', 'exons_deletions'],
        ['All exons tested duplications', 'exons_duplications'],
        ['Currently able to walk', 'walk'],
        ['Current steroids use', 'steroids'],
        ['Non-invasive ventilation', 'non_invasive_ventilation'],
        ['Invasive ventilation','invasive_ventilation'],
        ['Clinical Trials', 'trials']
    ]
    
    @method_decorator(login_required)
    def get(self, request):
        from dmd.dmd.models import Diagnosis, MotorFunction, Steroids, Respiratory, ClinicalTrials
        response = HttpResponse(mimetype="text/csv")
        writer = csv.writer(response)
        
        for age in self.age_range:
            variations = Variation.objects.get_containing('protein_variation', ['X', '*'])
            variations = variations.filter(molecular_data__patient__date_of_birth__range=(self.str_to_date(age[1]), self.str_to_date(age[2])))
            if variations:
                report = [self.get_results(v) for v in variations]
                writer.writerow([age[0]])    
                writer.writerow([s[0] for s in self.spec])
                for r in report:
                    writer.writerow([r[s[1]] for s in self.spec])
                writer.writerow([''])

        response['Content-Disposition'] = 'attachment; filename=report.csv'
        return response

    def get_results(self, variation):
        results = {}
        
        results['proteinvariation'] = variation.protein_variation
        results['gene'] = variation.gene
        results['exon'] = variation.exon
        results['dna_variation'] = variation.dna_variation
        results['exons_deletions'] = self.yes_no_unknown(variation.deletion_all_exons_tested)
        results['exons_duplications'] = self.yes_no_unknown(variation.duplication_all_exons_tested)
        
        diagnosis = Diagnosis.objects.get(patient=variation.molecular_data.patient)
        
        try:
            motor = MotorFunction.objects.get(diagnosis=diagnosis)
            results['walk'] = self.yes_no_unknown(motor.walk)
        except MotorFunction.DoesNotExist:
            results['walk'] = 'No/Unknown'
            
        try:
            steroids = Steroids.objects.get(diagnosis=diagnosis)
            results['steroids'] = self.yes_no_unknown(steroids.current)
        except Steroids.DoesNotExist:
            results['steroids'] = 'Unknown'
            
        try:
            respiratory = Respiratory.objects.get(diagnosis=diagnosis)
            results['non_invasive_ventilation'] = self.yes_part_no_unknown(respiratory.non_invasive_ventilation)
            results['invasive_ventilation'] = self.yes_part_no_unknown(respiratory.invasive_ventilation)
        except Respiratory.DoesNotExist:
            results['non_invasive_ventilation'] = 'Unknown'
            results['invasive_ventilation'] = 'Unknown'
            
        try:
            trials = ClinicalTrials.objects.get(diagnosis=diagnosis)
            results['trials'] = 'Yes'
        except ClinicalTrials.DoesNotExist:
            results['trials'] = 'No'
            
        return results

    def yes_part_no_unknown(self, value):
        if value is None:
            return 'Unknown'
        if value == 'Y':
            return 'Yes'
        if value == 'PT':
            return 'Yes - part time'
        if value == 'N':
            return 'No'

    def yes_no_unknown(self, value):
        if value is None:
            return 'Unknown'
        if value:
            return 'Yes'
        elif not value:
            return 'No'

    def str_to_date(self, value):
        return datetime.strptime(value , '%d.%m.%Y').date()