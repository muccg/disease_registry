# vim: set fileencoding=UTF-8:
from __future__ import division
from django.db import models

from registry.patients.models import Patient

# Base abstract models for fields common to the registry proper and
# questionnaire.

class Diagnosis(models.Model):
    # Trac 16 #12 Now assigning numbers instead of lengthy strings. The database is not really in production yet, so we can change that
    FIRST_SYMPTOM_CHOICES = (
        ("1", "Prenatal - polyhydramnios and reduced fetal movements"),
        ("2", "Feeding difficulties requiring tube at or near term"),
        ("3", "Hypotonia"),
        ("4", "Learning difficulties"),
        ("5", "Delayed development"),
        ("6", "Myotonia"),
        ("7", "Muscle weakness"),
        ("8", "Bilateral cataracts"),
        ("9", "Cardiac symptoms"),
        ("10", "Anaesthetic problems"),
        ("11", "Patient is the mother of a child with congenital facioscapulohumeral muscular dystrophy"),
        ("12", "Patient asymptomatic"),
        ("13", "Diagnosis of a family member with Myotonic dystrophy"),
        ("14", "Other"))

    FIRST_SUSPECTED_CHOICES = (
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

    AFFECTED_STATUS_CHOICES = (
        ('FamilyHistory','Not yet diagnosed/Family history only'),
        ('AsymptomaticCarrier','Asymptomatic Carrier'),
        ('Congenital','Congenital Facioscapulohumeral Muscular Dystrophy'),
        ('Juvenile','Juvenile Facioscapulohumeral Muscular Dystrophy'),
        ('Adult','Adult Facioscapulohumeral Muscular Dystrophy'),
    )

    DIAGNOSIS_CHOICES = (
        ("FSHD", "FSHD"),
        ("DM2", "DM2"),
        ("O", "Other"),
    )
    # moved up to base.py since the question is now in registry & questionnaire
    # Need the "default='FSHD'" to remove the '----' option, see Django admin
    # /home/username/registry/virt_registry/lib/python2.6/site-packages/Mango_py-1.2.3-py2.6.egg/django/db/models/fields/__init__.py
    diagnosis = models.CharField(max_length=3, choices=DIAGNOSIS_CHOICES, verbose_name='Condition', default='FSHD') # required

    #affectedstatus = models.CharField(max_length=30, choices=AFFECTED_STATUS_CHOICES, verbose_name='Affected Status') # required
    affectedstatus = models.CharField(max_length=30, choices=AFFECTED_STATUS_CHOICES, verbose_name='Affected Status', default='') # required, default to remove the '---' in the options
    first_symptom = models.CharField('What was the first symptom that prompted the diagnosis of Facioscapulohumeral Muscular Dystrophy', max_length=50, choices=FIRST_SYMPTOM_CHOICES, null=True, blank=True)
    first_suspected_by = models.CharField(max_length=50, choices=FIRST_SUSPECTED_CHOICES, null=True, blank=True)

    age_at_clinical_diagnosis = models.IntegerField('age in years at clinical diagnosis', null=True, blank=True)
    age_at_molecular_diagnosis = models.IntegerField('age in years at molecular diagnosis', null=True, blank=True)

    class Meta:
        abstract = True


class MotorFunction(models.Model):
    DYSARTHRIA_CHOICES = (
        (0, "No dysarthria"),
        (1, "Slightly slurred speech"),
        (2, "Some problems being understood"),
        (3, "Significant speech problems"),
    )

    MOTOR_FUNCTION_CHOICES = (
        ("walking", "Walking independently"),
        ("assisted", "Walking assisted"),
        ("nonamb", "Non-ambulatory"), # added v3
        #("sitting", "Sitting independently"), # removed v3
        #("none", "Never able to walk or sit independently") # removed v3
    )

    YN_CHOICES = (('N', 'No'), ('Y', 'Yes'))

    WALK_ASSISTED_CHOICES = (
        ("No device", "No device required"), # Trac 16 #49
        ("Ankle support", "Ankle support"),
        ("Stick", "Stick"),
        ("Walker", "Walker"),
    )

    WHEELCHAIR_USE_CHOICES = (
        ("never", "Never"),
        ("intermittent", "Yes (Intermittent)"),
        ("permanent", "Yes (Permanent)"),
        ("unknown", "Unknown")
    )

    # could not make the BooleanField required
    #walk = models.BooleanField(verbose_name="currently able to walk", null=False, blank=False) # Trac 16 Item 48, removed help text #required
    walk = models.CharField(max_length=1, choices=YN_CHOICES, verbose_name="currently able to walk", default='') #required
    walk_assisted = models.CharField(max_length=50, choices=WALK_ASSISTED_CHOICES, verbose_name="current use of devices to assist with walking", default='') #required
    walk_assisted_age = models.IntegerField(verbose_name="at what age did the patient commence using devices to assist with walking", null=True, blank=True, help_text="age in years")
    # removed v3
    #sit = models.BooleanField(verbose_name="currently able to sit without support", help_text="Able to maintain a sitting position on a chair or a wheelchair without support of upper limbs or leaning against the back of the chair")
    # Trac #33
    best_function = models.CharField(choices=MOTOR_FUNCTION_CHOICES, default='', null=True, blank=True, max_length=8, verbose_name="What is the best motor function level the patient has achieved", help_text="[Motor functions are listed in order with higher functions at the top, please choose one]<br/>Walking: walking with or without help (orthoses or assistive device or human assistance), inside or outdoors")
    #removed v3
    #acquisition_age = models.IntegerField(verbose_name="At what age did the patient start walking", null=True, blank=True, help_text="Indicate age in years when the patient started walking")
    wheelchair_use = models.CharField(verbose_name="wheel chair use", default='', max_length=12, choices=WHEELCHAIR_USE_CHOICES, help_text="<b>Yes (permanent):</b> patient is not able to walk and needs a wheelchair to move<br/><b>Yes (intermittent):</b> patient is still able to walk") #required
    wheelchair_usage_age = models.IntegerField(null=True, blank=True, help_text="If using wheelchair specify age at start of wheelchair use") # required but need to check Yes previous question
    dysarthria = models.IntegerField(choices=DYSARTHRIA_CHOICES,null=True, blank=True, default=0)

    class Meta:
        abstract = True


class Surgery(models.Model):
    CARDIAC_IMPLANT_CHOICES = (
        ("no", "No"),
        ("pacemaker", "Pacemaker"),
        ("icd", "Implantable cardioverter defibrillator"),
        ("yes", "Yes, not specified further"),
    )

    UYN_CHOICES = (
        ('U', 'Unknown'),
        ('Y', 'Yes'),
        ('N', 'No'),
    )

    #cardiac_implant = models.NullBooleanField(verbose_name="cardiac implant", help_text="Have you had an operation to implant a device to control/normalise your heart rhythm?")
    # Trac #34
    cardiac_implant = models.CharField(verbose_name="Cardiac implant", blank=True, null=True, max_length=30, choices=CARDIAC_IMPLANT_CHOICES, help_text="Have you had an operation to implant a device to control/normalise your heart rhythm?")
    cardiac_implant_age = models.IntegerField(verbose_name="age cardiac implant received", null=True, blank=True, help_text="Age at which cardiac implant received")
    cataract_diagnosis = models.BooleanField()
    #cataract = models.NullBooleanField(verbose_name="cataract surgery")
    # Trac #34
    cataract = models.CharField(max_length=1, choices=UYN_CHOICES, verbose_name="Cataract surgery", null=True, blank=True)

    cataract_age = models.IntegerField(verbose_name="age at cataract surgery", null=True, blank=True, help_text="Age at which cataract surgery was performed")

    class Meta:
        abstract = True


class Heart(models.Model):
    HEART_CHOICES = (
        ("yes", "Yes, not specified further"),
        ("arrhythmia", "Yes, with arrhythmia or conduction block"),
        ("cardiomyopathy", "Yes, with cardiomyopathy"),
        ("no", "No"),
        ("unknown", "Unknown")
    )

    UYN_CHOICES = (
        ('U', 'Unknown'),
        ('Y', 'Yes'),
        ('N', 'No'),
    )

    YN_CHOICES = (('N', 'No'), ('Y', 'Yes'))

    condition = models.CharField(verbose_name="heart condition", max_length=14, choices=HEART_CHOICES, null=True, blank=True)
    age_at_diagnosis = models.IntegerField(verbose_name="At what age was the patient diagnosed with a heart condition", null=True, blank=True)

    # added according to the questionnaire
    racing = models.CharField(verbose_name="Does the patient experience: heart racing or beating irregularly", choices=UYN_CHOICES, max_length=1, null=True, blank=True)
    palpitations = models.CharField(verbose_name="heart palpitations", choices=UYN_CHOICES, max_length=1, null=True, blank=True)
    fainting = models.CharField(verbose_name="black-outs or fainting", choices=UYN_CHOICES, max_length=1, null=True, blank=True)

    # ecg
    #ecg = models.NullBooleanField(verbose_name="ECG")
    ecg = models.CharField(max_length=1, choices=UYN_CHOICES, verbose_name="ECG", null=True, blank=True)
    #ecg_sinus_rhythm = models.NullBooleanField(verbose_name="ECG Sinus Rhythm", null=True, blank=True)
    ecg_sinus_rhythm = models.CharField(max_length=1, choices=UYN_CHOICES, verbose_name="ECG Sinus Rhythm", null=True, blank=True)
    ecg_pr_interval = models.IntegerField(verbose_name="ECG PR interval", null=True, blank=True, help_text="PR Interval measured in milliseconds")
    ecg_qrs_duration = models.IntegerField(verbose_name="ECG QRS duration", null=True, blank=True, help_text="QRS Duration measured in milliseconds")
    ecg_examination_date = models.DateField(null=True, blank=True, verbose_name="ECG Examination Date")

    # echocardiogram
    #echocardiogram = models.NullBooleanField()
    echocardiogram = models.CharField(max_length=1, choices=UYN_CHOICES, null=True, blank=True)

    echocardiogram_lvef = models.IntegerField(null=True, blank=True, verbose_name="LVEF score", help_text="Left Ventricular Ejection Fraction (LVEF) determined by ultrasound examination of the heart; expressed in % [%=(End disatolic volume - End systolic volume) ÷ End diastolic volume] to specify last LVEF(%) and date of examination")
    echocardiogram_lvef_date = models.DateField(null=True, blank=True, verbose_name="LVEF date")

    class Meta:
        abstract = True


class HeartMedication(models.Model):
    STATUS_CHOICES = (
        ("Current", "Current prescription"),
        ("Previous", "Previous prescription"),
    )

    drug = models.CharField(max_length=100, help_text="Specify each drug with its International Nonproprietary Name (INN)")
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)

    class Meta:
        abstract = True


