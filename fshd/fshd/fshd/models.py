# -*- coding: utf-8 -*-
# vim: set fileencoding=UTF-8:
import traceback, datetime
from django.db import models
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist
from fshd.fshd import base
from registry.genetic.models import MolecularData
#from patients.models import Patient as BasePatient
from registry.patients.models import Patient
from registry.groups.models import User
from registry.mail import sendNewPatientEmail


import logging
logger = logging.getLogger('fshd')

'''
#subclass the patients/Patient to override the choices for gender
class Patient(BasePatient):
    SEX_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        #("X", "Other/Intersex"),   # Trac #16 item 9
    )
'''

class Diagnosis(base.Diagnosis):
    patient = models.OneToOneField(Patient, primary_key=True, related_name='patient_diagnosis')

    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)

    class Meta:
        ordering = ["patient"]
        verbose_name = "FSHD Registry entry"   #"clinical diagnosis"
        verbose_name_plural = "FSHD Registry" # "clinical diagnoses"

    def __unicode__(self):
        return str(self.patient)

    def save(self, *args, **kwargs):
        '''On save, update timestamps, auto-fields reportedly unreliable'''
        if not self.created:
            self.created = datetime.datetime.now()
        self.updated = datetime.datetime.now()
        super(Diagnosis, self).save(*args, **kwargs)


    def percentage_complete(self):
        score = 0.0
        fieldlist = ['motorfunction', 'surgery', 'heart', 'respiratory', 'muscle', 'feedingfunction', 'fatigue', 'ethnicorigin']
        for f in fieldlist:
            try:
                getattr(self, f)
                score += 1.0
            except ObjectDoesNotExist, e:
                pass
        return  int(score / len(fieldlist) * 100.0)

    def incomplete_sections(self):
        fieldlist = ['motorfunction', 'surgery', 'heart', 'respiratory', 'muscle', 'feedingfunction', 'fatigue', 'ethnicorigin']
        fields_to_complete = []
        for f in fieldlist:
            try:
                getattr(self, f)
            except ObjectDoesNotExist, e:
                fields_to_complete.append(f)

        if fields_to_complete:
            return "Incomplete sections: %s." % ", ".join(fields_to_complete)
        else:
            return "All sections complete."

    def progress_graph(self):
        """This strictly speaking should be on the admin as it is used there,
        but if included on the model we can access it from registry.patient
        as well as from the diagnosis admin
        """
        graph_html = '<img title="%s" src="http://chart.apis.google.com/chart' % self.incomplete_sections()
        graph_html += '?chf=bg,s,FFFFFF00&chs=200x15&cht=bhs&chco=4D89F9,C6D9FD&chd=t:%d|100&chbh=5"/>' % self.percentage_complete()
        return graph_html

class ClinicalFeatures(base.ClinicalFeatures):
    diagnosis = models.OneToOneField(Diagnosis, primary_key=True)
    def __unicode__(self):
        return str(self.diagnosis)
    class Meta:
        verbose_name_plural = "clinical features"

class Heart(base.Heart):
    diagnosis = models.OneToOneField(Diagnosis, primary_key=True)

    class Meta:
        verbose_name_plural = "heart"

    def __unicode__(self):
        return str(self.diagnosis)




class Respiratory(base.Respiratory):
    diagnosis = models.OneToOneField(Diagnosis, primary_key=True)

    class Meta:
        verbose_name_plural = "respiratory"

    def __unicode__(self):
        return str(self.diagnosis)




class GeneticTestDetails(base.GeneticTestDetails):
    diagnosis = models.OneToOneField(Diagnosis, primary_key=True)

    class Meta:
        verbose_name_plural = "genetic test details"

    def __unicode__(self):
        return str(self.diagnosis)


class EthnicOrigin(base.EthnicOrigin):
    diagnosis = models.OneToOneField(Diagnosis, primary_key=True)

    def __unicode__(self):
        return str(self.diagnosis)


class ClinicalTrials(base.ClinicalTrials):
    diagnosis = models.ForeignKey(Diagnosis)

    class Meta:
        verbose_name_plural = "clinical trials"

    def __unicode__(self):
        return str(self.diagnosis)


class OtherRegistries(base.OtherRegistries):
    diagnosis = models.ForeignKey(Diagnosis)

    class Meta:
        verbose_name_plural = "other registries"

    def __unicode__(self):
        return str(self.diagnosis)

class Notes(models.Model):
    diagnosis = models.OneToOneField(Diagnosis, primary_key=True)
    notes = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "notes"

    def __unicode__(self):
        return str(self.diagnosis)

class FamilyMember(base.FamilyMember):
    diagnosis = models.ForeignKey(Diagnosis)
    registry_patient = models.OneToOneField(Patient, blank=True, null=True, verbose_name="Family members with Myotonic dystrophy", related_name="%(app_label)s_%(class)s_related")

    def __unicode__(self):
        return str(self.diagnosis)

class Consent(base.Consent):
    diagnosis = models.OneToOneField(Diagnosis, primary_key=True)

    def __unicode__(self):
        return str(self.diagnosis)

# This model is actually based off the molecular data and not the diagnosis,
# but is FSHD specific, and hence placed here.
class DiagnosticCategory(models.Model):
    CATEGORY_CHOICES = (
        ("DNA test positive: CTG repeat >50", "DNA test positive: CTG repeat >50"),
        ("DNA test negative: CTG repeat <37", "DNA test negative: CTG repeat <37"),
        ("DNA test positive: CCTG repeat >75", "DNA test positive: CCTG repeat >75"),
        ("DNA test negative: CCTG repeat <75", "DNA test negative: CCTG repeat <75"),
        ("DNA test (DM-1 or DM-2) not done", "DNA test (DM-1 or DM-2) not done"),
    )

    molecular_data = models.OneToOneField(MolecularData, primary_key=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    repeat_size = models.IntegerField(null=True, blank=True)
    relative_test = models.BooleanField(verbose_name="DNA test performed on relative")
    relative_ctg_repeat = models.IntegerField(null=True, blank=True, verbose_name="size of CTG repeat")
    relative_cctg_repeat = models.IntegerField(null=True, blank=True, verbose_name="size of CCTG repeat")

    class Meta:
        verbose_name_plural = "diagnostic categories"

    def __unicode__(self):
        return str(self.molecular_data)


def signal_patient_post_save(sender, **kwargs):
    logger.debug("patient post_save signal")

    try:
        patient = kwargs['instance']
        diagnosis, created = Diagnosis.objects.get_or_create(patient=patient)
        logger.debug("Diagnosis record %s" % ("created" if created else "already existed"))
    except Exception, e:
        logger.critical(e)
        logger.critical(traceback.format_exc())
        raise

def signal_diagnosis_post_save(sender, **kwargs):
    diagnosis = kwargs['instance']
    working_group_id = diagnosis.patient.working_group.id
    regusers = User.objects.filter(working_group__id=working_group_id).filter(user__groups__id__in = [2,3]).distinct()

    email_to = []

    for reguser in regusers:
        email_to.append(reguser.user.email)

    sendNewPatientEmail(email_to)

# connect up django signals
post_save.connect(signal_patient_post_save, sender=Patient)
post_save.connect(signal_diagnosis_post_save, sender=Diagnosis)
