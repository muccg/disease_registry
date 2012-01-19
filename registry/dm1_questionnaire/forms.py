from django import forms
from django.forms.models import inlineformset_factory
from django.forms.widgets import HiddenInput, DateInput, TextInput, Select, Textarea, RadioSelect
from registry.forms.widgets import LubricatedDateWidget
import models
from dm1 import base
from django.forms import Select

from models import Patient as Dm1Patient
from patients.models import Patient as RegistryPatient

from utils.stripspaces import stripspaces

class ConsentForm(forms.Form):
    consent = forms.BooleanField(required=True)


class DiagnosisForm(forms.ModelForm):
    # keep that in sync with base.py and add the null option
    FIRST_SYMPTOM_CHOICES_FORM = (('', "--------"),) + base.Diagnosis.FIRST_SYMPTOM_CHOICES
    FIRST_SUSPECTED_CHOICES_FORM = (('', "--------"),) + base.Diagnosis.FIRST_SUSPECTED_CHOICES
    DIAGNOSED_CHOICES = (('', "---"), ('False', 'No'), ('True', 'Yes'))

    #first_symptom = forms.CharField('What was the first symptom that prompted your diagnosis', widget=Select(choices=base.Diagnosis.FIRST_SYMPTOM_CHOICES))
    first_symptom = forms.CharField(label='What was the first symptom that prompted your diagnosis', widget=Select(choices=FIRST_SYMPTOM_CHOICES_FORM))
    first_suspected_by = forms.CharField(label='Who first suspected you to have Myotonic Dystrophy', widget=Select(choices=FIRST_SUSPECTED_CHOICES_FORM))
    # TODO: IMPORTANT: the question is reverse from the "Yest undiagnosed" in registry base.py
    #undiagnosed = forms.BooleanField(label="Have you been clinically diagnosed with myotonic dystrophy", widget=Select(choices=DIAGNOSED_CHOICES))
    #undiagnosed = forms.NullBooleanSelect(label="Have you been clinically diagnosed with myotonic dystrophy")
    undiagnosed = forms.CharField(label='Have you been clinically diagnosed with myotonic dystrophy', widget=Select(choices=DIAGNOSED_CHOICES))
    #TODO: shadow !undiagnosed in save
    #diagnosed = forms.BooleanField(label="diagnosed")

    age_at_clinical_diagnosis = forms.IntegerField(label='What was your age when you were clinically diagnosed', required=False, max_value=120, min_value=0, help_text="Age in years")

    class Meta:
        exclude = ("patient", "age_at_molecular_diagnosis")
        model = models.Diagnosis


class MotorFunctionForm(forms.ModelForm):
    WALK_CHOICES = (('', "---"), ('False', 'No'), ('True', 'Yes'))
    # Keep in sync with base.py!!!!
    WALK_ASSISTED_CHOICES = (
        ('', "-------"),
        ("No device", "No device required"), # Trac 16 #49
        # ("Ankle support", "Ankle support"), # Trac 16 Questionnaire #20, last item
        ("Stick", "Stick"),
        ("Walker", "Walker"))

    MOTOR_FUNCTION_CHOICES = (('', "-------"),) + base.MotorFunction.MOTOR_FUNCTION_CHOICES

    # Keep in sync with base.py!!!!
    WHEELCHAIR_USE_CHOICES = (
        ('', "-------"),
        ("never", "Never"),
        ("intermittent", "Yes (Intermittent): still able to walk"),
        ("permanent", "Yes (Permanent): not able to walk and need a wheelchair to move"),
        ("unknown", "Unknown"))

    DYSARTHRIA_CHOICES = (
        ('', "-------"),
        (0, "No"),
        (1, "Slightly slurred speech"),
        (2, "Some problems being understood"),
        (3, "Significant speech problems"),
    )

    walk = forms.CharField(label='Are you currently able to walk', widget=Select(choices=WALK_CHOICES), help_text="Walking without help or assisted walking (orthoses or assistive device or human assistance), indoors or outdoors")
    walk_assisted = forms.CharField(label='Do you currently use devices to assist with walking', widget=Select(choices=WALK_ASSISTED_CHOICES), help_text="Walking without help or assisted walking (orthoses or assistive device or human assistance), indoors or outdoors")
    walk_assisted_age = forms.IntegerField(label='At what age did you commence using devices to assist with walking', required=False, max_value=120, min_value=0, help_text="Age in years")
    sit = forms.BooleanField(label="Are you currently able to sit without support", widget=Select(choices=WALK_CHOICES), help_text="Able to maintain a sitting position on a chair or a wheelchair without support of upper limbs or leaning against the back of the chair")
    best_function = forms.CharField(label="What is the best motor function level you have achieved", widget=Select(choices=MOTOR_FUNCTION_CHOICES), help_text="Walking: walking with or without help (orthoses or assistive device or human assistance), inside or outdoors<br/>Sitting independently: able to maintain a sitting position on a chair or a wheelchair without support of upper limbs or leaning against the back of the chair")
    acquisition_age = forms.IntegerField(label='At what age did you start walking', required=False, max_value=120, min_value=0, help_text="Indicate the age in years when you started walking")
    wheelchair_use = forms.CharField(label='Do you use a wheelchair', widget=Select(choices=WHEELCHAIR_USE_CHOICES))
    wheelchair_usage_age = forms.IntegerField(label='At what age did you start using a wheelchair', required=False, max_value=120, min_value=0, help_text="If using a wheelchair, specify age when wheelchair use started")

    dysarthria = forms.IntegerField(label='Do you have problems with your speech', widget=Select(choices=DYSARTHRIA_CHOICES))

    class Meta:
        exclude = ("diagnosis",)
        model = models.MotorFunction
        #FJ Trac 16 item 15, change checkbox to drop down with Yes, No
        #widgets = { 'walk': Select( choices = ((None, '---'), ('0', 'No'), ('1','Yes')) ) }