class Respiratory(models.Model):
    VENTILATION_CHOICES = (
        ("N", "No"),
        ("PT", "Yes (night only)"), # was "part-time"
        ("Y", "Yes (day and night)"),
    )

    VENTILATION_TYPE_CHOICES = (
        ("CPAP", "Continuous Positive Airway Pressure (CPAP)"),
        ("BIPAP", "Bi-level Positive Airway Pressure (BIPAP)"),
    )

    non_invasive_ventilation = models.CharField(max_length=2, null=True, blank=True, choices=VENTILATION_CHOICES, help_text="Mechanical ventilation with nasal or bucal mask")
    age_non_invasive_ventilation = models.IntegerField(null=True, blank=True, verbose_name="age ventilation device use commenced", help_text="Age at which non invasive ventilation device use started (leave blank if no ventilation device is in use)")
    non_invasive_ventilation_type = models.CharField(max_length=5, null=True, blank=True, choices=VENTILATION_TYPE_CHOICES)
    invasive_ventilation = models.CharField(max_length=2, null=True, blank=True, choices=VENTILATION_CHOICES, help_text="Mechanical ventilation with tracheostomy")
    fvc = models.DecimalField(null=True,max_digits=5, decimal_places=2, blank=True, verbose_name="Measured FVC", help_text="Using spirometer measures of total volume of air exhaled from a full lung (total lung capacity) to an empty lung (residual volume).")
    fvc_date = models.DateField(null=True, blank=True, verbose_name="Date of last spirometer reading of FVC")
    calculatedfvc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Calculated FVC")

    # adding this field, cannot figure out how to have a calculated field on the form without storing it in the DB
    # if editable=flase, the field is not made readonly, it is NOT displayed in the admin UI AT ALL
    #predictedfvc = models.DecimalField(verbose_name='Predicted FVC', help_text='forced vital capacity (FVC, expressed as % of normal, predicted by height, age and sex according to NHANES III formulae for Caucasians).', max_digits=5, decimal_places=2, null=True, blank=True) #, editable=False)

    '''
    # could not get that to display in the forms
    @property
    def predictedfvc(self):
        print "predictedfvc property"
        fvc = 92.3 # test
        return fvc
    '''

    class Meta:
        abstract = True


