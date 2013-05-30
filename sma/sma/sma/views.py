from django.http import HttpResponse
from django.db.models import Q

from django.contrib.auth.decorators import login_required

import csv, StringIO

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
        'motorfunction', 'steroids', 'surgery', 'heart', 'heartmedication', 'respiratory')

    results = []

    for d in diagnosis:
        items = {}

        items['patient_id'] = str(d.patient.id)
        items['age'] = str(d.patient.date_of_birth)
        items['diagnosis'] = str(diagnosis_name(d.diagnosis))
        items['localisation'] = str(d.patient.postcode)

        items['last_follow_up'] = str(d.updated) if d.updated is not None else str(d.created)

#        items['muscle_biopsy'] = yes_no_str(d.muscle_biopsy) if d.muscle_biopsy is not None else 'Unknown'

        items['able_to_walk'] = yes_no_str(d.motorfunction.walk) if d.motorfunction is not None else 'Unknown'
        items['wheelchair_use'] = yes_no_str(d.motorfunction.wheelchair_use) if d.motorfunction is not None else 'Unknown'
        items['able_to_sit'] = yes_no_str(d.motorfunction.sit) if d.motorfunction is not None else 'Unknown'

#        items['current_steroid_theraphy'] = yes_no_str(d.steroids.current) if d.steroids is not None else 'Unknown'

        items['scoliosis_surgery'] = yes_no_str(d.surgery.surgery) if d.surgery is not None else 'Unknown'

#        items['heart'] = yes_no_str(d.heart.current) if d.heart is not None else 'Unknown'
#        items['heart_failure'] = yes_no_str(d.heart.failure) if d.heart is not None else 'Unknown'
#        items['last_lvef'] = yes_no_str(d.heart.lvef) if d.heart is not None else 'Unknown'

        items['non_invasive_ventilation'] = yes_no_pt_str(d.respiratory.non_invasive_ventilation) if d.respiratory is not None else 'Unknown'
        items['invasive_ventilation'] = yes_no_pt_str(d.respiratory.invasive_ventilation) if d.respiratory is not None else 'Unknown'
        items['last_fvc'] = yes_no_str(d.respiratory.fvc) if d.respiratory is not None else 'Unknown'

        molecular_data = MolecularData.objects.filter(patient_id=d.patient.id)

        if molecular_data:
            variation = Variation.objects.filter(molecular_data_id = molecular_data[0].patient_id)
        else:
            variation = None

        if variation:
            items['deletion'] = str(variation[0].deletion_all_exons_tested)
            items['duplication'] = str(variation[0].duplication_all_exons_tested)
            items['deletion_duplication'] = str(variation[0].exon_boundaries_known)
            items['point_mutation'] = str(variation[0].point_mutation_all_exons_sequenced)
            items['all_exons_in_male_relative'] = str(variation[0].all_exons_in_male_relative)
        else:
            items['deletion'] = 'Unknown'
            items['duplication'] = 'Unknown'
            items['deletion_duplication'] = 'Unknown'
            items['point_mutation'] = 'Unknown'
            items['all_exons_in_male_relative'] = 'Unknown'

        trials = ClinicalTrials.objects.filter(diagnosis_id=d.id)
        items['trials'] = yes_no_str(trials)

        other_regs = OtherRegistries.objects.filter(diagnosis_id=d.id)
        items['other_registries'] = yes_no_str(other_regs)

        family_history = FamilyMember.objects.filter(diagnosis_id=d.id)
        items['family_history'] = yes_no_str(family_history)

        results.append(items)

    writer.writerow((
        'Patient ID', 
        'Mutation Name', 
        'All Exons Tested (Deletion)', 
        'All Exons Tested (Duplications)', 
        'Exon Boundaries Known', 
        'All Exons Sequenced (Point Mutation)', 
        'All expons tested in Male Relative',
        'Diagnosis', 
        'Currently Able To Walk', 
        'Wheelchair Use', 
        'Scoliosis Surgery',
        'Clinical Trials', 
        'Date of birth', 
        'Last updated', 
        'State/Province, postcode', 
        'Currently able to sit without support', 
        'Non Invasive Ventilation', 
        'Invasive Ventilation', 
        'FVC score and date', 
        'Other Registries', 
        'Family History'))
    for r in results:
        writer.writerow((r['patient_id'], '', r['deletion'], r['duplication'], r['deletion_duplication'],
                        r['point_mutation'], r['all_exons_in_male_relative'], r['diagnosis'], r['able_to_walk'],
                        r['wheelchair_use'], r['scoliosis_surgery'],
                        r['trials'], r['age'], r['last_follow_up'], r['localisation'], r['able_to_sit'], 
                        r['non_invasive_ventilation'], r['invasive_ventilation'], r['last_fvc'], r['other_registries'], r['family_history']))

    response['Content-Disposition'] = 'attachment; filename=nmdreport_' + working_group + '.csv'
    return response

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
