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
    )

    eyes_dry = models.BooleanField(default=False, verbose_name='eyes dry and irritated occasionally/always')
    difficulty_speaking = models.BooleanField(default=False, verbose_name='difficulty speaking')
    difficulty_swallowing = models.BooleanField(default=False, verbose_name='difficulty swallowing')
    trouble_whistling = models.BooleanField(default=False, verbose_name='trouble whistling/drinking through a straw')

    periscapular_shoulder_weakness = models.CharField(
            default=periscapular_shoulder_weakness_choices[0],
            choices=periscapular_shoulder_weakness_choices,
            max_length=100
    )

    foot_dorsiflexor_weakness = models.CharField(
            default=foot_dorsiflexor_weakness_choices[0],
            choices=foot_dorsiflexor_weakness_choices,
            max_length=100
    )

    hip_girdle_weakness = models.CharField(
            default=hip_girdle_weakness_choices[0],
            choices=hip_girdle_weakness_choices,
            max_length=100
    )

    distal_upper_limb_weakness = models.CharField(
            default=distal_upper_limb_weakness_choices[0],
            choices=distal_upper_limb_weakness_choices,
            max_length=100
    )

    abdominal_muscle_weakness = models.CharField(
            default=abdominal_muscle_weakness_choices[0],
            choices=abdominal_muscle_weakness_choices,
            max_length=100
    )

    leg_function = models.CharField(
            blank=True,
            default='',
            choices=leg_function_choices,
            max_length=100
    )

    retinal_vascular_disease = models.CharField(
            blank=True,
            default=retinal_vascular_disease_choices[0],
            choices=retinal_vascular_disease_choices,
            max_length=100
    )

    retinal_vascular_disease_age = models.IntegerField(blank=True)

    hearing_loss = models.CharField(
            blank=True,
            default=hearing_loss_choices[0],
            choices=hearing_loss_choices,
            max_length=100
    )

    hearing_loss_age = models.IntegerField(blank=True)

    scapular_fixation = models.CharField(
            blank=True,
            default=scapular_fixation_choices[0],
            choices=scapular_fixation_choices,
            max_length=100
    )

    scapular_fixation_age = models.IntegerField(blank=True)

    pain = models.CharField(
            blank=True,
            default=pain_choices[0],
            choices=pain_choices,
            max_length=100
    )

    class Meta:
        abstract = True

class Pregnancy(models.Model):

    pregnancies = models.IntegerField(default=0,blank=True,verbose_name="Number of pregnancies")
    childbirths = models.IntegerField(default=0,blank=True,verbose_name="Number of child births")

    class Meta:
        abstract = True


class MotorFunction(models.Model):

    MOTOR_FUNCTION_CHOICES = (
        ('Ambulatory (unassisted)',)*2,
        ('Ambulatory assisted - walker',)*2,
        ('Ambulatory assisted - brace/splint/orthoses',)*2,
        ('Ambulatory assisted - walking stick',)*2,
        ('Non-ambulatory',)*2
    )

    WHEELCHAIR_USE_CHOICES = (
        ("no", "No"),
        ("parttime", "Part-time"),
        ("fulltime", "Full-time")
    )

    best_function = models.CharField(choices=MOTOR_FUNCTION_CHOICES, default='', max_length=100, verbose_name="What is the best motor function level the patient has achieved", help_text="[Motor functions are listed in order with higher functions at the top, please choose one]<br/>Walking: walking with or without help (orthoses or assistive device or human assistance), inside or outdoors")
    wheelchair_use = models.CharField(verbose_name="wheel chair use", default='', max_length=100, choices=WHEELCHAIR_USE_CHOICES, help_text="<b>Yes (permanent):</b> patient is not able to walk and needs a wheelchair to move<br/><b>Yes (intermittent):</b> patient is still able to walk") #required
    wheelchair_usage_age = models.IntegerField(null=True, blank=True, help_text="If using wheelchair specify age at start of wheelchair use") # required but need to check Yes previous question

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


    condition = models.CharField(verbose_name="heart condition", max_length=14, choices=HEART_CHOICES, null=True, blank=True)
    
    class Meta:
        abstract = True


class Respiratory(models.Model):
    VENTILATION_CHOICES = (
        ("N", "No"),
        ("PT", "Yes (night only)"), # was "part-time"
        ("Y", "Yes (day and night)"),
    )

    non_invasive_ventilation = models.CharField(max_length=2, null=True, blank=True, choices=VENTILATION_CHOICES, help_text="Mechanical ventilation with nasal or bucal mask")
    age_non_invasive_ventilation = models.IntegerField(null=True, blank=True, verbose_name="age ventilation device use commenced", help_text="Age at which non invasive ventilation device use started (leave blank if no ventilation device is in use)")
    invasive_ventilation = models.CharField(max_length=2, null=True, blank=True, choices=VENTILATION_CHOICES, help_text="Mechanical ventilation with tracheostomy")

    class Meta:
        abstract = True


class GeneticTestDetails(models.Model):
    METHOD_CHOICES = (
        ("EcoR1/AvrII", "EcoR1/AvrII"),
        ("EcoR1/Blnl", "EcoR1/Blnl"),
        ("other", "Other"),
    )

    result_choices = (
        ("Confirmed FSHD 2 (contraction independent D4Z4 hypomethylation on the 4qA161 subtelomere).",)*2,
        ("Result pending",)*2,
        ("Genetic test is negative for FSHD1. However clinician identifies FSDH as best known diagnosis",)*2,
        ("Not tested",)*2,
        ("I have not been tested.  However clinician identifies FSDH as best known diagnosis",)*2,
        ("Other result positive for FSHD",)*2,
        ("FSHD1 confirmed: 1-9 D4Z4 repeats",)*2,
        ("FSHD1 borderline: 10-11 D4Z4 repeats",)*2,
        ("FSHD1 excluded: 12-100 D4Z4 repeats",)*2,
        ("FSHD1 borderline: 10-11 D4Z4 repeats ",)*2,
    )

    result = models.CharField(
        default=result_choices[0],
        choices=result_choices,
        max_length=len(max(result_choices,key=len)[0])
    )
    comments = models.TextField(blank=True)

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
    RELATIONSHIP_CHOICES = (
        ("affected mother",)*2,
        ("affected mother",)*2,
        ("affected sibling(s)",)*2,
        ("affected child/children",)*2,
        ("other affected relative",)*2,
        ("no",)*2,
        ("unknown",)*2,

    )

    relationship = models.CharField(max_length=100, choices=RELATIONSHIP_CHOICES, verbose_name="relationship", null=True, blank=True)

    class Meta:
        abstract = True

class OtherRegistries(models.Model):
    registry = models.CharField(max_length=70, null=True, blank=True)

    class Meta:
        abstract = True