class Muscle(models.Model):
    MYOTONIA_CHOICES = (('S', 'Yes, severely'), ('M', 'Yes, mildly'), ('N', 'No'))
    YN_CHOICES = (('N', 'No'), ('Y', 'Yes'))

    myotonia = models.CharField(max_length=6, blank=True, null=True, choices=MYOTONIA_CHOICES, verbose_name="Does myotonia currently have a negative effect on the patient’s daily activities")

    class Meta:
        abstract = True


class MuscleMedication(models.Model):
    STATUS_CHOICES = (
        ("Current", "Current prescription"),
        ("Previous", "Previous prescription"),
    )

    drug = models.CharField(max_length=100, help_text="Specify each drug with its International Nonproprietary Name (INN)")
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)

    class Meta:
        abstract = True


class FeedingFunction(models.Model):
    UYN_CHOICES = (
        ('U', 'Unknown'),
        ('Y', 'Yes'),
        ('N', 'No'),
    )

    #dysphagia = models.NullBooleanField(help_text="Does the patient have difficulty swallowing?")
    dysphagia = models.CharField(max_length=1, choices=UYN_CHOICES, null=True, blank=True, help_text="Does the patient have difficulty swallowing?")

    #gastric_nasal_tube = models.NullBooleanField(verbose_name="gastric/nasal tube", help_text="Does the patient need nutritional supplementation via nasogastric or nasojejunal tube, or gastrostomy?")
    gastric_nasal_tube = models.CharField(max_length=1, choices=UYN_CHOICES, null=True, blank=True, help_text="Does the patient need nutritional supplementation via nasogastric or nasojejunal tube, or gastrostomy?")

    class Meta:
        abstract = True


