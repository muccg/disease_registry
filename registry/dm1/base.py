# vim: set fileencoding=UTF-8:
from __future__ import division
from django.db import models


# Base abstract models for fields common to the registry proper and
# questionnaire.

class Diagnosis(models.Model):
    """
    FIRST_SYMPTOM_CHOICES = (
        ("Prenatal", "Prenatal — polyhydramnios and reduced fetal movements"),
        ("Feeding difficulties", "Feeding difficulties requiring tube at or near term"),
        ("Hypotonia", "Hypotonia"),
        ("Learning difficulties", "Learning difficulties"),
        ("Myotonia", "Myotonia"),
        ("Muscle weakness", "Muscle weakness"),
        ("Bilateral cataracts", "Bilateral cataracts"),
        ("Cardiac", "Cardiac symptoms"),
        ("Anaesthetic", "Anaesthetic problems"),
        ("Mother", "Mother of a child with congenital myotonic dystrophy"),
        ("Relative", "Relative of a person with myotonic dystrophy but no symptoms or clinical manifestations"),
        ("Other", "Other"),
    )
    """
    # Trac 16 #12 Now assigning numbers instead of lengthy strings. The database is not really in production yet, so we can change that
    FIRST_SYMPTOM_CHOICES = (
        ("1", "Concerns prior to birth eg decreased movements in the womb"),
        ("2", "Feeding difficulties requiring a feeding tube shortly after birth"),
        ("3", "Learning difficulties"),
        ("4", "Delayed development"),
        ("5", "Muscle weakness"),
        ("6", "Muscles difficult to relax or stiff (myotonia) "),
        ("7", "Cataracts"),
        ("8", "Heart problems"),
        ("9", "Problems with anaesthetics"),
        ("10", "Diagnosis of a family member with Myotonic dystrophy"),
        ("11", "Asymptomatic"),
    )

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
        ('FamilyHistory','Family History only'),
        ('AsymptomaticCarrier','Asymptomatic Carrier'),
        ('Congenital','Congenital Myotonic Distrophy'),
        ('Juvenile','Juvenile Myotonic Distrophy'),
        ('Adult','Adult Myotonic Distrophy'),
    )

    affectedstatus = models.CharField(max_length=30, choices=AFFECTED_STATUS_CHOICES, verbose_name='Affected Status')
    first_symptom = models.CharField('What was the first symptom that prompted the diagnosis of Myotonic dystrophy', max_length=50, choices=FIRST_SYMPTOM_CHOICES)
    first_suspected_by = models.CharField(max_length=50, choices=FIRST_SUSPECTED_CHOICES)
    # 2012-01-18: CAUTION TODO: IMPORTANT: the question is reverse from the questionnaire in forms.py: undiagnosed = forms.BooleanField(label="Have you been clinically diagnosed with myotonic dystrophy")
    # trac 16 #62
    undiagnosed = models.BooleanField(verbose_name="Yet undiagnosed")
    age_at_clinical_diagnosis = models.IntegerField('age in years at clinical diagnosis', null=True, blank=True)
    age_at_molecular_diagnosis = models.IntegerField('age in years at molecular diagnosis', null=True, blank=True)

    @property
    def diagnosed(self):
        return not self.diagnosed

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
        ("sitting", "Sitting independently"),
        ("none", "Never able to walk or sit independently")
    )

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

    walk = models.BooleanField(verbose_name="currently able to walk") # Trac 16 Item 48, removed help text
    walk_assisted = models.CharField(null=True, blank=True, max_length=50, choices=WALK_ASSISTED_CHOICES, verbose_name="current use of devices to assist with walking")
    walk_assisted_age = models.IntegerField(verbose_name="at what age did the patient commence using devices to assist with walking", null=True, blank=True, help_text="age in years")
    sit = models.BooleanField(verbose_name="currently able to sit without support", help_text="Able to maintain a sitting position on a chair or a wheelchair without support of upper limbs or leaning against the back of the chair")
    best_function = models.CharField(max_length=8, verbose_name="What is the best motor function level the patient has achieved", choices=MOTOR_FUNCTION_CHOICES, help_text="[Motor functions are listed in order with higher functions at the top, please choose one]<br/>Walking: walking with or without help (orthoses or assistive device or human assistance), inside or outdoors<br/>Sitting independently: able to maintain a sitting position on a chair or a wheelchair without support of upper limbs or leaning against the back of the chair")
    acquisition_age = models.IntegerField(verbose_name="At what age did the patient start walking", null=True, blank=True, help_text="Indicate age in years when the patient started walking")
    wheelchair_use = models.CharField(verbose_name="wheel chair use (over 3 years of age)", max_length=12, choices=WHEELCHAIR_USE_CHOICES, help_text="Yes (permanent): patient is not able to walk and needs a wheelchair to move<br/>Yes (intermittent): patient is still able to walk")
    wheelchair_usage_age = models.IntegerField(null=True, blank=True, help_text="If using wheelchair specify age at start of wheelchair use")
    dysarthria = models.IntegerField(choices=DYSARTHRIA_CHOICES)

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
    cardiac_implant = models.CharField(verbose_name="cardiac implant", max_length=30, choices=CARDIAC_IMPLANT_CHOICES, help_text="Have you had an operation to implant a device to control/normalise your heart rhythm?")
    cardiac_implant_age = models.IntegerField(verbose_name="age cardiac implant received", null=True, blank=True, help_text="Age at which cardiac implant received")
    cataract_diagnosis = models.BooleanField()
    #cataract = models.NullBooleanField(verbose_name="cataract surgery")
    cataract = models.CharField(max_length=1, choices=UYN_CHOICES, verbose_name="cataract surgery", null=True, blank=True)

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

    condition = models.CharField(verbose_name="heart condition", max_length=14, choices=HEART_CHOICES)
    age_at_diagnosis = models.IntegerField(verbose_name="At what age was the patient diagnosed with a heart condition", null=True, blank=True)

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

    non_invasive_ventilation = models.CharField(max_length=2, choices=VENTILATION_CHOICES, help_text="Mechanical ventilation with nasal or bucal mask")
    age_non_invasive_ventilation = models.IntegerField(null=True, blank=True, verbose_name="age ventilation device use commenced", help_text="Age at which non invasive ventilation device use started (leave blank if no ventilation device is in use)")
    non_invasive_ventilation_type = models.CharField(max_length=5, null=True, blank=True, choices=VENTILATION_TYPE_CHOICES)
    invasive_ventilation = models.CharField(max_length=2, choices=VENTILATION_CHOICES, help_text="Mechanical ventilation with tracheostomy")
    fvc = models.IntegerField(null=True, blank=True, verbose_name="FVC score", help_text="Pulmonary function test with spirometry; Forced Vital Capacity (FVC) expressed as % predicted for height (not in mL) and date of last examination")
    fvc_date = models.DateField(null=True, blank=True, verbose_name="FVC date")

    class Meta:
        abstract = True


