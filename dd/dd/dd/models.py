from django.conf import settings
from django.core.files.storage import FileSystemStorage

import traceback
import datetime
from django.db import models
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist
#from registry.genetic.models import MolecularData
from registry.patients.models import Patient
from registry.groups.models import User

from registry.mail import sendNewPatientEmail

import logging
logger = logging.getLogger('registry_log')

file_system = FileSystemStorage(location=settings.MEDIA_ROOT,
                                base_url=settings.MEDIA_URL)
mri_store = file_system

class OrphanetChoices(models.Model):
    code = models.CharField(max_length=6)
    description = models.CharField(max_length=120) # need over 104, otherwise the SQL import fails

    class Meta:
        verbose_name = "Orphanet Code"
        ordering = ["code"] # doesn't seem to work on subclasses

    def __unicode__(self):
        return "%s - %s" % (self.code, self.description) # used in the select options

class MedicalHistoryDisease(models.Model):
    disease = models.CharField(max_length = 100)

    def __unicode__(self):
        return '%s' % (self.disease,)

    class Meta:
        verbose_name = "Medical History Disease"
        verbose_name_plural = "Medical History Diseases"
        ordering = ['disease']

class Treatment(models.Model):
    name = models.CharField(max_length = 100)
    common_name = models.CharField(max_length=100, blank=True,
                                   help_text="Leave blank if same as <em>Name</em>")

    def __unicode__(self):
        if self.common_name:
            return "%s (%s)" % (self.name, self.common_name)
        else:
            return "%s" % (self.name)

class TreatmentCourse(models.Model):
    DOSE_TYPE_CHOICES = [
        ('S','Standard'),
        ('O','Other')
        ]

    treatment = models.ForeignKey(Treatment)
    diagnosis = models.ForeignKey("Diagnosis")
    start_date = models.DateField()
    end_date = models.DateField(blank = True, null = True)
    dose_type = models.CharField(max_length=1, choices=DOSE_TYPE_CHOICES,
                                 default='S')
    dose_other = models.TextField(verbose_name='Dose notes')
    notes = models.TextField(blank = True, verbose_name="Notes / Adverse Events")

    def __unicode__(self):
        return "%s/%s" % (unicode(self.diagnosis), unicode(self.treatment))

class Diagnosis(models.Model):

    DD_AFFECTED_STATUS_CHOICES = (
        ('FamilyHistory', 'Not yet diagnosed/Family history only'),
        ('AS2', 'DD Affected Status 2'),
        ('AS3', 'DD Affected Status 3'),
        ('AS4', 'DD Affected Status 4'),
    )

    DD_DIAGNOSIS_CHOICES = (
        ('CIS', 'Clinically isolated syndrome'),
        ('RR',  'Relapsing remitting'),
        ('SP',  'Secondary progressive'),
        ('PP',  'Primary progressive'),
        ('PR',  'Progressive relapsing'),
    )

    DD_FIRST_SUSPECTED_CHOICES = (
        ("NA", "Not Applicable"), # Trac 16 #61
        ("Self", "Self"),
        ("Family", "Family"),
        ("GP", "GP"),
        ("Paediatrician", "Paediatrician"),
        ("Neurologist", "Neurologist"),
        ("Cardiologist", "Cardiologist"),
        ("Ophthalmologist", "Ophthalmologist"),
        ("Geneticist", "Geneticist"),
        ("Other", "Other"),
    )
    patient = models.OneToOneField(Patient, primary_key=True, related_name='patient_diagnosis')
    diagnosis = models.CharField(max_length=3, choices = DD_DIAGNOSIS_CHOICES, verbose_name = "Condition", default = 'UNK')
    affected_status = models.CharField(max_length=30, choices=DD_AFFECTED_STATUS_CHOICES, verbose_name = "Affected Status", default = '')

    first_suspected_by = models.CharField(max_length=50, choices = DD_FIRST_SUSPECTED_CHOICES, null=True, blank=True)
    date_of_first_symptom = models.DateField(null=True, blank=True)
    date_of_diagnosis = models.DateField(null=True, blank=True)

    age_at_clinical_diagnosis = models.IntegerField('age in years at clinical diagnosis', null=True, blank=True)

    orphanet = models.ForeignKey(OrphanetChoices, null=True, blank = True)

    family_history = models.TextField(null=True, blank=True)
    family_consent = models.BooleanField(default=False)

    treatments = models.ManyToManyField(Treatment, through=TreatmentCourse)

    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)

    def __unicode__(self):
        return unicode(self.patient)

    class Meta:
        verbose_name = "Demyelinating Disease Diagnosis"
        verbose_name_plural = "Demyelinating Disease Diagnoses"

    def save(self, *args, **kwargs):
        '''On save, update timestamps, auto-fields reportedly unreliable'''
        if not self.created:
            self.created = datetime.datetime.now()
        self.updated = datetime.datetime.now()
        super(Diagnosis, self).save(*args, **kwargs)

    def percentage_complete(self):
        score = 0.0
        fieldlist = ['affected_status']
        for f in fieldlist:
            try:
                getattr(self, f)
                score += 1.0
            except ObjectDoesNotExist, e:
                pass
        return  int(score / len(fieldlist) * 100.0)

    def incomplete_sections(self):
        fieldlist = ['affected_status']
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

