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
        items['diagnosis'] = str(diagnosis_name(d.diagnosis))
        items['localisation'] = str(d.patient.postcode)

        items['last_follow_up'] = str(d.updated) if d.updated is not None else str(d.created)

        items['muscle_biopsy'] = yes_no_str(d.muscle_biopsy) if d.muscle_biopsy is not None else 'Unknown'

        items['able_to_walk'] = yes_no_unknown_str(d.motorfunction.walk) if d.motorfunction is not None else 'No/Unknown'
        items['wheelchair_use'] = wheelchair_use(d.motorfunction) if d.motorfunction is not None else 'Unknown'
        items['able_to_sit'] = yes_no_unknown_str(d.motorfunction.sit) if d.motorfunction is not None else 'No/Unknown'

        items['current_steroid_theraphy'] = yes_no_str(d.steroids.current) if d.steroids is not None else 'Unknown'

        items['scoliosis_surgery'] = yes_no_str(d.surgery.surgery) if d.surgery is not None else 'Unknown'

        items['heartmedication'] = heart_medication(d)
        items['heart_failure'] = yes_no_str(d.heart.failure) if d.heart is not None else 'Unknown'
        items['last_lvef'] = '%s, %s' % (d.heart.lvef, d.heart.lvef_date) if d.heart is not None else 'Unknown'

        items['non_invasive_ventilation'] = yes_no_pt_str(d.respiratory.non_invasive_ventilation) if d.respiratory is not None else 'Unknown'
        items['invasive_ventilation'] = yes_no_pt_str(d.respiratory.invasive_ventilation) if d.respiratory is not None else 'Unknown'
        items['last_fvc'] = '%s, %s' % (d.respiratory.fvc, d.respiratory.fvc_date) if d.respiratory is not None else 'Unknown'

        molecular_data = MolecularData.objects.filter(patient_id=d.patient.id)

        if molecular_data:
            variation = Variation.objects.filter(molecular_data_id = molecular_data[0].patient_id)
        else:
            variation = None

        if variation:
            items['gene'] = str(get_gene_name(variation[0].gene_id))
            items['exon'] = str(variation[0].exon)
            items['dna_variation'] = str(variation[0].dna_variation)
            items['deletion'] = str(yes_no_str(variation[0].deletion_all_exons_tested))
            items['duplication'] = str(yes_no_str(variation[0].duplication_all_exons_tested))
            items['deletion_duplication'] = str(yes_no_str(variation[0].exon_boundaries_known))
            items['point_mutation'] = str(yes_no_str(variation[0].point_mutation_all_exons_sequenced))
            items['all_exons_in_male_relative'] = str(yes_no_str(variation[0].all_exons_in_male_relative))
        else:
            items['gene'] = 'Unknown'
            items['exon'] = 'Unknown'
            items['dna_variation'] = 'Unknown'
            items['deletion'] = 'Unknown'
            items['duplication'] = 'Unknown'
            items['deletion_duplication'] = 'Unknown'
            items['point_mutation'] = 'Unknown'
            items['all_exons_in_male_relative'] = 'Unknown'

        items['trials'] = clinical_trials(d)
        items['other_registries'] = other_registries(d)
        items['family_history'] = family_members(d)

        results.append(items)

    writer.writerow((
        'Patient ID', 
        'Gene',
        'Exon',
        'DNA Variation', 
        'All Exons Tested (Deletion)', 
        'All Exons Tested (Duplications)', 
        'Exon Boundaries Known', 
        'All Exons Sequenced (Point Mutation)', 
        'All expons tested in Male Relative',
        'Diagnosis', 
        'Currently Able To Walk', 
        'Wheelchair Use', 
        'Current Steroid Theraphy', 
        'Scoliosis Surgery',
        'Current cardiac medication', 
        'Clinical Trials', 
        'Date of birth', 
        'Last updated', 
        'State/Province, postcode', 
        'Currently able to sit without support', 
        'Heart failure/cardiomyopathy', 
        'LVEF score and date',
        'Non Invasive Ventilation', 
        'Invasive Ventilation', 
        'FVC score and date', 
        'Previous Muscle Biopsy', 
        'Other Registries', 
        'Family History'))
    for r in results:
        writer.writerow((r['patient_id'], r['gene'], r['exon'], r['dna_variation'], r['deletion'], r['duplication'], r['deletion_duplication'],
                        r['point_mutation'], r['all_exons_in_male_relative'], r['diagnosis'], r['able_to_walk'],
                        r['wheelchair_use'], r['current_steroid_theraphy'], r['scoliosis_surgery'],
                        r['heartmedication'], r['trials'], r['age'], r['last_follow_up'], r['localisation'], r['able_to_sit'], r['heart_failure'], r['last_lvef'],
                        r['non_invasive_ventilation'], r['invasive_ventilation'], r['last_fvc'], r['muscle_biopsy'], r['other_registries'], r['family_history']))

    response['Content-Disposition'] = 'attachment; filename=dmd_nmdreport_' + working_group + '.csv'
    return response

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
        return 'Unknown'

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
    if motorfunction.wheelchair_use is not None:
        return '%s, (%s years)' % (motorfunction.wheelchair_use.title(), motorfunction.wheelchair_usage_age)
    else:
        return 'Unknown'

