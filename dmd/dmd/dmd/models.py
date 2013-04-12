# vim: set fileencoding=UTF-8:
import traceback, datetime
from django.db import models
from django.db.models.signals import post_save
from registry.patients.models import Patient
from django.core.exceptions import ObjectDoesNotExist

from smart_selects.db_fields import ChainedForeignKey

import logging
logger = logging.getLogger('dmd')

class PhenotypeHpo(models.Model):
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Human Phenotype Ontology'
        verbose_name_plural = 'Human Phenotype Ontologies'
        ordering = ["code"]
    
    def __unicode__(self):
        return self.code + ' - ' + self.description

class PhenotypeOrpha(models.Model):
    orpha_number = models.CharField(max_length=20)
    synonym = models.TextField()
    icd_10 = models.CharField(max_length=15, verbose_name='ICD-10')

    class Meta:
        verbose_name = 'ORPHA'
        verbose_name_plural = 'ORPHAs'
        ordering = ["orpha_number"]
        ordering = ["orpha_number"]
    
    def __unicode__(self):
        return self.orpha_number + ' - ' + self.synonym

class PhenotypeOrphaDisability(models.Model):
    orpha = models.ForeignKey(PhenotypeOrpha)
    disability = models.CharField(max_length=100)

    def __unicode__(self):
        return self.disability

class PhenotypeOrphaDisabilityType(models.Model):
    disability = models.ForeignKey(PhenotypeOrphaDisability)
    disability_type = models.CharField(max_length=30)

    def __unicode__(self):
        return self.disability_type

class OrphaDisabilityThesaurus(models.Model):
    orpha = models.ForeignKey(PhenotypeOrpha, related_name="orpha")
    disease = models.CharField(max_length=100)
    disability = ChainedForeignKey(
        PhenotypeOrphaDisability,
        chained_field = 'orpha',
        chained_model_field = 'orpha',
        show_all = False,
        auto_choose = True,
        related_name = 'disability_th'
    )
    disability_type = ChainedForeignKey(
        PhenotypeOrphaDisabilityType,
        chained_field = 'disability',
        chained_model_field = 'disability',
        show_all = False,
        auto_choose = True
    )
    severity = models.CharField(max_length=1)
    frequency = models.CharField(max_length=2)
    loss_of_ability = models.BooleanField()
    environmental_factor = models.BooleanField()

class Diagnosis(models.Model):
    DIAGNOSIS_CHOICES = (
        ("DMD", "Duchenne Muscular Dystrophy"),
        ("BMD", "Becker Muscular Dystrophy"),
        ("IMD", "Intermediate Muscular Dystrophy"),
        ("Oth", "Non-Duchenne/Becker Muscular Dystrophy"),
        ("Car", "Non-Symptomatic Carrier"),
        ("Man", "Manifesting carrier"), # Trac #30
    )

    orpha_disability_thesaurus = models.OneToOneField(OrphaDisabilityThesaurus, null=True, blank=True)
    phenotype_hpo = models.OneToOneField(PhenotypeHpo, null=True, blank=True, verbose_name='HPO')
    phenotype_orpha = models.OneToOneField(PhenotypeOrpha, null=True, blank=True, verbose_name="ORPHA")
    patient = models.OneToOneField(Patient, primary_key=True, related_name='patient_diagnosis')
    diagnosis = models.CharField(max_length=3, choices=DIAGNOSIS_CHOICES)
    muscle_biopsy = models.NullBooleanField(verbose_name="previous muscle biopsy")
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)

    class Meta:
        ordering = ["patient"]
        verbose_name = "clinical diagnosis"
        verbose_name_plural = "clinical diagnoses"

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
        fieldlist = ['motorfunction', 'steroids', 'surgery', 'heart', 'respiratory']
        for f in fieldlist:
            try:
                getattr(self, f)
                score += 1.0
            except ObjectDoesNotExist, e:
                pass
        return  int(score / len(fieldlist) * 100.0)

    def incomplete_sections(self):
        fieldlist = ['motorfunction', 'steroids', 'surgery', 'heart', 'respiratory']
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

class MotorFunction(models.Model):
    WHEELCHAIR_USE_CHOICES = (
        ("permanent", "Yes (Permanent)"),
        ("intermittent", "Yes (Intermittent)"),
        ("never", "Never"),
        ("unknown", "Unknown")
    )

    diagnosis = models.OneToOneField(Diagnosis, primary_key=True)
    walk = models.BooleanField(verbose_name="currently able to walk", help_text="Functional walking with or without help (orthoses or assistive device or human assistance), inside or outdoors")
    sit = models.BooleanField(verbose_name="currently able to sit without support", help_text="Able to maintain the sitting position on a chair or a wheelchair without support of upper limbs or leaning against the back of the chair")
    wheelchair_use = models.CharField(verbose_name="wheel chair use (over 3 years of age)", max_length=12, choices=WHEELCHAIR_USE_CHOICES, help_text="Yes (permanent): patient is not able to walk and needs a wheelchair to move<br/>Yes (intermittent): patient is still able to walk")
    wheelchair_usage_age = models.IntegerField(null=True, blank=True, help_text="If using wheelchair specify age at start of wheelchair use")

    class Meta:
        verbose_name_plural = "motor function"

    def __unicode__(self):
        return str(self.diagnosis)