class Fatigue(models.Model):
    # need to be integers, since there is a calculation done in the form: 'score'
    DOZING_CHOICES = (
        (0, "Would never doze"),
        (1, "Slight chance of dozing"),
        (2, "Moderate chance of dozing"),
        (3, "High chance of dozing"),
    )

    YN_CHOICES = (('N', 'No'), ('Y', 'Yes'))

    FATIGUE_CHOICES = (('S', 'Yes, severely'), ('M', 'Yes, mildly'), ('N', 'No'))

    fatigue = models.CharField(null=True, blank=True, choices=FATIGUE_CHOICES, max_length=1, help_text="Does fatigue or daytime sleepiness currently have a negative effect on the patient’s normal daily activities?")

    # Trac 16 FSHD Questionnaire #46
    # We just want the label text, not the field as a general caption for the fields that follow
    #hereonlyforcaption = forms.CharField(label="Do you start to fall asleep in the following situations")
    #hereonlyforcaption = models.CharField(max_length=1, null=True, blank=True, help_text="Does the patient start to fall asleep in the following situations")

    #def _get_hereonlyforcaption(self):
    #    return "Y"
    #hereonlyforcaption = property(_get_hereonlyforcaption)

    sitting_reading = models.IntegerField(verbose_name="sitting and reading", choices=DOZING_CHOICES, null=True, blank=True)
    watching_tv = models.IntegerField(verbose_name="watching TV", choices=DOZING_CHOICES, null=True, blank=True)
    sitting_inactive_public = models.IntegerField(verbose_name="sitting, inactive, in a public place", choices=DOZING_CHOICES, help_text="For example, at a theatre or in a meeting", null=True, blank=True)
    passenger_car = models.IntegerField(verbose_name="as a passenger in a car for an hour without a break", choices=DOZING_CHOICES, null=True, blank=True)
    lying_down_afternoon = models.IntegerField(verbose_name="lying down to rest in the afternoon when circumstances permit", choices=DOZING_CHOICES, null=True, blank=True)
    sitting_talking = models.IntegerField(verbose_name="sitting and talking to someone", choices=DOZING_CHOICES, null=True, blank=True)
    sitting_quietly_lunch = models.IntegerField(verbose_name="sitting quietly after lunch without alcohol", choices=DOZING_CHOICES, null=True, blank=True)
    in_car = models.IntegerField(verbose_name="in a car, while stopped for a few minutes in traffic", choices=DOZING_CHOICES, null=True, blank=True)

    class Meta:
        abstract = True

    def score(self):
        return self.sitting_reading + self.watching_tv + self.sitting_inactive_public + self.passenger_car + self.lying_down_afternoon + self.sitting_talking + self.sitting_quietly_lunch + self.in_car


class FatigueMedication(models.Model):
    STATUS_CHOICES = (
        ("Current", "Current prescription"),
        ("Previous", "Previous prescription"),
    )

    drug = models.CharField(max_length=100, help_text="Specify each drug with its International Nonproprietary Name (INN)")
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)

    class Meta:
        abstract = True