class MedicalHistory(models.Model):
    diagnosis = models.ForeignKey(Diagnosis, related_name="medical_history")
    date = models.DateField()

    disease = models.ForeignKey(MedicalHistoryDisease)
    chronic = models.BooleanField(default = False, verbose_name = "Chronic / incurable")
    medical_history_file = models.FileField(upload_to='medical_history', storage=file_system, verbose_name="Document")
#    medical_history = models.ForeignKey(MedicalHistory)
#    diabetes                     = models.BooleanField(default = False, verbose_name="Diabetes")
#    diabetes_insulin             = models.BooleanField(default = False, verbose_name="If yes, do you use insulin?")
#    diabetes_onset_age           = models.IntegerField(default = 1,     verbose_name = "Age of onset")
#    rheumatoid_arthritis         = models.BooleanField(default = False, verbose_name = "Rheumatoid Arthritis")
#    crohns_disease               = models.BooleanField(default = False, verbose_name = "Crohn's Disease")
#    ulcerative_colitis           = models.BooleanField(default = False, verbose_name = "Ulcerative Colitis")
#    psoriasis                    = models.BooleanField(default = False, verbose_name = "Psoriasis")
#    myasthenia_gravis            = models.BooleanField(default = False, verbose_name = "Myasthenia Gravis")
#    vitiligo                     = models.BooleanField(default = False, verbose_name = "Vitiligo")
#    thyroid_disease              = models.BooleanField(default = False, verbose_name = "Thyroid Disease")
#    thyroid_hypothyroidism       = models.BooleanField(default = False, verbose_name = "Hypothyroidism")
#    thyroid_hashimotos           = models.BooleanField(default = False, verbose_name = "Hashimoto's Thyroiditis")
#    graves_disease               = models.BooleanField(default = False, verbose_name = "Graves' Disease")
#    sjogrens_syndrome            = models.BooleanField(default = False, verbose_name = "Sjorgens Syndrome")
#    pernicious_anemia            = models.BooleanField(default = False, verbose_name = "Pernicious Anemia")
#    systemic_lupus_erythematosus = models.BooleanField(default = False, verbose_name = "Systemic Lupus Erythematosus")
#    alopecia                     = models.BooleanField(default = False, verbose_name = "Alopecia")
#    family_history_of_ms         = models.BooleanField(default = False, verbose_name = "Family history of MS, NMO (or other autoimmune disease)")
    other = models.TextField(verbose_name="Other", blank=True)
    misdiagnosed = models.BooleanField(blank=True, default=False)

    class Meta:
        verbose_name = "Medical History Record"
        verbose_name_plural = "Medical History Records"

    def __unicode__(self):
        return unicode(self.diagnosis)


