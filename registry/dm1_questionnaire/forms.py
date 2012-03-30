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
    # keep that in sync with base.py and add the null option
    DIAGNOSIS_CHOICES = (
        ('', "--------"),
        ("DM1", "DM1"),
        ("DM2", "DM2"),
        ("O", "Not yet diagnosed"), # the text is different from registry, but the value is the same as 'Other' in the registry in base.py
    )

    # keep the values in sync with base.py base.Diagnosis.FIRST_SYMPTOM_CHOICES
    FIRST_SYMPTOM_CHOICES_FORM = (('', "--------"),
        ("1", "Concerns prior to/or around the time of birth eg decreased movements in the womb"),  #"Prenatal - polyhydramnios and reduced fetal movements"),
        ("2", "Feeding difficulties requiring a feeding tube shortly after birth"),  #"Feeding difficulties requiring tube at or near term"),
        #("3", ""),  #"Hypotonia"),
        ("4", "Learning difficulties"),  #"Learning difficulties"),
        ("5", "Delayed development"),  #"Delayed development"),
        ("6", "Muscles difficult to relax or stiff (myotonia)"),  #"Myotonia"),
        ("7", "Muscle weakness"),  #"Muscle weakness"),
        ("8", "Cataracts"),  #"Bilateral cataracts"),
        ("9", "Heart problems"),  #"Cardiac symptoms"),
        ("10", "Problems with anaesthetics"), #"Anaesthetic problems"),
        #("11", ""), #"Patient is the mother of a child with congenital myotonic dystrophy"),
        ("12", "Asymptomatic"), #"Patient asymptomatic"),
        ("13", "Diagnosis of a family member with Myotonic dystrophy"), #"Diagnosis of a family member with Myotonic dystrophy"),
        #("14", "")) #"Other")
        )

    FIRST_SUSPECTED_CHOICES_FORM = (('', "--------"),) + base.Diagnosis.FIRST_SUSPECTED_CHOICES
    DIAGNOSED_CHOICES = (('', "---"), ('False', 'No'), ('True', 'Yes'))

    diagnosis = forms.CharField(label='What type of Myotonic dystrophy have you been diagnosed with?', widget=Select(choices=DIAGNOSIS_CHOICES), required=False)

    #first_symptom = forms.CharField('What was the first symptom that prompted your diagnosis', widget=Select(choices=base.Diagnosis.FIRST_SYMPTOM_CHOICES))
    first_symptom = forms.CharField(label='What was the first symptom that prompted your diagnosis?', widget=Select(choices=FIRST_SYMPTOM_CHOICES_FORM), required=False)
    first_suspected_by = forms.CharField(label='Who first suspected you to have Myotonic Dystrophy?', widget=Select(choices=FIRST_SUSPECTED_CHOICES_FORM), required=False)

    age_at_clinical_diagnosis = forms.IntegerField(label='What was your age when you were clinically diagnosed?', required=False, max_value=120, min_value=0, help_text="Age in years")

    class Meta:
        exclude = ("patient", "affectedstatus", "age_at_molecular_diagnosis")
        model = models.Diagnosis


class MotorFunctionForm(forms.ModelForm):
    WALK_CHOICES = (('', "---"),) + base.MotorFunction.YN_CHOICES
    WALK_ASSISTED_CHOICES = (('', "-------"),) + base.MotorFunction.WALK_ASSISTED_CHOICES
    # caution: keep in sync with base.MotorFunction.MOTOR_FUNCTION_CHOICES
    MOTOR_FUNCTION_CHOICES = (
        ('', "-------"),
        ("walking", "Walking independently"),
        ("assisted", "Walking assisted"),
        ("nonamb", "I cannot walk"), # added v3
    )

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

    walk = forms.CharField(label='Are you currently able to walk', required=False, widget=Select(choices=WALK_CHOICES), help_text="Walking without help or assisted walking (orthoses or assistive device or human assistance), indoors or outdoors")
    walk_assisted = forms.CharField(label='Do you currently use devices to assist with walking', required=False, widget=Select(choices=WALK_ASSISTED_CHOICES), help_text="Walking without help or assisted walking (orthoses or assistive device or human assistance), indoors or outdoors")
    walk_assisted_age = forms.IntegerField(label='At what age did you commence using devices to assist with walking', required=False, max_value=120, min_value=0, help_text="Age in years")
    # removed v3
    #sit = forms.BooleanField(label="Are you currently able to sit without support", widget=Select(choices=WALK_CHOICES), help_text="Able to maintain a sitting position on a chair or a wheelchair without support of upper limbs or leaning against the back of the chair")
    # removed v3
    #acquisition_age = forms.IntegerField(label='At what age did you start walking', required=False, max_value=120, min_value=0, help_text="Indicate the age in years when you started walking")
    best_function = forms.CharField(label="Which of the following options describes the best motor function you are currently able to achieve", required=False, widget=Select(choices=MOTOR_FUNCTION_CHOICES))

    wheelchair_use = forms.CharField(label='Do you use a wheelchair', required=False, widget=Select(choices=WHEELCHAIR_USE_CHOICES))
    wheelchair_usage_age = forms.IntegerField(label='At what age did you start using a wheelchair', required=False, max_value=120, min_value=0, help_text="If using a wheelchair, specify age when wheelchair use started")

    dysarthria = forms.IntegerField(label='Do you have problems with your speech', required=False, widget=Select(choices=DYSARTHRIA_CHOICES))

    class Meta:
        exclude = ("diagnosis", "best_function")
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
    cardiac_implant = forms.CharField(label="Have you had an operation to insert a device to control/normalize your heart rhythm", required=False, widget=Select(choices=CARDIAC_IMPLANT_CHOICES))
    cardiac_implant_age = forms.IntegerField(label='At what age was this device for heart rhythm inserted', required=False, max_value=120, min_value=0)

    cataract_diagnosis = forms.CharField(label='Have you been diagnosed with a cataract', required=False, widget=Select(choices=CATARACT_CHOICES))
    # This really should be cataract_surgery in the model and here.
    cataract = forms.CharField(label='Have you had eye surgery to remove a cataract', required=False, widget=Select(choices=CATARACT_SURGERY_CHOICES))
    cataract_age = forms.IntegerField(label='At what age was cataract surgery performed', required=False, max_value=120, min_value=0)

    class Meta:
        exclude = ("diagnosis",)
        model = models.Surgery


