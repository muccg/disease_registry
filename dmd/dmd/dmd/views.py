from django.http import HttpResponse
from django.db.models import Q

import csv, StringIO

from models import *

# special query for Hugh
def squerycsv(request):

    # from the book Python Web Development with Django p 246
    response = HttpResponse(mimetype="text/csv")
    writer = csv.writer(response)

    results = specialquery()
    for r in results:
        writer.writerow((r["startbirthdate"], r["endbirthdate"],
                r["ambulant"], r["nonambulant"], r["ambulantunknown"],
                r["onsteroids"], r["notonsteroids"], r["steroidsunknown"],
                r["trial"], r["total"]))
    response['Content-Disposition'] = 'attachment; filename=query.csv'
    return response

def squery(request, working_group):

    results = specialquery(working_group)
    return HttpResponse("squery results: %s" % results)

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

    print "patients: %s" % str([d.patient.family_name for d in q1])
    total = q1.count()
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