class DDClinicalData(models.Model):

    EVALUATION_TYPE_CHOICES = (
        (1, "Formal"),
        (2, "From notes"),
    )

    VISUAL_CHOICES = (
        (0, 'Normal'),
        (1, 'Disc pallor and/or mild scotoma and/or visual acuity of worse eye (corrected) less than 30/30 (1.0) but better than 20/30 (0.67)'),
        (2, 'Worse eye with large scotoma and/or maximal visual acuity (corrected) of 20/30 to 20/59 (0.67-0.34)'),
        (3, 'Worse eye with large scotoma or moderate decrease in fields and/or maximal visual acuity (corrected) of 20/60 to 20/99 (0.33-0.2)'),
        (4, 'Worse eye with marked decrease of fields and/or maximal visual acuity (corrected) of 20/100 to 20/200 (0.1-0.2); grade 3 plus maximal acuity of better eye of 20/60 (0.3) or less'),
        (5, 'Worse eye with maximal visual acuity (corrected) less than 20/200 (0.1); grade 4 plus maximal acuity of better eye of 20/60 (0.3) or less'),
        (6, 'Grade 5 plus maximal visual acuity of better eye of 20/60 (0.3) or less'))

    BRAINSTEM_CHOICES = (
        (0, 'Normal'),
        (1, 'Signs only'),
        (2, 'Moderate nystagmus; other mild disability'),
        (3, 'Severe nystagmus; marked extraocular weakness; moderate disability of other cranial nerves'),
        (4, 'Marked dysarthria; other marked disability'),
        (5, 'Inability to swallow or speak'))

    PYRAMIDAL_CHOICES = (
        (0, 'Normal'),
        (1, 'Abnormal signs without disability'),
        (2, 'Minimal disability, patient complains about fatiguability in motor tasks and/or BMRC grade 4 in one or two muscle groups'),
        (3, 'Mild to moderate paraparesis or hemiparesis, full range of mevement against gravity; severe monoparesis, refers to BMRC grade 2 or less in one muscle group'),
        (4, 'marked paraparesis or hemiparesis; moderate tetraparesis (refers to BMRC grade 3); monoplegia'),
        (5, 'Paraplegia, grade 0 or 1 in all muscle groups of the lower limbs, hemiplegia, marked tetraparesis (BMRC grade 2 or less)'),
        (6, 'Tetraplegia (grade 0 or 1 in all muscle groups of upper and lower limbs)'))

    CEREBELLAR_CHOICES = (
        (0, 'Normal'),
        (1, 'Abnormal signs without disability'),
        (2, 'Mild ataxia'),
        (3, 'Moderate truncal ataxia; moderate limb ataxia'),
        (4, 'Severe ataxia in all limbs or trunk'),
        (5, 'Unable to perform coordinated movements due to ataxia'))

    SENSORY_CHOICES = (
        (0, 'Normal'),
        (1, 'Mild vibration or figure-writing decrease only in 1 or 2 limbs'),
        (2, 'Mild decrease in touch or pain or position sense and/or moderate decrease in vibration in 1 or 2 limbs; vibration or figure-writing decrease, alone or in 3 or 4 limbs'),
        (3, 'Moderate decrease in touch or pain or position sense and/or essentially lost vibration in 1 or 2 limbs; mild decrease in touch or pain and/or moderated decrease in all proprioceptive tests in 3 or 4 limbs'),
        (4, 'Marked decrease in touch or pain or loss of proprioception, alone or combined in 1 or 2 limbs; moderate decrease in touch or pain and/or severe proprioceptive decrease in more than 2 limbs'),
        (5, 'Loss (essentially) of sensation in 1 or 2 limbs; moderate decrease in touch or pain and/or loss or proprioception for most of the body below the head'),
        (6, 'Sensation essentially lost below the head'))

    BOWEL_BLADDER_CHOICES = (
        (0, 'Normal'),
        (1, 'Mild urinary hesitancy, urgency and/or constipation'),
        (2, 'Moderate urinary hesitancy and/or urgency and/or rare incontinence and/or severe constipation'),
        (3, 'Frequent urinary incontinence or intermittent self catheterisation once or twice a day, needs constantly enemata or manual measures to evacuate bowel'),
        (4, 'In need of almost constant catheterisation, intermittent self-catheterisation more than twice a day'),
        (5, 'Loss of bladder function, external or indwelling catheter'),
        (6, 'Loss of bowel and bladder function'))

    CEREBRAL_MENTAL_CHOICES = (
        (0,'Normal'),
        (1, 'Mood alteration only (does not affect EDSS score)'),
        (2, 'Mild decrease in mentation/fatigue'),
        (3, 'Moderate decrease in mentation'),
        (4, 'Marked decrease in mentation'),
        (5, 'Dementia'))

    AMBULATION_CHOICES = (
        (0, 'Fully ambulatory'),
        (1, 'About 500 metres without aid or rest'),
        (2,'About 300 metres without aid or rest'),
        (3, 'About 200 metres without aid or rest'),
        (4, 'About 100 metres without aid or rest'),
        (5, 'About 100 metres with unilateral assistance'),
        (6, 'About 20 metres with bilateral assistance'),
        (7, 'Essentially restricted to wheelchair (wheels self)'),
        (8, 'Restricted to wheelchair (may need help in transfer)'),
        (9, 'Essentially restricted to bed or chair'),
        (10, 'Restricted to bed much of the day'),
        (11, 'Bed patient, can communicate and eat'),
        (12, 'Helpless bed patient, unable to communicate, eat or swallow'))

    diagnosis               = models.ForeignKey(Diagnosis)
    date                    = models.DateField(verbose_name = "Clinical Data date")
    date_first_symtoms      = models.DateField(verbose_name = "Date of first symptoms")

    edss_visual             = models.PositiveSmallIntegerField(choices=VISUAL_CHOICES, verbose_name='Visual', default=0)
    edss_brainstem          = models.PositiveSmallIntegerField(choices=BRAINSTEM_CHOICES, verbose_name='Brainstem', default=0)
    edss_pyramidal          = models.PositiveSmallIntegerField(choices=PYRAMIDAL_CHOICES, verbose_name='Pyramidal', default=0)
    edss_cerebellar         = models.PositiveSmallIntegerField(choices=CEREBELLAR_CHOICES, verbose_name='Cerebellar', default=0)
    edss_sensory            = models.PositiveSmallIntegerField(choices=SENSORY_CHOICES, verbose_name='Sensory', default=0)
    edss_bowel_bladder      = models.PositiveSmallIntegerField(choices=BOWEL_BLADDER_CHOICES, verbose_name="Bowel/Bladder", default=0)
    edss_cerebral_mental    = models.PositiveSmallIntegerField(choices=CEREBRAL_MENTAL_CHOICES, verbose_name="Cerebral (Mental)", default=0)
    edss_ambulation         = models.PositiveSmallIntegerField(choices=AMBULATION_CHOICES, verbose_name="Ambulation", default=0)

    edss_evaluation_type    = models.PositiveSmallIntegerField(choices=EVALUATION_TYPE_CHOICES, verbose_name="Evaluation type")
    edss_form               = models.FileField(upload_to='edss_form', storage=file_system, verbose_name="EDSS Form")
    date_of_visits          = models.DateField(verbose_name = "Date of visits")

    @property
    def edss_score(self):
        return 'TODO'

    def __unicode__(self):
        return unicode(self.diagnosis)

    class Meta:
        verbose_name = "Clinical Data"
        verbose_name_plural = "Clinical Data"

