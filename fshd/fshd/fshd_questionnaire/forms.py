from django import forms
from django.conf import settings
from django.forms.widgets import Select, RadioSelect, CheckboxSelectMultiple
from registry.forms.date import DateWidget
from registry.patients.models import Patient as RegistryPatient
from registry.utils import stripspaces

import models
from fshd.fshd import base
from models import Patient as FshdPatient

# Easily change the label to sound like a question without override
# automatic field types
class ModelQuestionnaireForm(forms.ModelForm):
    questions = {}
    def __init__(self, *args, **kwargs):
        super(ModelQuestionnaireForm, self).__init__(*args, **kwargs)
        for field in self.questions:
            if field in self.fields:
                self.fields[field].label = self.questions[field]

class ConsentForm(forms.ModelForm):
    CHOICES = (('N', 'NO'), ('Y', 'YES'))
    DATE_FORMATS = ('%d-%m-%Y', '%d/%m/%Y', '%d/%m/%y')

    # the default should be None, so none of the 2 radio buttons are selected, forcing the user to select one
    q1 = forms.ChoiceField(widget=RadioSelect, choices=CHOICES, required=True)
    q2 = forms.ChoiceField(widget=RadioSelect, choices=CHOICES, required=True)
    q3 = forms.ChoiceField(widget=RadioSelect, choices=CHOICES, required=True)
    q4 = forms.ChoiceField(widget=RadioSelect, choices=CHOICES, required=True)
    q5 = forms.ChoiceField(widget=RadioSelect, choices=CHOICES, required=True)
    q6 = forms.ChoiceField(widget=RadioSelect, choices=CHOICES, required=True)
    q7 = forms.ChoiceField(widget=RadioSelect, choices=CHOICES, required=True)

    firstname = forms.CharField(max_length=60, required = True, initial='')
    lastname = forms.CharField(max_length=60, required = True, initial='')
    consentdate = forms.DateField(required = True, input_formats=DATE_FORMATS, initial='')

    firstnameparentguardian = forms.CharField(max_length=60, required = False, initial='')
    lastnameparentguardian = forms.CharField(max_length=60, required = False, initial='')
    consentdateparentguardian =  forms.DateField(required = False, input_formats=DATE_FORMATS, initial='')

    # use that instead of a relation and a formset, just to get it up and running
    # this data is probably not gooing to be re-used
    doctor_0 = forms.CharField(max_length=60, required = False, initial='')
    doctoraddress_0 = forms.CharField(max_length=120, required = False, initial='')
    doctortelephone_0 = forms.CharField(max_length=40, required = False, initial='')
    specialist_0 = forms.CharField(max_length=60, required = False, initial='')

    doctor_1 = forms.CharField(max_length=60, required = False, initial='')
    doctoraddress_1 = forms.CharField(max_length=120, required = False, initial='')
    doctortelephone_1 = forms.CharField(max_length=40, required = False, initial='')
    specialist_1 = forms.CharField(max_length=60, required = False, initial='')

    doctor_2 = forms.CharField(max_length=60, required = False, initial='')
    doctoraddress_2 = forms.CharField(max_length=120, required = False, initial='')
    doctortelephone_2 = forms.CharField(max_length=40, required = False, initial='')
    specialist_2 = forms.CharField(max_length=60, required = False, initial='')

    doctor_3 = forms.CharField(max_length=60, required = False, initial='')
    doctoraddress_3 = forms.CharField(max_length=120, required = False, initial='')
    doctortelephone_3 = forms.CharField(max_length=40, required = False, initial='')
    specialist_3 = forms.CharField(max_length=60, required = False, initial='')

    doctor_4 = forms.CharField(max_length=60, required = False, initial='')
    doctoraddress_4 = forms.CharField(max_length=120, required = False, initial='')
    doctortelephone_4 = forms.CharField(max_length=40, required = False, initial='')
    specialist_4 = forms.CharField(max_length=60, required = False, initial='')

    doctor_5 = forms.CharField(max_length=60, required = False, initial='')
    doctoraddress_5 = forms.CharField(max_length=120, required = False, initial='')
    doctortelephone_5 = forms.CharField(max_length=40, required = False, initial='')
    specialist_5 = forms.CharField(max_length=60, required = False, initial='')

    doctor_6 = forms.CharField(max_length=60, required = False, initial='')
    doctoraddress_6 = forms.CharField(max_length=120, required = False, initial='')
    doctortelephone_6 = forms.CharField(max_length=40, required = False, initial='')
    specialist_6 = forms.CharField(max_length=60, required = False, initial='')

    doctor_7 = forms.CharField(max_length=60, required = False, initial='')
    doctoraddress_7 = forms.CharField(max_length=120, required = False, initial='')
    doctortelephone_7 = forms.CharField(max_length=40, required = False, initial='')
    specialist_7 = forms.CharField(max_length=60, required = False, initial='')

    doctor_8 = forms.CharField(max_length=60, required = False, initial='')
    doctoraddress_8 = forms.CharField(max_length=120, required = False, initial='')
    doctortelephone_8 = forms.CharField(max_length=40, required = False, initial='')
    specialist_8 = forms.CharField(max_length=60, required = False, initial='')

    doctor_9 = forms.CharField(max_length=60, required = False, initial='')
    doctoraddress_9 = forms.CharField(max_length=120, required = False, initial='')
    doctortelephone_9 = forms.CharField(max_length=40, required = False, initial='')
    specialist_9 = forms.CharField(max_length=60, required = False, initial='')

    class Meta:
        exclude = ("firstname", "lastname", "diagnosis")
        model = models.Consent