class Muscle(models.Model):
    MUSCLE_CHOICES = (
        ("severe", "Yes, severely"),
        ("mild", "Yes, mildly"),
        ("no", "No"),
    )
    EFFECT_CHOICES = (
        ("yes", "Yes"),
        ("no", "No"),
    )

    myotonia = models.CharField(max_length=6, choices=MUSCLE_CHOICES, help_text="Does myotonia currently have a negative effect on the patient’s daily activities?")
    # TODO: uncomment, create migration script, syncdb & migrate
    #myotonia_effect = models.CharField(max_length=6, choices=EFFECT_CHOICES, help_text="Does myotonia currently have a negative effect on the patient’s daily activities?")

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
    DOZING_CHOICES = (
        (0, "Would never doze"),
        (1, "Slight chance of dozing"),
        (2, "Moderate chance of dozing"),
        (3, "High chance of dozing"),
    )

    FATIGUE_CHOICES = (
        ("severe", "Yes, severely"),
        ("mild", "Yes, mildly"),
        ("no", "No"),
    )

    fatigue = models.CharField(null=True, blank=True, max_length=6, choices=FATIGUE_CHOICES, help_text="Does fatigue or daytime sleepiness currently have a negative effect on the patient’s normal daily activities?")
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

    education = models.CharField(max_length=30, choices=EDUCATION_CHOICES)
    occupation = models.CharField(max_length=30, choices=OCCUPATION_CHOICES)
    employment_effect = models.CharField(max_length=30, choices=EFFECT_CHOICES, verbose_name="has Myotonic dystrophy affected the patient's employment")
    comments = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        abstract = True


