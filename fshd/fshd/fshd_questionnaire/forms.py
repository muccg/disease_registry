from django import forms
from django.conf import settings
from django.forms.widgets import Select, RadioSelect
from registry.forms.date import DateWidget
from registry.patients.models import Patient as RegistryPatient
from registry.utils import stripspaces

import models
from fshd.fshd import base
from models import Patient as FshdPatient


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

class ClinicalFeaturesForm(forms.ModelForm): 
    class Meta:
        exclude = ("diagnosis")
        model = models.ClinicalFeatures

class PregnancyForm(forms.ModelForm): 
    class Meta:
        exclude = ("diagnosis",)
        model = models.Pregnancy


class HeartForm(forms.ModelForm):
    HEART_CHOICES = (('', "-------"),) + base.Heart.HEART_CHOICES
    YN_CHOICES = (('', "---"),) + base.Heart.YN_CHOICES

    condition = forms.CharField(label="Do you have a heart condition", required=False, widget=Select(choices=HEART_CHOICES))
    age_at_diagnosis = forms.IntegerField(label='At what age were you diagnosed with a heart condition', required=False, max_value=120, min_value=0)

    # Trac 16 FSHD Questionnaire Item 35, new fields
    # TODO: implement in Base.model to map them to Registry
    racing = forms.CharField(label="Do you experience: your heart racing or beating irregularly", widget=Select(choices=YN_CHOICES), required=False)
    palpitations = forms.CharField(label="heart palpitations", widget=Select(choices=YN_CHOICES), required=False)
    fainting = forms.CharField(label="black-outs or fainting", widget=Select(choices=YN_CHOICES), required=False)

    class Meta:
        exclude = ('diagnosis', 'ecg', 'ecg_sinus_rhythm', 'ecg_pr_interval', 'ecg_qrs_duration', 'ecg_examination_date',
                   'echocardiogram', 'echocardiogram_lvef', 'echocardiogram_lvef_date')
        model = models.Heart


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




class GeneticTestDetailsForm(forms.ModelForm):
    YESNO_CHOICES = (('', "---"), ('Y', 'Yes'), ('N', 'No'))

    details = forms.CharField(label="Have you had a genetic test for facioscapulohumeral muscular dystrophy", required=False, widget=Select(choices=YESNO_CHOICES))
    counselling = forms.CharField(label="Have you received genetic counselling", required=False, widget=Select(choices=YESNO_CHOICES))
    familycounselling = forms.CharField(label="Has any of your family members received genetic counselling", required=False, widget=Select(choices=YESNO_CHOICES))

    class Meta:
        exclude = ("diagnosis", "laboratory")
        model = models.GeneticTestDetails
        widgets = {
            "test_date": DateWidget(years=-10),
        }


class EthnicOriginForm(forms.ModelForm):
    ORIGIN_CHOICES = (('', "-------"),) + base.EthnicOrigin.ORIGIN_CHOICES

    ethnic_origin = forms.CharField(label="How would you describe your ethnic origin", required=False, widget=Select(choices=ORIGIN_CHOICES))

    class Meta:
        exclude = ("diagnosis",)
        model = models.EthnicOrigin


class PatientForm(forms.ModelForm):
    email = forms.EmailField(required=False)
    SEX_CHOICES = (('', "-------"),) + models.Patient.SEX_CHOICES
    sex = forms.CharField(required=False, widget=Select(choices=SEX_CHOICES))

    class Meta:
        model = models.Patient
        #model = FshdPatient  # The one for Fshd registry and questionnaire with a Male/Female choice, without the Intersex option

        widgets = {
            "date_of_birth": DateWidget(years=-100),
            "address": forms.Textarea(attrs={"cols": 60, "rows": 3}),
        }

    # add check on uniqueness in the fshd_questionnaire.patients table and registry.patients as well
    def clean(self):
        '''
        Prevents saving a patient if there is an existing one with the same family name, given names in the same working group
        in both the FSHD questionnaire patient table and the Registry patient table
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

        workinggroup = cleaneddata.get('working_group')

        #print "familyname: %s givennames %s workinggroup %s" % (familyname, givennames, workinggroup)

        fshdpatients = FshdPatient.objects.filter(family_name__iexact=familyname, given_names__iexact=givennames, working_group=workinggroup)
        #print "fshdpatients: %s" % fshdpatients

        registrypatients = RegistryPatient.objects.filter(family_name__iexact=familyname, given_names__iexact=givennames, working_group=workinggroup)
        #print "registrypatients: %s" % registrypatients

        if len(fshdpatients) > 0 or len(registrypatients) > 0:
            #print "raise forms.ValidationError"
            raise forms.ValidationError('There is already a patient with the same family and given names in this working group: "%s %s %s".' % (familyname, givennames, workinggroup))
        return cleaneddata

class FamilyMemberForm(forms.ModelForm):
    class Meta:
        exclude = ("diagnosis",)
        model = models.FamilyMember

class OtherRegistriesForm(forms.ModelForm):
    class Meta:
        exclude = ("diagnosis",)
        model = models.OtherRegistries