class SocioeconomicFactors(models.Model):
    EDUCATION_CHOICES = (
        ("Special", "Special education"),
        ("NoSecondary", "Not completed secondary school"),
        ("Secondary", "Completed secondary school"),
        ("HSC", "High School Certificate or equivalent"),
        ("Trade", "Trade or college of advanced vocational education (including TAFE)"),
        ("Tertiary", "Tertiary education (including university)"),
        ("Postgrad", "Post-graduate qualifications"),
    )

    EFFECT_CHOICES = (
        ("Yes", "Yes, has resulted in unemployment"),
        ("Limited", "Yes, has limited employment choices"),
        ("No", "No"),
        ("Uncertain", "Uncertain"),
    )

    OCCUPATION_CHOICES = (
        ("Employed", "Employed"),
        ("Homemaker", "Homemaker"),
        ("Student", "Student"),
        ("Retired", "Retired"),
        ("Disabled", "Disabled"),
        ("Unemployed", "Unemployed — not due to disablement"),
    )

    education = models.CharField(max_length=30, choices=EDUCATION_CHOICES, null=True, blank=True)
    occupation = models.CharField(max_length=30, choices=OCCUPATION_CHOICES, null=True, blank=True)
    employment_effect = models.CharField(max_length=30, choices=EFFECT_CHOICES, verbose_name="has Myotonic dystrophy affected the patient's employment", null=True, blank=True)
    comments = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        abstract = True

# Trac #35
# replaces the CANCER_TYPE_CHOICES tuples, now in the DB
class CancerTypeChoices(models.Model):
    description = models.CharField(max_length=50, verbose_name='Cancer Type Choice')

    class Meta:
        ordering = ['description']
        verbose_name_plural = "Cancer Types"

    def __unicode__(self):
        return "%s" % self.description

class GeneralMedicalFactors(models.Model):
    YESNO_CHOICES = ( ('N', 'No'), ('Y','Yes') ) # need to keep the values in sync with UYN_CHOICES
    UYN_CHOICES = ( ('U', 'Unknown'), ('N', 'No'), ('Y','Yes') )
    YESNOUNSURE_CHOICES = ( ('0','No'), ('1','Yes'), ('2', 'Unsure') )

    COGNITIVE_CHOICES = (
        ("No", "No"),
        ("Minor", "Minor"),
        ("Marked", "Marked"),
    )

    DIABETES_CHOICES = (
        ('No', 'Not diagnosed'),
        ('SugarIntolerance', 'Has sugar intolerance but not diabetes'),
        ('Type1', 'Yes, Type 1 Diabetes'),
        ('Type2', 'Yes, Type 2 Diabetes'),
    )

    # Trac #35
    # Now in the db with CancerType Choices
    # reverted to choices, until South migration is fixed
    CANCER_TYPE_CHOICES = (
        ('Basal', 'Basal cell carcinomas'),
        ('Insulinomas', 'Insulinomas'),
        ('Parathyroid', 'Parathyroid tumours'),
        ('Pilomatricomas', 'Pilomatricomas'),
        ('Saliverygland', 'Salivery gland tumours'),
        ('Thymomas', 'Thymomas'),
        ('Thyroid', 'Thyroid tumours'),
    )

    #diabetes = models.IntegerField(null=True, blank=True, help_text="Age at onset (leave blank if you do not suffer from diabetes)")
    diabetes = models.CharField(max_length=30, choices=DIABETES_CHOICES, null=True, blank=True)
    diabetesage = models.IntegerField(null=True, blank=True, help_text="Leave blank if you do not suffer from diabetes", verbose_name='Age at diagnosis')

    pneumonia = models.CharField(max_length=3, choices=YESNO_CHOICES, verbose_name="pneumonia", null=True, blank=True)
    pneumoniaage = models.IntegerField(null=True, blank=True, verbose_name="pneumonia age", help_text="Age of first episode (leave blank if you have never suffered from pneumonia)")
    pneumoniainfections = models.CharField(max_length=3, null=True, blank=True, verbose_name="Number of Chest infections in the last 12 months")

    # TODO: make sure all this fields about cancer are not required, since they are not in Questionnaire
    cancer = models.CharField(max_length=3, choices=YESNO_CHOICES, null=True, blank=True, verbose_name="Has the patient been diagnosed with cancer or a tumour", help_text='Please tick the check box if the patient has been diagnosed with or identifies as having any of the following')

    # reverted to previous version until South Migration is fixed
    # Trac #35
    #cancertype = models.CharField(max_length=30, null=True, blank=True, choices=CANCER_TYPE_CHOICES, verbose_name="if yes, please choose from the following options in it")
    # moved to fshd/models.py and fshd_questionnaire/models.py to avoid relation clash and provide 2 different names
    #cancertype = models.ManyToManyField(CancerTypeChoices, related_name='cancertypechoices_cancertype', blank=True, null=True,)

    cancerothers = models.CharField(max_length=30, null=True, blank=True, verbose_name="Others")
    cancerorgan = models.CharField(max_length=30, null=True, blank=True, verbose_name="If the patient was diagnosed with cancer please indicate the body organ it was diagnosed in")
    liver = models.BooleanField(verbose_name="Has the patient been diagnosed with: liver disease")
    miscarriage = models.BooleanField()
    gor = models.BooleanField(verbose_name="gastro-oesophageal reflux")
    gall_bladder = models.BooleanField(verbose_name="gall bladder disease")
    infection = models.BooleanField(verbose_name="chronic infection")
    sexual_dysfunction = models.BooleanField()
    constipation = models.BooleanField()
    cholesterol = models.BooleanField()
    cognitive_impairment = models.CharField(max_length=6, choices=COGNITIVE_CHOICES, null=True, blank=True)
    psychological = models.BooleanField(verbose_name="psychological problems")

    anxiety = models.BooleanField()
    depression = models.BooleanField()
    apathy = models.BooleanField()
    weight = models.IntegerField(verbose_name="body weight", help_text="Body weight in kilograms", null=True, blank=True)
    height = models.IntegerField(verbose_name="height", help_text="Height in centimetres", null=True, blank=True)
    endocrine = models.BooleanField(verbose_name="endocrine disorders")
    obgyn = models.BooleanField(verbose_name="OB/GYN issues")

    # added according to questionnaire
    medicalert = models.CharField(verbose_name="Does the patient wear a Medicalert bracelet", choices=UYN_CHOICES, max_length=1, null=True, blank=True, default='')

    physiotherapy = models.CharField(verbose_name="Has the patient received any of the following: Physiotherapy", choices=UYN_CHOICES, max_length=1, null=True, blank=True, default='')
    # Trac #36
    psychologicalcounseling = models.CharField(verbose_name="Emotional & psychological counselling", choices=UYN_CHOICES, max_length=1, null=True, blank=True, default='')
    speechtherapy = models.CharField(verbose_name="Speech therapy", choices=UYN_CHOICES, max_length=1, null=True, blank=True, default='')
    occupationaltherapy = models.CharField(verbose_name="Occupational therapy", choices=UYN_CHOICES, max_length=1, null=True, blank=True, default='')
    vocationaltraining = models.CharField(verbose_name="Vocational rehabilitation", choices=UYN_CHOICES, max_length=1, null=True, blank=True, default='')

    class Meta:
        abstract = True

    def bmi(self):
        return self.weight / (self.height * self.height)


