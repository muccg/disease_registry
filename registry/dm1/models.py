# -*- coding: utf-8 -*-
# vim: set fileencoding=UTF-8:
import traceback, datetime
from django.db import models
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist
from dm1 import base
from genetic.models import MolecularData
#from patients.models import Patient as BasePatient
from patients.models import Patient

import logging
logger = logging.getLogger('dm1')

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
    patient = models.OneToOneField(Patient, primary_key=True)

    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)

    class Meta:
        ordering = ["patient"]
        verbose_name = "Myotonic Dystrophy Registry entry"   #"clinical diagnosis"
        verbose_name_plural = "Myotonic Dystrophy Registry" # "clinical diagnoses"

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



class MotorFunction(base.MotorFunction):
    diagnosis = models.OneToOneField(Diagnosis, primary_key=True)

    class Meta:
        verbose_name_plural = "motor function"

    def __unicode__(self):
        return str(self.diagnosis)



class Surgery(base.Surgery):
    diagnosis = models.OneToOneField(Diagnosis, primary_key=True)

    class Meta:
        verbose_name_plural = "surgeries"

    def __unicode__(self):
        return str(self.diagnosis)


class Heart(base.Heart):
    diagnosis = models.OneToOneField(Diagnosis, primary_key=True)

    class Meta:
        verbose_name_plural = "heart"

    def __unicode__(self):
        return str(self.diagnosis)


class HeartMedication(base.HeartMedication):
    diagnosis = models.ForeignKey(Diagnosis)

    class Meta:
        verbose_name_plural = "heart medication"

    def __unicode__(self):
        return str(self.diagnosis.patient)


class Muscle(base.Muscle):
    # Trac 16 #53 Removed
    '''
    GRIP_PERCUSSION_MYOTONIA_CHOICES = (
        ("Good", "Good"),
        ("OK", "OK"),
        ("Poor", "Poor"),
        ("OT", "Receiving occupational therapy"),
    )
    '''
    MRC_CHOICES = (
        (5, "5"),
        (4.5, "4+"),
        (4, "4"),
        (3, "3"),
        (2, "2"),
        (1, "1"),
    )

    UYN_CHOICES = (
        ('U', 'Unknown'),
        ('Y', 'Yes'),
        ('N', 'No'),
    )

    MRC_HELP_TEXT = "MRC scale of muscle grading: 5=normal to 1=extreme weakness"

    diagnosis = models.OneToOneField(Diagnosis, primary_key=True)

## ADAM - these fields don't seem to be in the frontend now and were causing db errors so have made them nullable
    ## they are shown in the Registry but not in the Questionnaire
    flexor_digitorum_profundis = models.DecimalField(max_digits=2, decimal_places=1, choices=MRC_CHOICES, help_text=MRC_HELP_TEXT, null=True, blank=True)
    tibialis_anterior = models.DecimalField(max_digits=2, decimal_places=1, choices=MRC_CHOICES, help_text=MRC_HELP_TEXT, null=True, blank=True)
    neck_flexion = models.DecimalField(max_digits=2, decimal_places=1, choices=MRC_CHOICES, help_text=MRC_HELP_TEXT, null=True, blank=True)
    iliopsoas = models.DecimalField(max_digits=2, decimal_places=1, choices=MRC_CHOICES, help_text=MRC_HELP_TEXT, null=True, blank=True)
    #face = models.NullBooleanField(verbose_name="facial muscle weakness", null=True, blank=True)
    face = models.CharField(max_length=1, choices=UYN_CHOICES, null=True, blank=True)

    #early_weakness = models.NullBooleanField(verbose_name="Was there any evidence of hypotonia or weakness within the first four weeks", null=True, blank=True)
    early_weakness = models.CharField(verbose_name="Was there any evidence of hypotonia or weakness within the first four weeks",max_length=1, choices=UYN_CHOICES, null=True, blank=True)
    # Trac 16 #53 Removed
    #grip_percussion_myotonia = models.CharField(max_length=4, choices=GRIP_PERCUSSION_MYOTONIA_CHOICES, verbose_name="grip or percussion myotonia", null=True, blank=True)

    class Meta:
        verbose_name_plural = "muscle"

    def __unicode__(self):
        return str(self.diagnosis)


class MuscleMedication(base.MuscleMedication):
    diagnosis = models.ForeignKey(Diagnosis)

    class Meta:
        verbose_name_plural = "muscle medication"

    def __unicode__(self):
        return str(self.diagnosis.patient)


class Respiratory(base.Respiratory):
    diagnosis = models.OneToOneField(Diagnosis, primary_key=True)

    class Meta:
        verbose_name_plural = "respiratory"

    def __unicode__(self):
        return str(self.diagnosis)


class FeedingFunction(base.FeedingFunction):
    diagnosis = models.OneToOneField(Diagnosis, primary_key=True)

    class Meta:
        verbose_name_plural = "feeding function"

    def __unicode__(self):
        return str(self.diagnosis)


class Fatigue(base.Fatigue):
    diagnosis = models.OneToOneField(Diagnosis, primary_key=True)

    class Meta:
        verbose_name_plural = "fatigue"

    def __unicode__(self):
        return str(self.diagnosis)


class FatigueMedication(base.FatigueMedication):
    diagnosis = models.ForeignKey(Diagnosis)

    class Meta:
        verbose_name_plural = "fatigue medication"

    def __unicode__(self):
        return str(self.diagnosis)


class SocioeconomicFactors(base.SocioeconomicFactors):
    diagnosis = models.OneToOneField(Diagnosis, primary_key=True)

    class Meta:
        verbose_name_plural = "socioeconomic factors"

    def __unicode__(self):
        return str(self.diagnosis)


class GeneralMedicalFactors(base.GeneralMedicalFactors):
    diagnosis = models.OneToOneField(Diagnosis, primary_key=True)

    class Meta:
        verbose_name_plural = "general medical factors"

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


class OtherRegistries(models.Model):
    diagnosis = models.ForeignKey(Diagnosis)
    registry = models.CharField(max_length=50)

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
# but is DM1 specific, and hence placed here.
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

# connect up django signals
post_save.connect(signal_patient_post_save, sender=Patient)
