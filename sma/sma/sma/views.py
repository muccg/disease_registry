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
        'motorfunction', 'surgery', 'respiratory')

    results = []

    for d in diagnosis:
        items = {}

        items['patient_id'] = str(d.patient.id)
        items['age'] = str(d.patient.date_of_birth)
        items['diagnosis'] = str(d.diagnosis)
        items['localisation'] = str(d.patient.postcode)

        items['last_follow_up'] = str(d.updated) if d.updated is not None else str(d.created)

        #items['muscle_biopsy'] = str(d.muscle_biopsy) if d.muscle_biopsy is not None else ''

        items['able_to_walk'] = str(d.motorfunction.walk) if d.motorfunction is not None else ''
        items['wheelchair_use'] = str(d.motorfunction.wheelchair_use) if d.motorfunction is not None else ''
        items['able_to_sit'] = str(d.motorfunction.sit) if d.motorfunction is not None else ''

        #items['current_steroid_theraphy'] = str(d.steroids.current) if d.steroids is not None else ''

        items['scoliosis_surgery'] = str(d.surgery.surgery) if d.surgery is not None else ''

        #items['heart'] = str(d.heart.current) if d.heart is not None else ''
        #items['heart_failure'] = str(d.heart.failure) if d.heart is not None else ''
        #items['last_lvef'] = str(d.heart.lvef) if d.heart is not None else ''

        items['non_invasive_ventilation'] = str(d.respiratory.non_invasive_ventilation) if d.respiratory is not None else ''
        items['invasive_ventilation'] = str(d.respiratory.invasive_ventilation) if d.respiratory is not None else ''
        items['last_fvc'] = str(d.respiratory.fvc) if d.respiratory is not None else ''

        molecular_data = MolecularData.objects.filter(patient_id=d.patient.id)
        variation = Variation.objects.filter(molecular_data_id = molecular_data[0].patient_id)

        if variation:
            items['deletion'] = str(variation[0].deletion_all_exons_tested)
            items['duplication'] = str(variation[0].duplication_all_exons_tested)
            items['deletion_duplication'] = str(variation[0].exon_boundaries_known)
            items['point_mutation'] = str(variation[0].point_mutation_all_exons_sequenced)
        else:
            items['deletion'] = ''
            items['duplication'] = ''
            items['deletion_duplication'] = ''
            items['point_mutation'] = ''

        trials = ClinicalTrials.objects.filter(diagnosis_id=d.id)
        items['trials'] = str('Y') if trials else str('N')

        other_regs = OtherRegistries.objects.filter(diagnosis_id=d.id)
        items['other_registries'] = str('Y') if other_regs else str('N')

        family_history = FamilyMember.objects.filter(diagnosis_id=d.id)
        items['family_history'] = str('Y') if family_history else str('N')

        results.append(items)

    writer.writerow(('Patient ID', 'Mutation Name', 'Deletion', 'Duplication', 'Deletion/Duplication', 'Point Mutation', 'Targeted mutation testing',
                    'Diagnosis', 'Able To Walk', 'Wheelchair Use', 'Current Steroid Theraphy', 'Scoliosis Surgery',
                    'Heart', 'Trials', 'Age', 'Last Follow-up', 'Localisation', 'Able To Sit', 'Heart Failure', 'Last LVEF',
                    'Non Invasive Ventilation', 'Invasive Ventilation', 'Last FVC', 'Muscle Biopsy', 'Other Registries', 'Family History'))
    for r in results:
        writer.writerow((r['patient_id'], '', r['deletion'], r['duplication'], r['deletion_duplication'],
                        r['point_mutation'], '', r['diagnosis'], r['able_to_walk'],
                        r['wheelchair_use'], '', r['scoliosis_surgery'],
                        '', r['trials'], r['age'], r['last_follow_up'], r['localisation'], r['able_to_sit'], '', '',
                        r['non_invasive_ventilation'], r['invasive_ventilation'], r['last_fvc'], '', r['other_registries'], r['family_history']))

    response['Content-Disposition'] = 'attachment; filename=nmdreport_' + working_group + '.csv'
    return response