class GeneticTestDetails(models.Model):
    METHOD_CHOICES = (
        ("southern", "Southern"),
        ("pcr", "PCR"),
        ("rppcr", "RP-PCR"),
        ("other", "Other"),
    )

    UYN_CHOICES = (
        ('U', 'Unknown'),
        ('Y', 'Yes'),
        ('N', 'No'),
    )

    YES_NO_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )

    #details = models.NullBooleanField(verbose_name="details", help_text="Are details of genetic testing available?")
    details = models.CharField(max_length=1, choices=UYN_CHOICES, verbose_name="Are details of genetic testing available") # required

    # TODO: add the "null=True, blank=True" attributes when the DDL change for the table column is ready, otherwise exception when saving with a blank date
    # ALTER TABLE dev_fshd_registry.public.fshd_genetictestdetails ALTER COLUMN test_date DROP NOT NULL;
    # this works in PGAdmin III when using the "registryapp" username & pass:
    # ALTER TABLE "dev_fshd_registry"."public"."fshd_genetictestdetails" ALTER COLUMN test_date DROP NOT NULL;
    # ALTER TABLE dev_fshd_registry.public.fshd_genetictestdetails ALTER COLUMN test_date DROP NOT NULL;

    #test_date = models.DateField(null=True, blank=True, verbose_name="Genetic Test Date")
    test_date = models.DateField(verbose_name="Genetic Test Date", null=True, blank=True) # required, but need to check Yes to previous question
    # not used in questionnaire, should we keep it in the registry?
    laboratory = models.CharField(max_length=256, null=True, blank=True)

    # added for the questionnaire 2012-02-20
    counselling = models.CharField(max_length=1, choices=UYN_CHOICES, null=True, blank=True, verbose_name="Has the patient received genetic counselling")
    familycounselling = models.CharField(max_length=1, choices=UYN_CHOICES, null=True, blank=True, verbose_name="Has any of the patient's family members received genetic counselling")

    class Meta:
        abstract = True

