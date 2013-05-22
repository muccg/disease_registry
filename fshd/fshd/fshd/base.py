# vim: set fileencoding=UTF-8:
from __future__ import division
from django.db import models

from registry.patients.models import Patient

# Base abstract models for fields common to the registry proper and
# questionnaire.

class Diagnosis(models.Model):
    age_at_clinical_diagnosis = models.IntegerField('age in years at clinical diagnosis', null=True, blank=True)
    age_at_molecular_diagnosis = models.IntegerField('age in years at molecular diagnosis', null=True, blank=True)

    class Meta:
        abstract = True

class ClinicalFeatures(models.Model):
    facial_weakness_choices = (
        ("no weakness",)*2,
        ("eyes dry and irritated occasionally/always",)*2,
        ("difficulty speaking",)*2,
        ("difficulty swallowing",)*2,
        ("trouble whistling/drinking through a straw",)*2,
    )
    periscapular_shoulder_weakness_choices = (
        ("no weakness",)*2,
        ("able to raise arms sideways over head",)*2,
        ("able to raise arms sideways to shoulder height",)*2,
        ("unable to raise arms sideways",)*2,
    )
    foot_dorsiflexor_weakness_choices = (
        ("yes",)*2,
        ("no",)*2,
    )
    hip_girdle_weakness_choices = (
        ("no weakness - can rise from chair without raising arms",)*2,
        ("use arms to push up from chair",)*2,
        ("only with assistance from person or device",)*2,
        ("sit up without using arms",)*2,
        ("sit up only be using arms",)*2,
        ("sit up only by turning sideways and using arms",)*2,
        ("sit up only with someones's assistance",)*2,
        ("transfer from bed to chair with assistive device",)*2,
    )
    distal_upper_limb_weakness_choices = (
        ("yes",)*2,
        ("no",)*2,
    )
    abdominal_muscle_weakness_choices = (
        ("yes",)*2,
        ("no",)*2,
    )
    leg_function_choices = (
        ("unable to walk",)*2,
        ("walk and run",)*2,
        ("walk and not run",)*2,
        ("walk and climb stairs",)*2,
        ("walk and climb stairs with railing",)*2,
        ("walk with cane/walker and unable to use stairs",)*2,
    )
    retinal_vascular_disease_choices = (
        ("yes (start date month/year",)*2,
        ("no",)*2,
        ("unknown",)*2,
    )
    hearing_loss_choices = (
        ("yes (start date month/year",)*2,
        ("no",)*2,
        ("unknown",)*2,
    )
    scapular_fixation_choices = (
        ("yes, bilateral (surgery dates month/year",)*2,
        ("yes - unilateral (surgery dates month/year",)*2,
        ("no",)*2,
    )
    pain_choices = (
        ("neck",)*2,
        ("shoulders",)*2,
        ("lower back",)*2,
        ("knees and thighs",)*2,
        ("head",)*2,
        ("shoulders",)*2,
        ("knees",)*2,
        ("toes",)*2,
        ("eyes and ears and mouth and nose",)*2,
    )

    facial_weakness = models.CharField(
            default=facial_weakness_choices[0],
            choices=facial_weakness_choices,
            max_length=len(max(facial_weakness_choices))
    )

    periscapular_shoulder_weakness = models.CharField(
            default=periscapular_shoulder_weakness_choices[0],
            choices=periscapular_shoulder_weakness_choices,
            max_length=len(max(periscapular_shoulder_weakness_choices))
    )

    foot_dorsiflexor_weakness = models.CharField(
            default=foot_dorsiflexor_weakness_choices[0],
            choices=foot_dorsiflexor_weakness_choices,
            max_length=len(max(foot_dorsiflexor_weakness_choices))
    )

    hip_girdle_weakness = models.CharField(
            default=hip_girdle_weakness_choices[0],
            choices=hip_girdle_weakness_choices,
            max_length=len(max(hip_girdle_weakness_choices))
    )

    distal_upper_limb_weakness = models.CharField(
            default=distal_upper_limb_weakness_choices[0],
            choices=distal_upper_limb_weakness_choices,
            max_length=len(max(distal_upper_limb_weakness_choices))
    )

    abdominal_muscle_weakness = models.CharField(
            default=abdominal_muscle_weakness_choices[0],
            choices=abdominal_muscle_weakness_choices,
            max_length=len(max(abdominal_muscle_weakness_choices))
    )

    leg_function = models.CharField(
            default=leg_function_choices[0],
            choices=leg_function_choices,
            max_length=len(max(leg_function_choices))
    )

    retinal_vascular_disease = models.CharField(
            default=retinal_vascular_disease_choices[0],
            choices=retinal_vascular_disease_choices,
            max_length=len(max(retinal_vascular_disease_choices))
    )

    hearing_loss = models.CharField(
            default=hearing_loss_choices[0],
            choices=hearing_loss_choices,
            max_length=len(max(hearing_loss_choices))
    )

    scapular_fixation = models.CharField(
            default=scapular_fixation_choices[0],
            choices=scapular_fixation_choices,
            max_length=len(max(scapular_fixation_choices))
    )

    pain = models.CharField(
            default=pain_choices[0],
            choices=pain_choices,
            max_length=len(max(pain_choices))
    )

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
    registry = models.CharField(max_length=70, null=True, blank=True)

    class Meta:
        abstract = True