class HeartForm(forms.ModelForm):
    HEART_CHOICES = (('', "-------"),) + base.Heart.HEART_CHOICES
    YN_CHOICES = (('', "---"),) + base.Heart.YN_CHOICES

    condition = forms.CharField(label="Do you have a heart condition", required=False, widget=Select(choices=HEART_CHOICES))
    age_at_diagnosis = forms.IntegerField(label='At what age were you diagnosed with a heart condition', required=False, max_value=120, min_value=0)

    # Trac 16 DM1 Questionnaire Item 35, new fields
    # TODO: implement in Base.model to map them to Registry
    racing = forms.CharField(label="Do you experience: your heart racing or beating irregularly", widget=Select(choices=YN_CHOICES), required=False)
    palpitations = forms.CharField(label="heart palpitations", widget=Select(choices=YN_CHOICES), required=False)
    fainting = forms.CharField(label="black-outs or fainting", widget=Select(choices=YN_CHOICES), required=False)

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

    non_invasive_ventilation = forms.CharField(widget=Select(choices=VENTILATION_CHOICES), required=False, label="Do you use a mechanical ventilation device (eg nasal or buccal mask)")
    age_non_invasive_ventilation = forms.IntegerField(label='If you use a ventilation device, at what age did you start using it', required=False, max_value=120, min_value=0)

    non_invasive_ventilation_type = forms.CharField(required=False, label='If you use a ventilation device, what type', widget=Select(choices=VENTILATION_TYPE_CHOICES))
    invasive_ventilation = forms.CharField(widget=Select(choices=VENTILATION_CHOICES), required=False, label="Do you use a tracheostomy for ventilation")

    class Meta:
        exclude = ("diagnosis", "fvc", "fvc_date", "calculatedfvc")
        model = models.Respiratory


class MuscleForm(forms.ModelForm):
    # keep in sync with base.Surgery.UYN_CHOICES
    YN_CHOICES = (('', "---"),) + base.Muscle.MYOTONIA_CHOICES
    myotonia = forms.CharField(widget=Select(choices=YN_CHOICES), required=False, label="Do problems with slow relaxation of muscles currently have a negative effect on your normal daily activities?")

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
    dysphagia = forms.CharField(widget=Select(choices=DYSPHAGIA_CHOICES), required=False, label="Do you have difficulty swallowing")

    gastric_nasal_tube = forms.CharField(widget=Select(choices=DYSPHAGIA_CHOICES), required=False, label="Do you use a nasogastric or nasojejunal tube, or a gastrostomy for additional meal supplementation")

    class Meta:
        exclude = ("diagnosis",)
        model = models.FeedingFunction


class FatigueForm(forms.ModelForm):
    FATIGUE_CHOICES = (('', "---"),) + models.Fatigue.YN_CHOICES
    DOZING_CHOICES = (('', "-------"),) + models.Fatigue.DOZING_CHOICES
    fatigue = forms.CharField(widget=Select(choices=FATIGUE_CHOICES), required=False, label="Does fatigue or daytime sleepiness currently have a negative effect on your normal daily activities")
    sitting_reading = forms.IntegerField(label="Do you start to fall asleep in the following situations: Sitting and reading", widget=Select(choices=DOZING_CHOICES), required=False)

    #hereonlyforcaption = forms.CharField(label="hereonlyforcaption")
    # 'fields' ignored in the questionnaire form, must be an admin UI only thing
    #fields = ['fatigue', 'hereonlyforcaption','watching_tv','sitting_reading','sitting_inactive_public','passenger_car','lying_down_afternoon','sitting_talking','sitting_quietly_lunch','in_car'];

    class Meta:
        exclude = ("diagnosis",)
        model = models.Fatigue