class Steroids(models.Model):
    diagnosis = models.OneToOneField(Diagnosis, primary_key=True)
    current = models.NullBooleanField(verbose_name="current steroid therapy")
    previous = models.IntegerField(verbose_name="previous steroid therapy (years)", default=0, help_text="Enter 0 to indicate that no previous steroid therapy has occurred")

    class Meta:
        verbose_name_plural = "steroids"

    def __unicode__(self):
        return str(self.diagnosis)


class Surgery(models.Model):
    diagnosis = models.OneToOneField(Diagnosis, primary_key=True)
    surgery = models.NullBooleanField(verbose_name="scoliosis surgery", help_text="Scoliosis: lateral curvature of the spine in the coronal plane with a Cobb angle measuring more than 10°; surgery: any type of surgical procedure")

    class Meta:
        verbose_name_plural = "surgeries"

    def __unicode__(self):
        return str(self.diagnosis)


class Heart(models.Model):
    diagnosis = models.OneToOneField(Diagnosis, primary_key=True)
    current = models.NullBooleanField(verbose_name="current cardiac medication")
    failure = models.NullBooleanField(verbose_name="heart failure/ cardiomyopathy")
    lvef = models.IntegerField(null=True, blank=True, verbose_name="LVEF score", help_text="Left Ventricular Ejection Fraction (LVEF) determined by ultrasound examination of the heart; expressed in % [%=(End disatolic volume - End systolic volume) ÷ End diastolic volume] to specify last LVEF(%) and date of examination")
    lvef_date = models.DateField(null=True, blank=True, verbose_name="LVEF date")

    class Meta:
        verbose_name_plural = "heart"

    def __unicode__(self):
        return str(self.diagnosis)


class HeartMedication(models.Model):
    STATUS_CHOICES = (
        ("Current", "Current prescription"),
        ("Previous", "Previous prescription"),
    )

    diagnosis = models.ForeignKey(Diagnosis)
    drug = models.CharField(max_length=100, help_text="Specify each drug with its International Nonproprietary Name (INN)")
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)

    class Meta:
        verbose_name_plural = "heart medication"

    def __unicode__(self):
        return str(self.diagnosis.patient)


class Respiratory(models.Model):
    VENTILATION_CHOICES = (
        ("Y", "Yes"),
        ("PT", "Yes (part-time)"),
        ("N", "No"),
    )

    diagnosis = models.OneToOneField(Diagnosis, primary_key=True)
    non_invasive_ventilation = models.CharField(max_length=2, choices=VENTILATION_CHOICES, help_text="Mechanical ventilation with nasal or bucal mask. Part-time means usually at night")
    invasive_ventilation = models.CharField(max_length=2, choices=VENTILATION_CHOICES, help_text="Mechanical ventilation with tracheostomy. Part-time means usually at night")
    fvc = models.IntegerField(null=True, blank=True, verbose_name="FVC score", help_text="Pulmonary function test with spirometry; Forced Vital Capacity (FVC) expressed as % predicted for height (not in mL) and date of last examination")
    fvc_date = models.DateField(null=True, blank=True, verbose_name="FVC date")

    class Meta:
        verbose_name_plural = "respiratory"

    def __unicode__(self):
        return str(self.diagnosis)


class ClinicalTrials(models.Model):
    diagnosis = models.ForeignKey(Diagnosis)
    drug_name = models.CharField(max_length=50)
    trial_name = models.CharField(max_length=50)
    trial_sponsor = models.CharField(max_length=50)
    trial_phase = models.CharField(max_length=50)

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


class FamilyMember(models.Model):
    DIAGNOSIS_CHOICES = Diagnosis.DIAGNOSIS_CHOICES + (
        ("Non", "Non-Carrier"),
    )

    diagnosis = models.ForeignKey(Diagnosis)
    registry_patient = models.OneToOneField(Patient, blank=True, null=True, verbose_name="patient record within the registry (optional)")
    sex = models.CharField(max_length=1, choices=Patient.SEX_CHOICES)
    relationship = models.CharField(max_length=50)
    family_member_diagnosis = models.CharField(max_length=3, choices=DIAGNOSIS_CHOICES, verbose_name="diagnosis")

    def __unicode__(self):
        return str(self.diagnosis)


class Notes(models.Model):
    diagnosis = models.OneToOneField(Diagnosis, primary_key=True)
    notes = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "notes"

    def __unicode__(self):
        return str(self.diagnosis)



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