class SurgeryForm(forms.ModelForm):
    CARDIAC_IMPLANT_CHOICES = (('', "-------"), # keep in sync with base.Surgery.CARDIAC_IMPLANT_CHOICES
        ("no", "No"),
        ("pacemaker", "Pacemaker"),
        ("icd", "Implantable cardioverter defibrillator"),
        ("yes", "Yes, not sure what type"),
    )
    CATARACT_CHOICES = (('', "---"), ('False', 'No'), ('True', 'Yes'))

    # keep in sync with base.Surgery.UYN_CHOICES
    CATARACT_SURGERY_CHOICES = (('', "---"), ('N', 'No'), ('Y', 'Yes'))

    #cardiac_implant = models.NullBooleanField(verbose_name="cardiac implant", help_text="Have you had an operation to implant a device to control/normalise your heart rhythm?")
    cardiac_implant = forms.CharField(label="Have you had an operation to insert a device to control/normalize your heart rhythm", widget=Select(choices=CARDIAC_IMPLANT_CHOICES))
    cardiac_implant_age = forms.IntegerField(label='At what age was this device for heart rhythm inserted', required=False, max_value=120, min_value=0)

    cataract_diagnosis = forms.CharField(label='Have you been diagnosed with cataracts in your eyes', widget=Select(choices=CATARACT_CHOICES))
    # This really should be cataract_surgery in the model and here.
    cataract = forms.CharField(label='Have you had eye surgery for cataract removal', widget=Select(choices=CATARACT_SURGERY_CHOICES))
    cataract_age = forms.IntegerField(label='At what age was the cataract surgery performed', required=False, max_value=120, min_value=0)

    class Meta:
        exclude = ("diagnosis",)
        model = models.Surgery


class HeartForm(forms.ModelForm):
    HEART_CHOICES = (('', "-------"),) + base.Heart.HEART_CHOICES

    condition = forms.CharField(label="Do you have a heart condition", widget=Select(choices=HEART_CHOICES))
    age_at_diagnosis = forms.IntegerField(label='At what age were you diagnosed with a heart condition', required=False, max_value=120, min_value=0)


    class Meta:
        exclude = ('diagnosis', 'ecg', 'ecg_sinus_rhythm', 'ecg_pr_interval', 'ecg_qrs_duration', 'ecg_examination_date',
                   'echocardiogram', 'echocardiogram_lvef', 'echocardiogram_lvef_date')
        model = models.Heart

class HeartMedicationForm(forms.ModelForm):
    class Meta:
        exclude = ("diagnosis",)
        model = models.HeartMedication