class DiagnosisForm(forms.ModelForm):
    age_at_clinical_diagnosis = forms.IntegerField(label='What was your age when you were clinically diagnosed?', required=False, max_value=120, min_value=0, help_text="Age in years")

    class Meta:
        exclude = ("patient", "affectedstatus", "age_at_molecular_diagnosis")
        model = models.Diagnosis

class MotorFunctionForm(ModelQuestionnaireForm):

    questions = {
        'best_function': 'Which of the following options describes the best motor function you are currently able to achieve?',
        'wheelchair_use': "Do you use a wheelchair or mobility scooter?",
        'wheelchair_usage_age': "At what age did you begin using a wheelchair or mobility scooter?"
    }

    #best_function = forms.CharField(label="Which of the following options describes the best motor function you are currently able to achieve", required=False, widget=Select(choices=models.MotorFunction.MOTOR_FUNCTION_CHOICES))

    #wheelchair_use = forms.CharField(label='Do you use a wheelchair', required=False, widget=Select(choices=models.MotorFunction.WHEELCHAIR_USE_CHOICES))
   #wheelchair_usage_age = forms.IntegerField(label='At what age did you start using a wheelchair', required=False, max_value=120, min_value=0, help_text="If using a wheelchair, specify age when wheelchair use started")

    class Meta:
        exclude = ("diagnosis")
        model = models.MotorFunction


class ClinicalFeaturesForm(ModelQuestionnaireForm):
    questions = {
        'eyes_dry': 'My eyes are dry and irritated occasionally/always',
        'difficulty_speaking': 'I have difficulty speaking',
        'difficulty_swallowing': 'I have difficulty swallowing',
        'trouble_whistling': 'I have trouble whistling/drinking through a straw',
        'periscapular_shoulder_weakness': 'Shoulder weakness (weakness of the muscles around the shoulder blades causing e.g. inability to raise your arms sideways above the level of your shoulder).',
        'foot_dorsiflexor_weakness': 'Foot weakness (weakness of the muscles that help you lift your feet up, causing e.g. foot drop (where the foot tends to hang with the toes pointing down), steppage gait (lifting the feet high when walking) or frequent tripping).',
        'hip_girld_weakness': 'Hip girdle weakness (weakness of the muscles of the pelvis and top of the legs, causing e.g. difficulties in going up stairs or ladders, rising from a chair or getting up from the floor).',
        'distal_upper_limb_weakness': 'Elbow or wrist weakness (weakness of your muscles which help you to lift or hold a pen)',
        'abdominal_muscle_weakness': 'Abdominal muscles weakness (do you have difficulty in the abdominal muscles which help you to sit up)',
        'retinal_vascular_disease': 'Have you been diagnosed with retinal vascular disease (problems with the retina of your eye causing e.g. loss of vision) that your doctors think may be related to your FSHD?',
        'retinal_vascular_disease_age': 'At what age were you diagnosed with retinal vascular disease?',
        'hearing_loss': 'Do you have hearing loss?',
        'hearing_loss_age': 'At what age did you first experience hearing loss?',
        'scapular_fixation': 'Have you had scapular fixation (an operation to fix your shoulder blade to your ribcage)?',
        'scapular_fixation_age': 'At what age did you have scapular fixation surgery?',
        'pain': 'Do you have pain? (indicate where the pain occurs)'
    }
    class Meta:
        exclude = ("diagnosis")
        model = models.ClinicalFeatures

class PregnancyForm(ModelQuestionnaireForm):
    questions = {
        'pregnancies': 'How many times have you been pregnant?',
        'childbirths': 'How many children do you have?'
    }
    class Meta:
        exclude = ("diagnosis",)
        model = models.Pregnancy


class HeartForm(ModelQuestionnaireForm):
    questions = {
        'condition': 'Do you have a heart condition?',
    }
    class Meta:
        exclude = ('diagnosis')
        model = models.Heart


class RespiratoryForm(forms.ModelForm):
    VENTILATION_CHOICES = (('', "-------"),) + base.Respiratory.VENTILATION_CHOICES

    non_invasive_ventilation = forms.CharField(widget=Select(choices=VENTILATION_CHOICES), required=False, label="Do you regularly use a non-invasive (mask) ventilation device?")
    age_non_invasive_ventilation = forms.IntegerField(label='If you use a ventilation device, at what age did you start using it', required=False, max_value=120, min_value=0)

    class Meta:
        exclude = ("diagnosis", "invasive_ventilation")
        model = models.Respiratory


class GeneticTestDetailsForm(ModelQuestionnaireForm):

    questions = {
        'result': 'What is your genetic test result?',
    }

    class Meta:
        exclude = ("diagnosis", "laboratory")
        model = models.GeneticTestDetails
        widgets = {
            "test_date": DateWidget(years=-10),
        }


class EthnicOriginForm(ModelQuestionnaireForm):

    questions = {
        'ethnic_origin': 'How would you describe your ethnic origin?'
    }

    class Meta:
        exclude = ("diagnosis",)
        model = models.EthnicOrigin


class FamilyMemberForm(ModelQuestionnaireForm):
    questions = {
        'relationship': 'Has anybody else in your family been diagnosed with FSHD (tick all that apply)?',
    }

    class Meta:
        exclude = ("diagnosis",)
        model = models.FamilyMember

class OtherRegistriesForm(ModelQuestionnaireForm):
    questions = {
        'registry': 'Have you signed up for any other FSHD registry?',
    }
    class Meta:
        exclude = ("diagnosis",)
        model = models.OtherRegistries
