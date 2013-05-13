from django.http import HttpResponse
from django.db.models import Q

from django.contrib.auth.decorators import login_required

import csv, StringIO

from models import *
from registry.genetic.models import *

country = { 'au': 'Western Australia' }

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
        items['diagnosis'] = str(d.diagnosis)
        items['localisation'] = str(d.patient.postcode)
        
        items['last_follow_up'] = str(d.updated) if d.updated is not None else str(d.created)
        
        items['muscle_biopsy'] = str(d.muscle_biopsy) if d.muscle_biopsy is not None else ''
        
        items['able_to_walk'] = str(d.motorfunction.walk) if d.motorfunction is not None else ''
        items['wheelchair_use'] = str(d.motorfunction.wheelchair_use) if d.motorfunction is not None else ''
        items['able_to_sit'] = str(d.motorfunction.sit) if d.motorfunction is not None else ''
        
        items['current_steroid_theraphy'] = str(d.steroids.current) if d.steroids is not None else ''
        
        items['scoliosis_surgery'] = str(d.surgery.surgery) if d.surgery is not None else ''
        
        items['heart'] = str(d.heart.current) if d.heart is not None else ''
        items['heart_failure'] = str(d.heart.failure) if d.heart is not None else ''
        items['last_lvef'] = str(d.heart.lvef) if d.heart is not None else ''

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
                        r['wheelchair_use'], r['current_steroid_theraphy'], r['scoliosis_surgery'],
                        r['heart'], r['trials'], r['age'], r['last_follow_up'], r['localisation'], r['able_to_sit'], r['heart_failure'], r['last_lvef'],
                        r['non_invasive_ventilation'], r['invasive_ventilation'], r['last_fvc'], r['muscle_biopsy'], r['other_registries'], r['family_history']))
    
    response['Content-Disposition'] = 'attachment; filename=nmdreport_' + working_group + '.csv'
    return response

# special query for Hugh
@login_required
def squerycsv(request, working_group):

    # from the book Python Web Development with Django p 246
    response = HttpResponse(mimetype="text/csv")
    writer = csv.writer(response)

    results = specialquery(working_group)
    for r in results:
        writer.writerow((r["startbirthdate"], r["endbirthdate"],
                r["ambulant"], r["nonambulant"], r["ambulantunknown"],
                r["onsteroids"], r["notonsteroids"], r["steroidsunknown"],
                r["trial"], r["total"]))
    response['Content-Disposition'] = 'attachment; filename=query_' + working_group + '.csv'
    return response

@login_required
def squery(request, working_group):

    results = specialquery(working_group)
    return HttpResponse("squery results: %s" % results)

@login_required
def squeryreport(request, working_group):
    results = get_report(working_group)
    return HttpResponse("%s" % results)

@login_required
def squeryreportcsv(results, working_group):
    response = HttpResponse(mimetype="text/csv")
    writer = csv.writer(response)
    
    results = get_report(working_group)
    
    for result in results:
        writer.writerow((
            str(result.patient.date_of_birth.strftime('%m/%Y')), 
            str(result.updated.strftime('%d/%m/%Y')),
            str(result.patient.postcode)
        ))
    
    response['Content-Disposition'] = 'attachment; filename=report_' + working_group + '.csv'
    return response

def specialquery(working_group):
    dateranges = (
        ('2011-06-16', '2020-12-31'),
        ('2008-06-16', '2011-06-15'),
        ('2005-06-16', '2008-06-15'),
        ('2002-06-16', '2005-06-15'),
        ('1999-06-16', '2002-06-15'),
        ('1996-06-16', '1999-06-15'),
        ('1993-06-16', '1996-06-15'),
        ('1900-01-01', '1993-06-15')
        )

    results = [getqueryresults(d, working_group) for d in dateranges]
    return results

def getqueryresults(daterange, working_group):
    '''
    returns a dictionary with STRING values for: startbirthdate, endbirthdate
                ambulant, nonambulant, ambulantunknown,
                onsteroids, notonsteroids, steroidsunknown,
                trial, total
    for the birth date range passed in
    '''
    results = {'startbirthdate': str(daterange[0]), 'endbirthdate': str(daterange[1])}

    # get the diagnoses for the patients in the age range requested
    q0 = Diagnosis.objects.filter(patient__date_of_birth__gte=daterange[0])

    # filter by working group
    if working_group == 'nz':
        q_wg = q0.filter(patient__working_group__name__iexact='NEW ZEALAND')
    if working_group == 'au':
        q_wg = q0.filter(~Q(patient__working_group__name__iexact='NEW ZEALAND'))

    # q1 has all the diagnoses for patients with their birth date wihton the date range
    q1 = q_wg.filter(patient__date_of_birth__lte=daterange[1])

    total = q1.filter(motorfunction__walk=True).filter(steroids__current=True).count()
    results['total'] = str(total)

    ambulant = q1.filter(motorfunction__walk=True).count()
    nonambulant = q1.filter(motorfunction__walk=False).count()
    ambulantunknown = 0  # NOTE: we don't have an unknown for walk q1.filter(motorfunction__walk=????).count()

    results['ambulant'] = str(ambulant)
    results['nonambulant'] = str(nonambulant)
    results['ambulantunknown'] = str(ambulantunknown)

    onsteroids = q1.filter(steroids__current=True).count()
    # TODO: check that the filter is an AND here
    notonsteroids = q1.filter(steroids__current=False).filter(steroids__previous=0).count()
    steroidsunknown = q1.filter(steroids__current__isnull=True).count()

    results['onsteroids'] = str(onsteroids)
    results['notonsteroids'] = str(notonsteroids)
    results['steroidsunknown'] = str(steroidsunknown)

    # we don't have the fields for trials current, previously and unknown
    # if there is at least one trial record then trial is true,
    # since all the fields are required in a ClinicalTrial record
    trial = 0
    for d in q1:
        if d.clinicaltrials_set and d.clinicaltrials_set.count() != 0:
            trial = trial + 1
    results['trial'] = str(trial)

    # print "results: %s" % (str(results),)
    return results

def get_report(working_group):
    query = Diagnosis.objects.all()

    if working_group == 'nz':
        q0 = query.filter(patient__working_group__name__iexact='NEW ZEALAND')
    if working_group == 'au':
        q0 = query.filter(~Q(patient__working_group__name__iexact='NEW ZEALAND'))

    return q0