class FatigueMedicationForm(forms.ModelForm):
    class Meta:
        exclude = ("diagnosis",)
        model = models.FatigueMedication


class SocioeconomicFactorsForm(forms.ModelForm):
    EDUCATION_CHOICES = (('', "-------"),) + base.SocioeconomicFactors.EDUCATION_CHOICES
    education = forms.CharField(label="What is the highest level of education you have achieved", required=False, widget=Select(choices=EDUCATION_CHOICES))

    OCCUPATION_CHOICES = (('', "-------"),) + base.SocioeconomicFactors.OCCUPATION_CHOICES
    occupation = forms.CharField(label="What is your occupation", required=False, widget=Select(choices=OCCUPATION_CHOICES))

    EFFECT_CHOICES = (('', "-------"),) + base.SocioeconomicFactors.EFFECT_CHOICES
    employment_effect = forms.CharField(label="Has myotonic dystrophy affected your employment", required=False, widget=Select(choices=EFFECT_CHOICES))

    class Meta:
        exclude = ("diagnosis",'comments')
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
    YESNOUNSURE_CHOICES = (('', "---"),) + base.GeneralMedicalFactors.YESNOUNSURE_CHOICES

    diabetes = forms.CharField(label="Have you been diagnosed with diabetes", required=False, widget=Select(choices=DIABETES_CHOICES))
    diabetesage = forms.IntegerField(required=False, label='Age at diagnosis')

    pneumonia = forms.CharField(label="Have you ever suffered from pneumonia, if yes please give the age when you first had it", required=False, widget=Select(choices=YESNO_CHOICES))
    pneumoniaage = forms.IntegerField(label='Age of first episode', required=False, max_value=120, min_value=0)

    medicalert = forms.CharField(label="Do you wear a Medicalert bracelet", widget=Select(choices=YESNO_CHOICES), required=False)

    physiotherapy = forms.CharField(label="Have you received any of the following: Physiotherapy", widget=Select(choices=YESNO_CHOICES), required=False)
    psychologicalcounseling = forms.CharField(label="Emotional & psychological counseling", widget=Select(choices=YESNO_CHOICES), required=False)
    speechtherapy = forms.CharField(label="Speech therapy", widget=Select(choices=YESNO_CHOICES), required=False)
    occupationaltherapy = forms.CharField(label="Occupational therapy", widget=Select(choices=YESNO_CHOICES), required=False)
    vocationaltraining = forms.CharField(label="Vocational rehabilitation", widget=Select(choices=YESNO_CHOICES), required=False)

    liver = forms.BooleanField(label="Have you been diagnosed with: Liver disease", required=False)

    class Meta:
        exclude = ("diagnosis","cancer", "cancertype","cancerothers","cancerorgan","cognitive_impairment","psychological","endocrine","obgyn",)
        model = models.GeneralMedicalFactors


class GeneticTestDetailsForm(forms.ModelForm):
    YESNO_CHOICES = (('', "---"), ('Y', 'Yes'), ('N', 'No'))

    details = forms.CharField(label="Have you had a genetic test for myotonic dystrophy", required=False, widget=Select(choices=YESNO_CHOICES))
    counselling = forms.CharField(label="Have you received genetic counselling", required=False, widget=Select(choices=YESNO_CHOICES))
    familycounselling = forms.CharField(label="Has any of your family members received genetic counselling", required=False, widget=Select(choices=YESNO_CHOICES))

    class Meta:
        exclude = ("diagnosis", "laboratory")
        model = models.GeneticTestDetails
        widgets = {
            "test_date": LubricatedDateWidget(years=-10),
        }


class EthnicOriginForm(forms.ModelForm):
    ORIGIN_CHOICES = (('', "-------"),) + base.EthnicOrigin.ORIGIN_CHOICES

    ethnic_origin = forms.CharField(label="How would you describe your ethnic origin", required=False, widget=Select(choices=ORIGIN_CHOICES))

    class Meta:
        exclude = ("diagnosis",)
        model = models.EthnicOrigin


class ClinicalTrialsForm(forms.ModelForm):
    class Meta:
        exclude = ("diagnosis",)
        model = models.ClinicalTrials


class PatientForm(forms.ModelForm):
    email = forms.EmailField(required=False)
    SEX_CHOICES = (('', "-------"),) + models.Patient.SEX_CHOICES
    sex = forms.CharField(required=False, widget=Select(choices=SEX_CHOICES))

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

class FamilyMemberForm(forms.ModelForm):
    class Meta:
        exclude = ("diagnosis",)
        model = models.FamilyMember