class GeneralMedicalFactors(models.Model):
    YESNO_CHOICES = ( ('0', 'No'), ('1','Yes') )

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
    diabetes = models.CharField(max_length=30, choices=DIABETES_CHOICES)
    diabetesage = models.IntegerField(null=True, blank=True, help_text="Leave blank if you do not suffer from diabetes", verbose_name='Age at diagnosis')

    pneumonia = models.CharField(max_length=3, choices=YESNO_CHOICES, verbose_name="pneumonia")
    pneumoniaage = models.IntegerField(null=True, blank=True, verbose_name="pneumonia age", help_text="Age of first episode (leave blank if you have never suffered from pneumonia)")
    pneumoniainfections = models.CharField(max_length=60, null=True, blank=True, verbose_name="Chest infections recent frequency")

    # TODO: make sure all this fields about cancer are not required, since they are not in Questionnaire
    cancer = models.CharField(max_length=3, choices=YESNO_CHOICES, verbose_name="Has the patient been diagnosed with cancer or a tumour", help_text='Please tick the check box if the patient has been diagnosed with or identifies as having any of the following')
    cancertype = models.CharField(max_length=30, null=True, blank=True, choices=CANCER_TYPE_CHOICES, verbose_name="if yes, please choose from the following options in it")
    cancerothers = models.CharField(max_length=30, null=True, blank=True, verbose_name="Others")
    cancerorgan = models.CharField(max_length=30, null=True, blank=True, verbose_name="If the patient was diagnosed with cancer please indicate the body organ it was diagnosed in")
    liver = models.BooleanField(verbose_name="liver disease")
    miscarriage = models.BooleanField()
    gor = models.BooleanField(verbose_name="gastro-oesophageal reflux")
    gall_bladder = models.BooleanField(verbose_name="gall bladder disease")
    infection = models.BooleanField(verbose_name="chronic infection")
    sexual_dysfunction = models.BooleanField()
    constipation = models.BooleanField()
    cholesterol = models.BooleanField()
    cognitive_impairment = models.CharField(max_length=6, choices=COGNITIVE_CHOICES)
    psychological = models.BooleanField(verbose_name="psychological problems")

    anxiety = models.BooleanField()
    depression = models.BooleanField()
    apathy = models.BooleanField()
    weight = models.IntegerField(verbose_name="body weight", help_text="Body weight in kilograms")
    height = models.IntegerField(verbose_name="height", help_text="Height in centimetres")
    endocrine = models.BooleanField(verbose_name="endocrine disorders")
    obgyn = models.BooleanField(verbose_name="OB/GYN issues")

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

    #details = models.NullBooleanField(verbose_name="details", help_text="Are details of genetic testing available?")
    details = models.CharField(max_length=1, choices=UYN_CHOICES, null=True, blank=True, help_text="Are details of genetic testing available?")


    # TODO: add the "null=True, blank=True" attributes when the DDL change for the table column is ready, otherwise exception when saving with a blank date
    # ALTER TABLE dev_dm1_registry.public.dm1_genetictestdetails ALTER COLUMN test_date DROP NOT NULL;
    # this works in PGAdmin III when using the "registryapp" username & pass:
    # ALTER TABLE "dev_dm1_registry"."public"."dm1_genetictestdetails" ALTER COLUMN test_date DROP NOT NULL;
    # ALTER TABLE dev_dm1_registry.public.dm1_genetictestdetails ALTER COLUMN test_date DROP NOT NULL;

    #test_date = models.DateField(null=True, blank=True, verbose_name="Genetic Test Date")
    test_date = models.DateField(verbose_name="Genetic Test Date", null=True, blank=True)
    laboratory = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        abstract = True


class EthnicOrigin(models.Model):
    ORIGIN_CHOICES = (
        ("atsi", "Aboriginal or Torres Strait Islander"),
        ("black", "Black African/African American"),
        ("caucasian", "Caucasian/European"),
        ("chinese", "Chinese"),
        ("indian", "Indian"),
        ("maori", "Maori"),
        ("meastern", "Middle eastern"),
        ("pacific", "Pacific island person"),
        ("asian", "Other Asian"),
        ("other", "Other"),
        ("unknown", "Decline to answer"),
    )

    ethnic_origin = models.CharField(null=True, blank=True, max_length=9, choices=ORIGIN_CHOICES, help_text="How does the patient describe their ethnic origin?")

    class Meta:
        abstract = True


class ClinicalTrials(models.Model):
    drug_name = models.CharField(max_length=50)
    trial_name = models.CharField(max_length=50)
    trial_sponsor = models.CharField(max_length=50)
    trial_phase = models.CharField(max_length=50)

    class Meta:
        abstract = True
