from django.http import HttpResponse
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.decorators import login_required

import csv, StringIO
import time

from models import *
from registry.genetic.models import *

@login_required
def nmd_report(request, working_group):
    response = HttpResponse(mimetype="text/csv")
    writer = csv.writer(response)

    if working_group == 'nz':
        country_filter = Q(patient__working_group__name='NEW ZEALAND')
    if working_group == 'au':
        country_filter = ~Q(patient__working_group__name='NEW ZEALAND')

    diagnosis = Diagnosis.objects.all().filter(country_filter).select_related(
        'motorfunction', 'steroids', 'surgery', 'heart', 'heartmedication', 'respiratory', 'feedingfunction')

    results = []

    for d in diagnosis:
        items = {}

        items['patient_id'] = str(d.patient.id)
        items['age'] = str(d.patient.date_of_birth)
        items['diagnosis'] = str(diagnosis_name(d.diagnosis))
        items['localisation'] = str(d.patient.postcode)

        items['last_follow_up'] = str(d.updated.strftime('%Y-%m-%d')) if d.updated is not None else str(d.updated.strftime('%Y-%m-%d'))

        try:
            items['able_to_walk'] = yes_no_unknown_str(d.motorfunction.walk)
            items['wheelchair_use'] = wheelchair_use(d.motorfunction)
            items['able_to_sit'] = yes_no_unknown_str(d.motorfunction.sit)
            items['motor_function'] = motor_function(d.motorfunction)
        except ObjectDoesNotExist:
            items['able_to_walk'] = 'No/Unknown'
            items['wheelchair_use'] = 'Unknown'
            items['able_to_sit'] = 'No/Unknown'
            items['motor_function'] = 'No/Unknown'

        try:
            items['scoliosis_surgery'] = yes_no_str(d.surgery.surgery)
        except ObjectDoesNotExist:
            items['scoliosis_surgery'] = 'Unknown'

        try:
            items['feeding_function'] = yes_no_str(d.feedingfunction.gastric_nasal_tube)
        except ObjectDoesNotExist:
            items['feeding_function'] = 'Unknown'

        try:
            items['non_invasive_ventilation'] = yes_no_pt_str(d.respiratory.non_invasive_ventilation)
            items['invasive_ventilation'] = yes_no_pt_str(d.respiratory.invasive_ventilation)
            items['last_fvc'] = yes_no_str(d.respiratory.fvc)
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
            items['gene'] = str(get_gene_name(variation[0].gene_id))
        else:
            items['gene'] = 'Unknown'

        items['trials'] = clinical_trials(d)
        items['other_registries'] = other_registries(d)
        items['family_history'] = family_members(d)

        items['sma_classification'] = str(get_classification(d.classification))
        
        results.append(items)

    writer.writerow((
        'Patient ID', 
        'Gene',
        'Diagnosis', 
        'Currently Able To Walk', 
        'Wheelchair Use',
        'Motor Function', 
        'Scoliosis Surgery',
        'Gastric/nasal tube',
        'Clinical Trials', 
        'Date of birth', 
        'Last updated', 
        'State/Province, postcode', 
        'Currently able to sit without support', 
        'Non Invasive Ventilation', 
        'Invasive Ventilation', 
        'FVC score and date', 
        'Other Registries', 
        'Family History',
        'SMA Classification'))
    for r in results:
        writer.writerow((r['patient_id'], r['gene'], r['diagnosis'], r['able_to_walk'],
                        r['wheelchair_use'], r['motor_function'], r['scoliosis_surgery'], r['feeding_function'],
                        r['trials'], r['age'], r['last_follow_up'], r['localisation'], r['able_to_sit'], 
                        r['non_invasive_ventilation'], r['invasive_ventilation'], r['last_fvc'], r['other_registries'], r['family_history'], r['sma_classification']))

    response['Content-Disposition'] = 'attachment; filename=sma_nmdreport_' + working_group + '.csv'
    return response

def motor_function(obj):
    if obj.best_function == 'walking':
        return '%s - %s year(s)' % (obj.best_function.title(), obj.acquisition_age if obj.acquisition_age is not None else 'Unknown')
    else:
        return obj.best_function.title()
    

def family_members(obj):
    members = obj.familymember_set.all()
    if len(members) > 0:
        result = ''
        for member in members:
            result += '%s (%s - %s), ' % (member.family_member_diagnosis, member.registry_patient_id, member.relationship)
        return result[:-2]
    else:
        return 'Unknown'

def other_registries(obj):
    other_regs = obj.otherregistries_set.all()
    if len(other_regs) > 0:
        result = ''
        for other_reg in other_regs:
            result += '%s, ' % other_reg.registry
        return result[:-2]
    else:
        return 'Unknown'    

def clinical_trials(obj):
    trials = obj.clinicaltrials_set.all()
    if len(trials) > 0:
        result = ''
        for trial in trials:
            result += '%s, ' % trial.drug_name
        return result[:-2]
    else:
        return 'No/Unknown'

def heart_medication(obj):
    if obj.heart:
        medications = obj.heartmedication_set.all()
        result = ''
        for medication in medications:
            result += '%s, ' % medication.drug
        return result[:-2]
    else:
        return 'Unknown'

def wheelchair_use(motorfunction):
    return '%s, (%s years)' % (motorfunction.wheelchair_use.title(), motorfunction.wheelchair_usage_age)

def yes_no_unknown_str(value):
    if value:
        return 'Yes'
    else:
        return 'No/Unknown'

def get_gene_name(gene_id):
    return Gene.objects.get(id=gene_id).name

def get_classification(code):
    name = [(key,value) for key, value in Diagnosis.SMA_CLASSIFICATION_CHOICES if key==code]
    return name[0][1] if name else 'Unknown'

def diagnosis_name(code):
    name = [(key,value) for key,value in Diagnosis.DIAGNOSIS_CHOICES if key==code]
    return name[0][1] if name else 'Unknown'

def yes_no_str(value):
    return str('Yes') if value else str('No')

def yes_no_pt_str(value):
    to_return = 'Unknown'
    if value:
        if value == 'Y':
            to_return = 'Yes'
        if value == 'PT':
            to_return = 'Yes (PT)'
        if value == 'N':
            to_return = 'No'
    return to_return
