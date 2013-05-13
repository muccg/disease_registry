from django.conf import settings
from django.core.files.storage import FileSystemStorage

import traceback
import datetime
from django.db import models
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist
#from registry.genetic.models import MolecularData
from registry.patients.models import Patient

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

class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient)

    def __unicode__(self):
        return unicode(self.patient)

    class Meta:
        verbose_name = "Medical History"
        verbose_name_plural = "Medical Histories"

class TreatmentOverview(models.Model):
    patient = models.ForeignKey(Patient)

    def __unicode__(self):
        return unicode(self.patient)

class Treatment(models.Model):
    #overview = models.ForeignKey(TreatmentOverview)
    name = models.CharField(max_length = 100)
    common_name = models.CharField(max_length = 100)

    def __unicode__(self):
        if self.common_name:
            return "%s (%s)" % (self.name, self.common_name)
        else:
            return "%s" % (self.name)

class TreatmentCourse(models.Model):
    treatment = models.ForeignKey(Treatment)
    overview = models.ForeignKey(TreatmentOverview)
    start_date = models.DateField()
    end_date = models.DateField(blank = True, null = True)
    dose_type = models.CharField(max_length=1, blank=True, null=True)
    dose_other = models.TextField(verbose_name='Dose notes')
    notes = models.TextField(blank = True, verbose_name="Notes / Adverse Events")