class LabData(models.Model):
    PLUS_MINUS_CHOICES = (
        ('+', '+'),
        ('-', '-')
    )
    
    diagnosis =         models.ForeignKey(Diagnosis)
    date =              models.DateField()
    protein =           models.CharField(max_length=1, choices=PLUS_MINUS_CHOICES, verbose_name = "Protein (g/L)")
    leucocytes =        models.CharField(max_length=1, choices=PLUS_MINUS_CHOICES, verbose_name = "Leucocytes (/ul)")
    erythrocytes =      models.CharField(max_length=1, choices=PLUS_MINUS_CHOICES, verbose_name = "Erythrocytes (/ul)")
    oligoclonal_bands = models.CharField(max_length=1, choices=PLUS_MINUS_CHOICES, verbose_name = "Oligoclonal Bands")
    igg_alb =           models.CharField(max_length=1, choices=PLUS_MINUS_CHOICES, verbose_name = "IgG/Alb")

    class Meta:
        verbose_name = "Lab Data"
        verbose_name_plural = "Lab Data"

    def __unicode__(self):
        return u"%s (%s)" % (self.diagnosis.patient, unicode(self.date))

class MRIData(models.Model):
    diagnosis = models.ForeignKey(Diagnosis)
    date = models.DateField()

    location = models.TextField(blank=True, verbose_name="MRI Data Location",
                                help_text="Fill in this field if " +
                                "MRI image file(s) can't be uploaded.")
    brain = models.BooleanField(default = False, verbose_name = "Brain")
    cervical = models.BooleanField(default = False, verbose_name = "Cervical")
    thoracic = models.BooleanField(default = False, verbose_name = "Thoracic")
    report_file = models.FileField(upload_to='mri_reports', storage=file_system, verbose_name="Report")

    class Meta:
        verbose_name = "MRI Data"
        verbose_name_plural = "MRI Data"

    def __unicode__(self):
        return unicode(self.diagnosis)


class MRIFile(models.Model):
    data = models.ForeignKey(MRIData, related_name="images")
    image = models.FileField(upload_to='mri_images', storage=mri_store,
                             verbose_name="MRI Image File")


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
    wg = diagnosis.patient.working_group
    recipients = User.objects.filter(working_groups=wg)
    sendNewPatientEmail(recipients)

# connect up django signals
post_save.connect(signal_patient_post_save, sender=Patient)
post_save.connect(signal_diagnosis_post_save, sender=Diagnosis)