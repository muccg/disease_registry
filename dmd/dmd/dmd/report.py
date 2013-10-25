from datetime import datetime

from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.base import View

import csv

from models import Diagnosis
from registry.genetic.models import MolecularData, Variation

class NmdReport(View):
    
    columns = ('Patient ID', 'Gene', 'Exon', 'DNA Variation', 'All Exons Tested (Deletion)', 'All Exons Tested (Duplications)', 'Exon Boundaries Known', 
                'All Exons Sequenced (Point Mutation)', 'All expons tested in Male Relative', 'Diagnosis', 'Currently Able To Walk', 'Wheelchair Use', 
                'Current Steroid Theraphy', 'Scoliosis Surgery', 'Current cardiac medication', 'Clinical Trials', 'Date of birth', 'Last updated', 
                'State/Province, postcode', 'Currently able to sit without support', 'Heart failure/cardiomyopathy', 'LVEF score and date',
                'Non Invasive Ventilation', 'Invasive Ventilation', 'FVC score and date', 'Previous Muscle Biopsy', 'Other Registries', 'Family History')
    
    def get(self, request, *args, **kwargs):
        working_group = self.kwargs['working_group']

        diagnosis = self.get_diagnosis(working_group)
        working_group = working_group
        file_name = 'dmd_nmdreport_%s_%s.csv' % (working_group, self.format_date(datetime.now(), '%d-%m-%Y_%H:%M:%S'))

        response = HttpResponse(mimetype="text/csv")
        writer = csv.writer(response)
        
        diagnosis = diagnosis.select_related('motorfunction', 'steroids', 'surgery', 'heart', 'heartmedication', 'respiratory')

        results = []

        for d in diagnosis:
            items = {}

            items['patient_id'] = str(d.patient.id)
            items['age'] = str(d.patient.date_of_birth)
            items['diagnosis'] = str(self.diagnosis_name(d.diagnosis))
            items['localisation'] = str(d.patient.postcode)

            items['last_follow_up'] = str(self.format_date(d.updated, '%d-%m-%Y')) if d.updated is not None else str(self.format_date(d.created, '%d-%m-%Y'))

            items['muscle_biopsy'] = self.yes_no_str(d.muscle_biopsy) if d.muscle_biopsy is not None else 'Unknown'

            try:
                items['able_to_walk'] = self.yes_no_unknown_str(d.motorfunction.walk)
                items['wheelchair_use'] = self.wheelchair_use(d.motorfunction)
                items['able_to_sit'] = self.yes_no_unknown_str(d.motorfunction.sit) 
            except ObjectDoesNotExist:
                items['able_to_walk'] = 'No/Unknown'
                items['wheelchair_use'] = 'Unknown'
                items['able_to_sit'] = 'No/Unknown'            

            try:
                items['current_steroid_theraphy'] = self.yes_no_str(d.steroids.current)
            except ObjectDoesNotExist:
                items['current_steroid_theraphy'] = 'Unknown'

            try:
                items['scoliosis_surgery'] = self.yes_no_str(d.surgery.surgery)
            except ObjectDoesNotExist:
                items['scoliosis_surgery'] = 'Unknown'

            try:
                items['heartmedication'] = self.heart_medication(d)
                items['heart_failure'] = self.yes_no_str(d.heart.failure)
                items['last_lvef'] = '%s, %s' % (d.heart.lvef, d.heart.lvef_date)
            except ObjectDoesNotExist:
                items['heart_failure'] = 'Unknown'
                items['last_lvef'] = 'Unknown'

            try:
                items['non_invasive_ventilation'] = self.yes_no_pt_str(d.respiratory.non_invasive_ventilation)
                items['invasive_ventilation'] = self.yes_no_pt_str(d.respiratory.invasive_ventilation)
                items['last_fvc'] = '%s, %s' % (d.respiratory.fvc, d.respiratory.fvc_date)
            except ObjectDoesNotExist:
                items['non_invasive_ventilation'] = 'Unknown'
                items['invasive_ventilation'] = 'Unknown'
                items['last_fvc'] = 'Unknown'

            molecular_data = MolecularData.objects.filter(patient_id=d.patient.id)

            if molecular_data:
                variation = Variation.objects.filter(molecular_data_id = molecular_data[0].patient_id)
            else:
                variation = None

            if variation:
                items['gene'] = str(self.get_gene_name(variation[0].gene_id))
                items['exon'] = str(variation[0].exon)
                items['dna_variation'] = str(variation[0].dna_variation)
                items['deletion'] = str(self.yes_no_str(variation[0].deletion_all_exons_tested))
                items['duplication'] = str(self.yes_no_str(variation[0].duplication_all_exons_tested))
                items['deletion_duplication'] = str(self.yes_no_str(variation[0].exon_boundaries_known))
                items['point_mutation'] = str(self.yes_no_str(variation[0].point_mutation_all_exons_sequenced))
                items['all_exons_in_male_relative'] = str(self.yes_no_str(variation[0].all_exons_in_male_relative))
            else:
                items['gene'] = 'Unknown'
                items['exon'] = 'Unknown'
                items['dna_variation'] = 'Unknown'
                items['deletion'] = 'Unknown'
                items['duplication'] = 'Unknown'
                items['deletion_duplication'] = 'Unknown'
                items['point_mutation'] = 'Unknown'
                items['all_exons_in_male_relative'] = 'Unknown'

            items['trials'] = self.clinical_trials(d)
            items['other_registries'] = self.other_registries(d)
            items['family_history'] = self.family_members(d)

            results.append(items)

        writer.writerow(self.columns)
        for r in results:
            writer.writerow((r['patient_id'], r['gene'], r['exon'], r['dna_variation'], r['deletion'], r['duplication'], r['deletion_duplication'],
                            r['point_mutation'], r['all_exons_in_male_relative'], r['diagnosis'], r['able_to_walk'],
                            r['wheelchair_use'], r['current_steroid_theraphy'], r['scoliosis_surgery'],
                            r['heartmedication'], r['trials'], r['age'], r['last_follow_up'], r['localisation'], r['able_to_sit'], r['heart_failure'], r['last_lvef'],
                            r['non_invasive_ventilation'], r['invasive_ventilation'], r['last_fvc'], r['muscle_biopsy'], r['other_registries'], r['family_history']))

        response['Content-Disposition'] = 'attachment; filename=%s' % file_name
        
        return response

    def get_diagnosis(self, working_group):
        return Diagnosis.objects.by_working_group(working_group)

    def family_members(self, obj):
        members = obj.familymember_set.all()
        if len(members) > 0:
            result = ''
            for member in members:
                result += '%s (%s - %s), ' % (member.family_member_diagnosis, member.registry_patient_id, member.relationship)
            return result[:-2]
        else:
            return 'Unknown'

    def other_registries(self, obj):
        other_regs = obj.otherregistries_set.all()
        if len(other_regs) > 0:
            result = ''
            for other_reg in other_regs:
                result += '%s, ' % other_reg.registry
            return result[:-2]
        else:
            return 'Unknown'    

    def clinical_trials(self, obj):
        trials = obj.clinicaltrials_set.all()
        if len(trials) > 0:
            result = ''
            for trial in trials:
                result += '%s, ' % trial.drug_name
            return result[:-2]
        else:
            return 'Unknown'

    def heart_medication(self, obj):
        try:
            if obj.heart:
                medications = obj.heartmedication_set.all()
                result = ''
                for medication in medications:
                    result += '%s, ' % medication.drug
                return result[:-2]
            else:
                return 'Unknown'
        except ObjectDoesNotExist:
            return 'Unknown'

    def wheelchair_use(self, motorfunction):
        if motorfunction.wheelchair_use is not None:
            return '%s, (%s years)' % (motorfunction.wheelchair_use.title(), motorfunction.wheelchair_usage_age)
        else:
            return 'Unknown'

    def yes_no_unknown_str(self, value):
        if value:
            return 'Yes'
        else:
            return 'No/Unknown'

    def get_gene_name(self, gene_id):
        return Gene.objects.get(id=gene_id).name

    def diagnosis_name(self, code):
        name = [(key,value) for key,value in Diagnosis.DIAGNOSIS_CHOICES if key==code]
        return name[0][1] if name else 'Unknown'

    def yes_no_str(self, value):
        return str('Yes') if value else str('No')

    def yes_no_pt_str(self, value):
        to_return = 'Unknown'
        if value:
            if value == 'Y':
                to_return = 'Yes'
            if value == 'PT':
                to_return = 'Yes (PT)'
            if value == 'N':
                to_return = 'No'
        return to_return
    
    def format_date(self, object, pattern):
        return object.strftime(pattern)
        