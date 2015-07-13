# vim: set fileencoding=UTF-8:
import traceback, datetime
from django.db import models
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist
from registry.patients.models import Patient
from registry.configuration.models import EmailTemplate
from registry.mail import sendNewPatientEmail
from registry.groups.models import User

import logging
logger = logging.getLogger('sma')

class Diagnosis(models.Model):
    DIAGNOSIS_CHOICES = (
        ("SMA", "Spinal Muscular Atrophy"),
        ("Oth", "Other"),
        ("Unk", "Unknown")
    )
    SMA_CLASSIFICATION_CHOICES = (
        ("SMA1", "SMA1 - onset between 0-6months, nevers sits, natural age of death <2 years "),
        ("SMA2", "SMA2 - onset between 7-18 months, never stands, natural age of death >2 years"),
        ("SMA3", "SMA3 - onset >18 months, stands and walks (this highest function may be lost during evolution)"),
        ("Other", "Other"),
        ("Unknown", "Unknown"),
    )
    patient = models.OneToOneField(Patient, unique=True, related_name='patient_diagnosis')
    diagnosis = models.CharField(max_length=3, choices=DIAGNOSIS_CHOICES)
    classification = models.CharField(max_length=7, choices=SMA_CLASSIFICATION_CHOICES)
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
        fieldlist = ['motorfunction', 'surgery', 'feedingfunction', 'respiratory']
        for f in fieldlist:
            try:
                getattr(self, f)
                score += 1.0
            except ObjectDoesNotExist, e:
                pass
        return  int(score / len(fieldlist) * 100.0)

    def incomplete_sections(self):
        fieldlist = ['motorfunction', 'surgery', 'feedingfunction', 'respiratory']
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
    MOTOR_FUNCTION_CHOICES = (
        ("walking", "Walking independently"),
        ("sitting", "Sitting independently"),
        ("none", "Never able to walk or sit independently")
    )
    WHEELCHAIR_USE_CHOICES = (
        ("permanent", "Yes (Permanent)"),
        ("intermittent", "Yes (Intermittent)"),
        ("never", "Never"),
        ("unknown", "Unknown")
    )
    diagnosis = models.OneToOneField(Diagnosis)
    walk = models.BooleanField(verbose_name="currently able to walk", help_text="Functional walking with or without help (orthoses or assistive device or human assistance), inside or outdoors")
    sit = models.BooleanField(verbose_name="currently able to sit without support", help_text="Able to maintain the sitting position on a chair or a wheelchair without support of upper limbs or leaning against the back of the chair")
    best_function = models.CharField(max_length=7, choices=MOTOR_FUNCTION_CHOICES, help_text="Walking: functional walking with or without help (orthoses or assistive device or human assistance), inside or outdoors<br/>Sitting independently: able to maintain the sitting position on a chair or a wheelchair without support of upper limbs or leaning against the back of the chair")
    acquisition_age = models.IntegerField(null=True, blank=True, help_text="If walking or sitting specify age of acquisition in months")
    wheelchair_use = models.CharField(verbose_name="wheel chair use (over 3 years of age)", max_length=12, choices=WHEELCHAIR_USE_CHOICES, help_text="Yes (permanent): patient is not able to walk and needs a wheelchair to move<br/>Yes (intermittent): patient is still able to walk")
    wheelchair_usage_age = models.IntegerField(null=True, blank=True, help_text="If using wheelchair specify age at start of wheelchair use")

    class Meta:
        verbose_name_plural = "motor function"

    def __unicode__(self):
        return str(self.diagnosis)



class Surgery(models.Model):
    diagnosis = models.OneToOneField(Diagnosis)
    surgery = models.NullBooleanField(verbose_name="scoliosis surgery", help_text="Scoliosis: lateral curvature of the spine in the coronal plane with a Cobb angle measuring more than 10°; surgery: any type of surgical procedure")

    class Meta:
        verbose_name_plural = "surgeries"

    def __unicode__(self):
        return str(self.diagnosis)


class FeedingFunction(models.Model):
    diagnosis = models.OneToOneField(Diagnosis)
    gastric_nasal_tube = models.NullBooleanField(verbose_name="gastric/nasal tube", help_text="Nutritional supplementation via nasogastric or nasojejunal tube or gastrostomy")

    class Meta:
        verbose_name_plural = "feeding function"

    def __unicode__(self):
        return str(self.diagnosis)


class Respiratory(models.Model):
    VENTILATION_CHOICES = (
        ("Y", "Yes"),
        ("PT", "Yes (part-time)"),
        ("N", "No"),
    )
    diagnosis = models.OneToOneField(Diagnosis)
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
    registry_patient = models.OneToOneField(Patient, blank=True, null=True, verbose_name="patient record within the registry (optional)", related_name="%(app_label)s_%(class)s_related")
    sex = models.CharField(max_length=1, choices=Patient.SEX_CHOICES)
    relationship = models.CharField(max_length=50)
    family_member_diagnosis = models.CharField(max_length=3, choices=DIAGNOSIS_CHOICES, verbose_name="diagnosis")

    def __unicode__(self):
        return str(self.diagnosis)


class Notes(models.Model):
    diagnosis = models.OneToOneField(Diagnosis)
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
        if kwargs['created']:
            wg = diagnosis.patient.working_group
            recipients = User.objects.filter(working_groups=wg)
            sendNewPatientEmail(recipients)            
    except Exception, e:
        logger.critical(e)
        logger.critical(traceback.format_exc())
        raise


# connect up django signals
post_save.connect(signal_patient_post_save, sender=Patient)