class RespiratoryForm(forms.ModelForm):
    VENTILATION_CHOICES = (('', "-------"),) + base.Respiratory.VENTILATION_CHOICES
    VENTILATION_TYPE_CHOICES = (('', "-------"),) + base.Respiratory.VENTILATION_TYPE_CHOICES

    non_invasive_ventilation = forms.CharField(widget=Select(choices=VENTILATION_CHOICES), label="Do you use a mechanical ventilation device (eg nasal or buccal mask)")
    age_non_invasive_ventilation = forms.IntegerField(label='If you use a ventilation device, at what age did you start using it', required=False, max_value=120, min_value=0)

    non_invasive_ventilation_type = forms.CharField(required=False, label='If you use a ventilation device, what type', widget=Select(choices=VENTILATION_TYPE_CHOICES))
    invasive_ventilation = forms.CharField(widget=Select(choices=VENTILATION_CHOICES), label="Do you use a tracheostomy for ventilation")

    class Meta:
        exclude = ("diagnosis", "fvc", "fvc_date")
        model = models.Respiratory


class MuscleForm(forms.ModelForm):
    # keep in sync with base.Surgery.UYN_CHOICES
    MYOTONIA_CHOICES = (('', "---"), ('N', 'No'), ('Y', 'Yes'))
    myotonia = forms.CharField(widget=Select(choices=MYOTONIA_CHOICES), label="Do you have problems with slow relaxation of muscles")
    # TODO: create the 'myotonia_effect' field in base and syncdb-migrate
    myotonia_effect = forms.CharField(widget=Select(choices=MYOTONIA_CHOICES), label="Do problems with slow relaxation of muscles currently have a negative effect on your normal daily activities")

    class Meta:
        exclude = ("diagnosis",)
        model = models.Muscle


class MuscleMedicationForm(forms.ModelForm):
    class Meta:
        exclude = ("diagnosis",)
        model = models.MuscleMedication


class FeedingFunctionForm(forms.ModelForm):
    # keep in sync with base.FeedingFunction.UYN_CHOICES
    DYSPHAGIA_CHOICES = (('', "---"), ('N', 'No'), ('Y', 'Yes'))
    dysphagia = forms.CharField(widget=Select(choices=DYSPHAGIA_CHOICES), label="Do you have difficulty swallowing")

    gastric_nasal_tube = forms.CharField(widget=Select(choices=DYSPHAGIA_CHOICES), label="Do you use a nasogastric or nasojejunal tube, or a gastrostomy for additional meal supplementation")

    class Meta:
        exclude = ("diagnosis",)
        model = models.FeedingFunction


class FatigueForm(forms.ModelForm):
    FATIGUE_CHOICES = (('', "---"), ('N', 'No'), ('Y', 'Yes'))
    fatigue = forms.CharField(widget=Select(choices=FATIGUE_CHOICES), label="Does fatigue or daytime sleepiness currently have a negative effect on your normal daily activities")

    class Meta:
        exclude = ("diagnosis",)
        model = models.Fatigue


class FatigueMedicationForm(forms.ModelForm):
    class Meta:
        exclude = ("diagnosis",)
        model = models.FatigueMedication


class SocioeconomicFactorsForm(forms.ModelForm):
    EDUCATION_CHOICES = (('', "-------"),) + base.SocioeconomicFactors.EDUCATION_CHOICES
    education = forms.CharField(label="What is the highest level of education you have achieved", widget=Select(choices=EDUCATION_CHOICES))

    OCCUPATION_CHOICES = (('', "-------"),) + base.SocioeconomicFactors.OCCUPATION_CHOICES
    occupation = forms.CharField(label="What is your occupation", widget=Select(choices=OCCUPATION_CHOICES))

    EFFECT_CHOICES = (('', "-------"),) + base.SocioeconomicFactors.EFFECT_CHOICES
    employment_effect = forms.CharField(label="Has myotonic dystrophy affected your employment", widget=Select(choices=EFFECT_CHOICES))

    comments = forms.CharField(required=False, widget=Textarea(attrs={"cols": 60, "rows": 3}))

    class Meta:
        exclude = ("diagnosis",)
        model = models.SocioeconomicFactors