class Diagnosis(models.Model):

    DD_AFFECTED_STATUS_CHOICES = (
        ('FamilyHistory', 'Not yet diagnosed/Family history only'),
        ('AS2', 'DD Affected Status 2'),
        ('AS3', 'DD Affected Status 3'),
        ('AS4', 'DD Affected Status 4'),
    )
    DD_DIAGNOSIS_CHOICES = (
        ("UNK", "Unknown"),
        ("DD1", "Demyelinating Disease 1"),
        ("DD2", "Demyelinating Disease 2"),
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
    age_at_molecular_diagnosis = models.IntegerField('age in years at molecular diagnosis', null=True, blank=True)

    orphanet = models.ForeignKey(OrphanetChoices, null=True, blank = True)

    family_history = models.TextField(null=True, blank=True)
    family_consent = models.BooleanField(default=False)

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

class DDMedicalHistoryRecord(models.Model):
    diagnosis = models.ForeignKey(Diagnosis, null=True, blank=True)
    history = models.ForeignKey(MedicalHistory, related_name='records')
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

class EdssRating(models.Model):
    rating = models.FloatField()
    name = models.CharField(max_length=300)

    class Meta:
        verbose_name = "EDSS Rating"
        ordering = ['rating',]

    def __unicode__(self):
        return '(%s) %s' % (self.rating, self.name)

class DDClinicalData(models.Model):
    ''' The full text of EDSS ratings. Possibly for use in a pop up widget - dropdown descriptions have been shortened for layout purposes.
    (0.0, "Normal Neurological Exam"),
    (1.0, "No disability, minimal signs on 1 FS"),
    (1.5, "No disability, minimal signs on 2 of 7 FS"),
    (2.0, "Minimal disability in 1 of 7 FS"),
    (2.5, "Minimal disability in 2 FS"),
    (3.0, "Moderate disability in 1 FS; or mild disability in 3 - 4 FS, though fully ambulatory"),
    (3.5, "Fully ambulatory but with moderate disability in 1 FS and mild disability in 1 or 2 FS; or moderate disability in 2 FS; or mild disability in 5 FS"),
    (4.0, "Fully ambulatory without aid, up and about 12hrs a day despite relatively severe disability. Able to walk without aid 500 meters"),
    (4.5, "Fully ambulatory without aid, up and about much of day, able to work a full day, may otherwise have some limitations of full activity or require minimal assistance. Relatively severe disability. Able to walk without aid 300 meters"),
    (5.0, "Ambulatory without aid for about 200 meters. Disability impairs full daily activities"),
    (5.5, "Ambulatory for 100 meters, disability precludes full daily activities"),
    (6.0, "Intermittent or unilateral constant assistance (cane, crutch or brace) required to walk 100 meters with or without resting"),
    (6.5, "Constant bilateral support (cane, crutch or braces) required to walk 20 meters without resting"),
    (7.0, "Unable to walk beyond 5 meters even with aid, essentially restricted to wheelchair, wheels self, transfers alone; active in wheelchair about 12 hours a day"),
    (7.5, "Unable to take more than a few steps, restricted to wheelchair, may need aid to transfer; wheels self, but may require motorized chair for full day's activities"),
    (8.0, "Essentially restricted to bed, chair, or wheelchair, but may be out of bed much of day; retains self care functions, generally effective use of arms"),
    (8.5, "Essentially restricted to bed much of day, some effective use of arms, retains some self care functions"),
    (9.0, "Helpless bed patient, can communicate and eat"),
    (9.5, "Unable to communicate effectively or eat/swallow"),
    (10.0, "Death due to MS")
    '''

    EDSSRatingChoices = ( ('0.0', "Normal Neurological Exam"),
                          ('1.0', "No disability, minimal signs on 1 FS"),
                          ('1.5', "No disability, minimal signs on 2 of 7 FS"),
                          ('2.0', "Minimal disability in 1 of 7 FS"),
                          ('2.5', "Minimal disability in 2 FS"),
                          ('3.0', "Fully amb (mod dblty in 1 FS; or mild dblty in 3-4 FS)"),
                          ('3.5', "Fully amb but with mod/mild disability in several FS"),
                          ('4.0', "Fully amb w/out aid 500m"),
                          ('4.5', "Fully amb w/out aid 300m"),
                          ('5.0', "Amb w/out aid 200m. Impaired activity"),
                          ('5.5', "Amb 100m, daily activities impaired"),
                          ('6.0', "Amb 100m with unilateral assist"),
                          ('6.5', "Amb 20m with bilateral assist"),
                          ('7.0', "Amb <5m w/out wheelchair"),
                          ('7.5', "Wheelchair restricted, mainly self propelled"),
                          ('8.0', "Bed/chair/wheelchair restricted, self care"),
                          ('8.5', "Bed restricted, some arm use/self care"),
                          ('9.0', "Helpless bed patient, can communicate and eat"),
                          ('9.5', "Unable to communicate effectively or eat/swallow"),
                          ('10.0', "Death due to MS")
                        )

    EVALUATION_TYPE_CHOICES = (
        (1, "Formal"),
        (2, "From notes"),
    )

    diagnosis               = models.ForeignKey(Diagnosis)
    date                    = models.DateField(verbose_name = "Clinical Data date")
    date_first_symtoms      = models.DateField(verbose_name = "Date of first symptoms")
    edss_rating             = models.ForeignKey(EdssRating)
    edss_evaluation_type    = models.PositiveSmallIntegerField(choices=EVALUATION_TYPE_CHOICES, verbose_name="Evaluation type")
    past_medical_history    = models.ForeignKey(DDMedicalHistoryRecord, null=True, blank = True)
    date_of_visits          = models.DateField(verbose_name = "Date of visits")

    def __unicode__(self):
        return unicode(self.diagnosis)

    class Meta:
        verbose_name = "Clinical Data"
        verbose_name_plural = "Clinical Data"

class LabData(models.Model):
    diagnosis =         models.ForeignKey(Diagnosis)
    date =              models.DateField()
    protein =           models.FloatField(default = 0.0, verbose_name = "Protein (g/L)")
    leucocytes =        models.FloatField(default = 0.0, verbose_name = "Leucocytes (/ul)")
    erythrocytes =      models.FloatField(default = 0.0, verbose_name = "Erythrocytes (/ul)")
    oligoclonal_bands = models.FloatField(default = 0.0, verbose_name = "Oligoclonal Bands")
    igg_alb =           models.FloatField(default = 0.0, verbose_name = "IgG/Alb")

    class Meta:
        verbose_name = "Lab Data"
        verbose_name_plural = "Lab Data"

    def __unicode__(self):
        return u"%s (%s)" % (self.diagnosis.patient, unicode(self.date))

class MRIData(models.Model):
    diagnosis = models.ForeignKey(Diagnosis)
    date = models.DateField()

    location = models.TextField(verbose_name = "MRI Data Location", blank=True)
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

class DDTreatmentOverview(TreatmentOverview):
    diagnosis = models.ForeignKey(Diagnosis, null=True, blank = True)
    treatments = models.ManyToManyField(Treatment, null=True, blank = True)

    def populate_initial_items(self):
        initial_items = [(u'1FN\u03b20 1a', "Avonex"),
                         (u'1FN\u03b2 1a', "Rebif"),
                         (u'1FN\u03b2 1b', "Betaferon"),
                         (u'Natalizumab', "Tysabri"),
                         (u'Glatiramer Acetate', "Copaxone"),
                         (u'Fingolimod', "Gilenya"),
                         (u'Mitoxantrone', None),
                         (u'Cladribine', None),
                         (u'Cyclophosphamide', None),
                         (u'Oral Steroids', None),
                         (u'Bone Marrow', None),
                         (u'Transplants', None),
                         (u'Rituximab', None),
                         (u'Alemtuzumab', None),
                         ]
        for item in initial_items:
            t, created = Treatment.objects.get_or_create(name = item[0])
            if created and item[1]:
                t.common_name = item[1]
            #t.overview = self
                t.save()

            self.treatments.add(t)

    def save(self, *args, **kwargs):
        created = False
        if not self.pk:
            created = True
        super(DDTreatmentOverview, self).save(*args, **kwargs)
        if created:
            self.populate_initial_items()

    class Meta:
        verbose_name = "Treatment Overview"
        verbose_name_plural = "Treatment Overviews"


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