def yes_no_unknown_str(value):
    if value:
        return 'Yes'
    else:
        return 'No/Unknown'

def get_gene_name(gene_id):
    return Gene.objects.get(id=gene_id).name

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

@login_required
def dmd_report(request, working_group):
    response = HttpResponse(mimetype="text/csv")
    writer = csv.writer(response)

    writer.writerow(('Age', 'Genetic Information', 'Ambulant', 'Non-ambulant/unknown', 'On steroids', 'Not on steroids', 'Steroids unknown', 'Cardiomyopathy', 'No Cardiomyopathy', 'Cardiomyopathy unknown', 'LVEF > 50%', 'Total'))

    date_ranges= (
        ('1999-08-02', '2006-08-01'),
    )

    for genetic in (True, False):
        results = [get_dmd_results(d, genetic, working_group) for d in date_ranges]

        genetic_message = 'Genetic confirmation' if genetic else 'No genetic confirmation or unknown'

        for result in results:
            writer.writerow((
                result['age'],
                genetic_message,
                result['ambulant'],
                result['non-ambulant'],
                result['onsteroids'],
                result['notonsteroids'],
                result['steroidsunknown'],
                result['cardiomyopathy_yes'],
                result['cardiomyopathy_no'],
                result['cardiomyopathy_unknown'],
                result['lvef'],
                result['total']
                ))

    response['Content-Disposition'] = 'attachment; filename=dmd_report_%s.csv' % (working_group)
    return response

def get_dmd_results(date_range, genetic, working_group):

    wg_q = Q(patient__working_group__name__iexact='NEW ZEALAND')

    if working_group == 'au':
        wg_q = ~wg_q

    diagnosis = Diagnosis.objects.filter(patient__sex ='M').filter(wg_q)
    diagnosis = diagnosis.filter(patient__date_of_birth__range=(date_range[0], date_range[1]))

    # Find the patients who have genetic data. That is, there exist
    # Variation objects for these patients.
    g_patient_ids = diagnosis.values_list("patient__id", flat=True)
    variations = Variation.objects.filter(molecular_data__patient__id__in=g_patient_ids)
    variations = variations.filter(Q(deletion_all_exons_tested=True) |
                                   Q(duplication_all_exons_tested=True) |
                                   Q(exon_boundaries_known=True) |
                                   Q(point_mutation_all_exons_sequenced=True) |
                                   Q(all_exons_in_male_relative=True))
    g_patient_ids = variations.values_list("molecular_data__patient__id", flat=True)

    if genetic:
        diagnosis = diagnosis.filter(patient__id__in=g_patient_ids)
    else:
        diagnosis = diagnosis.exclude(patient_id__in=g_patient_ids)

    results = { 'age': date_range[0] +' - ' + date_range[1]}

    results['ambulant'] = diagnosis.filter(motorfunction__walk = True).count()
    results['non-ambulant'] = diagnosis.filter(Q(motorfunction__walk__isnull=True) |
                                               Q(motorfunction__walk=False)).count()

    results['onsteroids'] = diagnosis.filter(steroids__current=True).count()
    results['notonsteroids'] = diagnosis.filter(steroids__current=False).count()
    results['steroidsunknown'] = diagnosis.filter(steroids__current__isnull=True).count()

    results['cardiomyopathy_yes'] = diagnosis.filter(heart__failure=True).count()
    results['cardiomyopathy_no'] = diagnosis.filter(heart__failure=False).count()
    results['cardiomyopathy_unknown'] = diagnosis.filter(heart__failure__isnull=True).count()

    results['lvef'] = diagnosis.filter(heart__lvef__gt = 50).count()

    qualifying = diagnosis
    qualifying = qualifying.filter(motorfunction__walk=True)
    qualifying = qualifying.filter(steroids__current=True)
    qualifying = qualifying.filter(heart__failure=False)

    results['total'] = qualifying.count()

    return results

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