class GeneralMedicalFactorsForm(forms.ModelForm):
    DIABETES_CHOICES = ( # keep in sync with base.GeneralMedicalFactors.DIABETES_CHOICES
        ('', "-------"),
        ('No', 'Not diagnosed'),
        ('SugarIntolerance', 'Have sugar intolerance but not diabetes'),
        ('Type1', 'Yes, Type 1 Diabetes'),
        ('Type2', 'Yes, Type 2 Diabetes'),
    )
    YESNO_CHOICES = (('', "---"),) + base.GeneralMedicalFactors.YESNO_CHOICES

    diabetes = forms.CharField(label="Have you been diagnosed with diabetes", widget=Select(choices=DIABETES_CHOICES))
    diabetesage = forms.IntegerField(required=False, label='Age at diagnosis')

    pneumonia = forms.CharField(label="Have you ever suffered from pneumonia, if yes please give the age when you first had it", widget=Select(choices=YESNO_CHOICES))
    pneumoniaage = forms.IntegerField(label='Age of first episode', required=False, max_value=120, min_value=0)

    # TODO: add this field to base!
    medicalert = forms.CharField(label="Do you wear a Medicalert bracelet", widget=Select(choices=YESNO_CHOICES))

    class Meta:
        exclude = ("diagnosis","cancer", "cancertype","cancerothers","cancerorgan","liver","miscarriage","gor","gall_bladder",
                   "infection","sexual_dysfunction","constipation","cholesterol","cognitive_impairment","psychological","endocrine","obgyn",
                   "anxiety","depression","apathy")
        model = models.GeneralMedicalFactors


class GeneticTestDetailsForm(forms.ModelForm):
    YESNO_CHOICES = (('', "---"), ('Y', 'Yes'), ('N', 'No'))

    details = forms.CharField(label="Have you had a genetic test for myotonic dystrophy", widget=Select(choices=YESNO_CHOICES))

    class Meta:
        exclude = ("diagnosis", "laboratory")
        model = models.GeneticTestDetails
        widgets = {
            "test_date": LubricatedDateWidget(years=-10),
        }


class EthnicOriginForm(forms.ModelForm):
    ORIGIN_CHOICES = (
        ('', "---"),
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

    ethnic_origin = forms.CharField(label="How would you describe your ethnic origin", widget=Select(choices=ORIGIN_CHOICES))

    class Meta:
        exclude = ("diagnosis",)
        model = models.EthnicOrigin


class ClinicalTrialsForm(forms.ModelForm):
    class Meta:
        exclude = ("diagnosis",)
        model = models.ClinicalTrials


class PatientForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = models.Patient
        #model = Dm1Patient  # The one for Dm1 registry and questionnaire with a Male/Female choice, without the Intersex option

        widgets = {
            "date_of_birth": LubricatedDateWidget(years=-100),
            "address": forms.Textarea(attrs={"cols": 60, "rows": 3}),
        }

    #FJ start
    # add check on uniqueness in the dm1_questionnaire.patients table and registry.patients as well
    def clean(self):
        '''
        Prevents saving a patient if there is an existing one with the same family name, given names in the same working group
        in both the DM1 questionnaire patient table and the Registry patient table
        '''
        cleaneddata = self.cleaned_data
        #print "PatientForm self %s" % dir(self)
        #print "cleaneddata: %s" % cleaneddata
        #print "instance %s" % self.instance.pk

        familyname = cleaneddata.get('family_name')
        if familyname:
            familyname = stripspaces(familyname).upper()

        givennames = cleaneddata.get('given_names')
        if givennames:
            givennames = stripspaces(givennames)

        if not familyname or not givennames:
            return cleaneddata  # the other validation will catch the empty fields

        workinggroup = cleaneddata['working_group']

        #print "familyname: %s givennames %s workinggroup %s" % (familyname, givennames, workinggroup)

        dm1patients = Dm1Patient.objects.filter(family_name__iexact=familyname, given_names__iexact=givennames, working_group=workinggroup)
        #print "dm1patients: %s" % dm1patients

        registrypatients = RegistryPatient.objects.filter(family_name__iexact=familyname, given_names__iexact=givennames, working_group=workinggroup)
        #print "registrypatients: %s" % registrypatients

        if len(dm1patients) > 0 or len(registrypatients) > 0:
            #print "raise forms.ValidationError"
            raise forms.ValidationError('There is already a patient with the same family and given names in this working group: "%s %s %s".' % (familyname, givennames, workinggroup))
        return cleaneddata
    #FJ end