class EthnicOrigin(models.Model):
    ORIGIN_CHOICES = (
        # changed according to Trac 16 FSHD Questionnaire #64. Questionnaire and Registry options are made the same now
        ("abo", "Aboriginal"),
        ("tsi", "Person from the Torres Strait Islands"),
        ("bla", "Black African/African American"),
        ("cau", "Caucasian/European"),
        ("chi", "Chinese"),
        ("ind", "Indian"),
        ("mao", "Maori"),
        ("mea", "Middle Eastern"),
        ("pac", "Person from the Pacific Islands"),
        ("asi", "Other Asian"),
        ("oth", "Other"),
        ("dcl", "Decline to answer"),
    )

    ethnic_origin = models.CharField(null=True, blank=True, max_length=9, choices=ORIGIN_CHOICES, help_text="How does the patient describe their ethnic origin?")

    class Meta:
        abstract = True


class ClinicalTrials(models.Model):
    drug_name = models.CharField(max_length=50, null=True, blank=True)
    trial_name = models.CharField(max_length=50, null=True, blank=True)
    trial_sponsor = models.CharField(max_length=50, null=True, blank=True)
    trial_phase = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        abstract = True

class Consent(models.Model):
    YES_NO_CHOICES = (('N', 'No'), ('Y', 'Yes'))

    q1 = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True, default='', verbose_name='Do we have your permission to store your personal & clinical data in the Australasian National Facioscapulohumeral Muscular Dystrophy Registry and to transfer it (in a form identifiable only by a code) to the global TREAT-NMD registry in which it may be used for research and for the planning of clinical trials?')
    q2 = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True, default='', verbose_name='Do we have your permission to obtain your Facioscapulohumeral Muscular Dystrophy genetic test result from the relevant testing laboratory to store this information with your clinical and personal information in the Australasian National Myotonic  Dystrophy Registry and to transfer it (in a form identifiable only by a code) to the global TREAT-NMD registry where it may be used for research and for the planning of clinical trials?')
    q3 = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True, default='', verbose_name='If we receive information on TREAT-NMD projects or other information related to your disease which might be relevant to you, would you like to be informed about this?')
    q4 = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True, default='', verbose_name='If your doctor receives information about a clinical trial which you might be eligible for, would you like to be informed about this?')
    q5 = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True, default='', verbose_name='So that we can keep the registry up to date, we will need to update your records once a year. Do you agree to receive follow-up forms once a year which you will be asked to complete in order to register any changes in your medical condition or contact details?')
    q6 = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True, default='', verbose_name='To improve the quality of the family history data on the Registry, we propose to link your record to any other affected family member or relative on the Registry. The link will only show your Unique identification number and your relationship to the affected relative. Do you agree to have your record linked to any other affected relatives on the Registry?')
    q7 = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True, default='', verbose_name='If there are any major changes in your data (for example change of address or changes in your medical condition, such as loss of ability to walk unassisted) that occur in the period between updates, are you willing to inform us?')

    #consentdate = models.DateField(verbose_name="Consent Date", null=True, blank=True, default=datetime.date.today())
    consentdate = models.DateField(verbose_name="Consent Date", null=True, blank=True, default=None)

    firstnameparentguardian = models.CharField(null=True, blank=True, default='', max_length=60, verbose_name="Parent/guardian's first name")
    lastnameparentguardian = models.CharField(null=True, blank=True, default='', max_length=60, verbose_name="Parent/guardian's last name")
    #consentdateparentguardian = models.DateField(verbose_name="Parent/guardian's Consent Date", null=True, blank=True, default=datetime.date.today())
    consentdateparentguardian = models.DateField(verbose_name="Parent/guardian's Consent Date", null=True, blank=True, default=None)

    # TODO: add doctors 1-10
    doctor_0 = models.CharField(null=True, blank=True, max_length=60, verbose_name="Doctor's name", default=None)
    doctoraddress_0 = models.CharField(null=True, blank=True, max_length=120, verbose_name="Doctor's address", default=None)
    doctortelephone_0 = models.CharField(null=True, blank=True, max_length=40, verbose_name="Doctor's phone", default=None)
    specialist_0 = models.CharField(null=True, blank=True, max_length=60, verbose_name="Specialist's name", default=None)

    doctor_1 = models.CharField(null=True, blank=True, max_length=60, verbose_name="Doctor's name", default=None)
    doctoraddress_1 = models.CharField(null=True, blank=True, max_length=120, verbose_name="Doctor's address", default=None)
    doctortelephone_1 = models.CharField(null=True, blank=True, max_length=40, verbose_name="Doctor's phone", default=None)
    specialist_1 = models.CharField(null=True, blank=True, max_length=60, verbose_name="Specialist's name", default=None)

    doctor_2 = models.CharField(null=True, blank=True, max_length=60, verbose_name="Doctor's name", default=None)
    doctoraddress_2 = models.CharField(null=True, blank=True, max_length=120, verbose_name="Doctor's address", default=None)
    doctortelephone_2 = models.CharField(null=True, blank=True, max_length=40, verbose_name="Doctor's phone", default=None)
    specialist_2 = models.CharField(null=True, blank=True, max_length=60, verbose_name="Specialist's name", default=None)

    doctor_3 = models.CharField(null=True, blank=True, max_length=60, verbose_name="Doctor's name", default=None)
    doctoraddress_3 = models.CharField(null=True, blank=True, max_length=120, verbose_name="Doctor's address", default=None)
    doctortelephone_3 = models.CharField(null=True, blank=True, max_length=40, verbose_name="Doctor's phone", default=None)
    specialist_3 = models.CharField(null=True, blank=True, max_length=60, verbose_name="Specialist's name", default=None)

    doctor_4 = models.CharField(null=True, blank=True, max_length=60, verbose_name="Doctor's name", default=None)
    doctoraddress_4 = models.CharField(null=True, blank=True, max_length=120, verbose_name="Doctor's address", default=None)
    doctortelephone_4 = models.CharField(null=True, blank=True, max_length=40, verbose_name="Doctor's phone", default=None)
    specialist_4 = models.CharField(null=True, blank=True, max_length=60, verbose_name="Specialist's name", default=None)

    doctor_5 = models.CharField(null=True, blank=True, max_length=60, verbose_name="Doctor's name", default=None)
    doctoraddress_5 = models.CharField(null=True, blank=True, max_length=120, verbose_name="Doctor's address", default=None)
    doctortelephone_5 = models.CharField(null=True, blank=True, max_length=40, verbose_name="Doctor's phone", default=None)
    specialist_5 = models.CharField(null=True, blank=True, max_length=60, verbose_name="Specialist's name", default=None)

    doctor_6 = models.CharField(null=True, blank=True, max_length=60, verbose_name="Doctor's name", default=None)
    doctoraddress_6 = models.CharField(null=True, blank=True, max_length=120, verbose_name="Doctor's address", default=None)
    doctortelephone_6 = models.CharField(null=True, blank=True, max_length=40, verbose_name="Doctor's phone", default=None)
    specialist_6 = models.CharField(null=True, blank=True, max_length=60, verbose_name="Specialist's name", default=None)

    doctor_7 = models.CharField(null=True, blank=True, max_length=60, verbose_name="Doctor's name", default=None)
    doctoraddress_7 = models.CharField(null=True, blank=True, max_length=120, verbose_name="Doctor's address", default=None)
    doctortelephone_7 = models.CharField(null=True, blank=True, max_length=40, verbose_name="Doctor's phone", default=None)
    specialist_7 = models.CharField(null=True, blank=True, max_length=60, verbose_name="Specialist's name", default=None)

    doctor_8 = models.CharField(null=True, blank=True, max_length=60, verbose_name="Doctor's name", default=None)
    doctoraddress_8 = models.CharField(null=True, blank=True, max_length=120, verbose_name="Doctor's address", default=None)
    doctortelephone_8 = models.CharField(null=True, blank=True, max_length=40, verbose_name="Doctor's phone", default=None)
    specialist_8 = models.CharField(null=True, blank=True, max_length=60, verbose_name="Specialist's name", default=None)

    doctor_9 = models.CharField(null=True, blank=True, max_length=60, verbose_name="Doctor's name", default=None)
    doctoraddress_9 = models.CharField(null=True, blank=True, max_length=120, verbose_name="Doctor's address", default=None)
    doctortelephone_9 = models.CharField(null=True, blank=True, max_length=40, verbose_name="Doctor's phone", default=None)
    specialist_9 = models.CharField(null=True, blank=True, max_length=60, verbose_name="Specialist's name", default=None)

    class Meta:
        abstract = True

# moved from fshd/models.py to base to add to the questionnaire
class FamilyMember(models.Model):
    # Trac #37
    DIAGNOSIS_CHOICES = (
        ("FSHD", "Myotonic dystrophy Type 1 (FSHD)"),
        ("DM2", "Myotonic dystrophy Type 2 (DM2)"),
        ("Unknown", "Unknown"),
    )

    sex = models.CharField(max_length=1, choices=Patient.SEX_CHOICES, null=True, blank=True)
    relationship = models.CharField(max_length=50, null=True, blank=True)
    family_member_diagnosis = models.CharField(max_length=30, choices=DIAGNOSIS_CHOICES, verbose_name="diagnosis", null=True, blank=True)

    class Meta:
        abstract = True

class OtherRegistries(models.Model):
    registry = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        abstract = True
