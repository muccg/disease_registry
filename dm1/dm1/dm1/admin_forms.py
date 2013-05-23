from django import forms
from django.core.urlresolvers import reverse_lazy
from models import *
from registry.forms.widgets import ComboWidget, LiveComboWidget, StaticWidget, FVCPercentageWidget, PercentageWidget
from registry.forms.date import DateWidget

from django.forms import Select
from registry.forms.widgets import NoDotsRadioSelect as RadioSelect
from registry.utils import get_working_groups

class DiagnosisForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DiagnosisForm, self).__init__(*args, **kwargs)

        # make the patient field static if not a new diagnosis
        # otherwise limit choices of patients to working group if not superuser
        if "instance" in kwargs:
            self.fields["patient"] = forms.ModelChoiceField(Patient.objects.all(), widget=StaticWidget(text=unicode(kwargs["instance"])))
        else:
            import registry.groups.models
            user = registry.groups.models.User.objects.get(user=self.user)
            if self.user.is_superuser:
                self.fields["patient"] = forms.ModelChoiceField(Patient.objects.all())
            else:
                self.fields["patient"] = forms.ModelChoiceField(Patient.objects.filter(working_group__in=get_working_groups(user)).filter(active=True))

    class Meta:
        model = Diagnosis
        widgets = { 'diagnosis': RadioSelect(choices = Diagnosis.DIAGNOSIS_CHOICES),
                    'affectedstatus': RadioSelect(choices=Diagnosis.AFFECTED_STATUS_CHOICES)
                }

class FamilyMemberForm(forms.ModelForm):
    OPTIONS = [
        "Parent",
        "Sibling",
        "Grandparent",
        "Uncle/Aunt",
        "Cousin",
        "Child",
    ]
    registry_patient = forms.ModelChoiceField(queryset=Patient.objects.all(), label="Patient record within the registry (optional)", required=False, widget=LiveComboWidget(attrs={"minchars": 1}, backend=reverse_lazy("admin:patient_search", args=("",))))
    relationship = forms.CharField(label="Relationship", widget=ComboWidget(options=OPTIONS))
    sex = forms.CharField(label="Sex", widget=RadioSelect(choices=Patient.SEX_CHOICES), required=False)
    family_member_diagnosis = forms.CharField(label="Diagnosis", widget=RadioSelect(choices=FamilyMember.DIAGNOSIS_CHOICES), required=False)

    class Meta:
        model = FamilyMember


class RespiratoryForm(forms.ModelForm):
    non_invasive_ventilation = forms.CharField(label="Non invasive ventilation", widget=RadioSelect(choices=Respiratory.VENTILATION_CHOICES), required=False, help_text="Mechanical ventilation with nasal or bucal mask")
    non_invasive_ventilation_type = forms.CharField(label="Non invasive ventilation type", widget=RadioSelect(choices=Respiratory.VENTILATION_TYPE_CHOICES), required=False)
    invasive_ventilation = forms.CharField(label="Invasive ventilation", widget=RadioSelect(choices=Respiratory.VENTILATION_CHOICES), required=False, help_text="Mechanical ventilation with tracheostomy")

    def __init__(self, *args, **kwargs):
        super(RespiratoryForm, self).__init__(*args, **kwargs)

        # This is ugly, but required to avoid clobbering the help text and
        # custom verbose name, which is what happens if you just override the
        # field by setting a property on the class the way the Django
        # documentation suggests.
        #self.fields["fvc"].widget = FVCPercentageWidget()
        self.fields["fvc_date"].widget=DateWidget(popup=True, today=True, years=-5)
        self.fields["calculatedfvc"].widget = PercentageWidget() # just to display the "%" symbol after the input field

        """
        # removed v3
        # Set the form fields based on the model object
        if kwargs.has_key('instance'):
            instance = kwargs['instance'] # dm1.models.Respiratory
            if not instance: return
            diagnosis = instance.diagnosis
            if not diagnosis: return
            patient = diagnosis.patient
            if not patient: return
            generalmedicalfactors = diagnosis.generalmedicalfactors
            if not generalmedicalfactors: return
            height = generalmedicalfactors.height
            if not height: return
            weight = generalmedicalfactors.weight
            if not weight: return
            dateofbirth = patient.date_of_birth
            if not dateofbirth: return
            sex = patient.sex
            if not sex: return

            fvc, ci = calculatefvcci(dateofbirth, height, weight, sex)
            self.initial['predictedfvc'] = "%.2f" % fvc
            self.initial['ci'] = "%.2f" % ci
        """

    class Meta:
        model = Respiratory

class HeartForm(forms.ModelForm):
    condition = forms.CharField(label="Heart condition", widget=RadioSelect(choices=Heart.HEART_CHOICES), required=False)
    racing = forms.CharField(label="Does the patient experience: heart racing or beating irregularly", widget=RadioSelect(choices=Heart.UYN_CHOICES), required=False)
    palpitations = forms.CharField(label="heart palpitations", widget=RadioSelect(choices=Heart.UYN_CHOICES), required=False)
    fainting = forms.CharField(label="black-outs or fainting", widget=RadioSelect(choices=Heart.UYN_CHOICES), required=False)
    ecg = forms.CharField(label="ECG", widget=RadioSelect(choices=Heart.UYN_CHOICES), required=False)
    ecg_sinus_rhythm = forms.CharField(label="ECG Sinus Rhythm", widget=RadioSelect(choices=Heart.UYN_CHOICES), required=False)
    echocardiogram = forms.CharField(label="Echocardiogram", widget=RadioSelect(choices=Heart.UYN_CHOICES), required=False)

    def __init__(self, *args, **kwargs):
        super(HeartForm, self).__init__(*args, **kwargs)

        # This is ugly, but required to avoid clobbering the help text and
        # custom verbose name, which is what happens if you just override the
        # field by setting a property on the class the way the Django
        # documentation suggests.
        self.fields["echocardiogram_lvef"].widget = PercentageWidget()
        self.fields["ecg_examination_date"].widget=DateWidget(popup=True, today=True, years=-20)
        self.fields["echocardiogram_lvef_date"].widget=DateWidget(popup=True, today=True, years=-5)

    class Meta:
        model = Heart

class GeneticTestDetailsForm(forms.ModelForm):
    details = forms.CharField(label="Are details of genetic testing available", widget=RadioSelect(choices=GeneticTestDetails.UYN_CHOICES))
    counselling = forms.CharField(label="Has the patient received genetic counselling", widget=RadioSelect(choices=GeneticTestDetails.UYN_CHOICES), required=False)
    familycounselling = forms.CharField(label="Has any of the patient's family members received genetic counselling", widget=RadioSelect(choices=GeneticTestDetails.UYN_CHOICES), required=False)

    def __init__(self, *args, **kwargs):
        super(GeneticTestDetailsForm, self).__init__(*args, **kwargs)

        widget = LiveComboWidget(attrs={"minchars": 0, "size": 60},
                                 backend=reverse_lazy("admin:laboratory_search", args=("",)))
        self.fields["laboratory"].widget = widget
        self.fields["test_date"].widget=DateWidget(popup=True, today=True, years=-5, required=self.fields["test_date"].required)

    # the following code doesn't display the wodget properly, hence the code above
    class Meta:
        model = GeneticTestDetails

    def clean(self):
        cleaneddata = self.cleaned_data

        details = cleaneddata.get('details', None)
        test_date = cleaneddata.get('test_date', None)

        if details == 'Y' and not test_date:
            # see https://docs.djangoproject.com/en/1.2/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other
            self._errors["test_date"] = self.error_class(["Please enter the Genetic Test Date"])
            self.fields["test_date"].required=True
        return cleaneddata

class DMTestDetailsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DMTestDetailsForm, self).__init__(*args, **kwargs)
        self.fields["repeat_sequence"].widget = forms.TextInput(attrs={"size": 20})
        self.fields["repeat_number"].widget = forms.TextInput(attrs={"size": 30})
        self.fields["region_targeted"].widget = forms.TextInput(attrs={"size": 20})
        self.fields["typing_method"].widget = forms.Textarea(attrs={"cols": 40, "rows": 3})

class MotorFunctionForm(forms.ModelForm):
    walk = forms.CharField(label="Currently able to walk", widget=RadioSelect(choices=base.MotorFunction.YN_CHOICES))
    best_function = forms.CharField(widget=RadioSelect(choices=base.MotorFunction.MOTOR_FUNCTION_CHOICES), required=False, label="What is the best motor function level the patient has achieved",
                        help_text="<b>Walking:</b> walking with or without help (orthoses or assistive device or human assistance), inside or outdoors<br/><b>Sitting independently</b>: able to maintain a sitting position on a chair or a wheelchair without support of upper limbs or leaning against the back of the chair")
    dysarthria = forms.IntegerField(widget=RadioSelect(choices=base.MotorFunction.DYSARTHRIA_CHOICES), required=False)

    class Meta:
        model = MotorFunction
        widgets = { 'walk_assisted': RadioSelect(choices = MotorFunction.WALK_ASSISTED_CHOICES),
                    'wheelchair_use': RadioSelect(choices = MotorFunction.WHEELCHAIR_USE_CHOICES),
                    'dysarthria': RadioSelect(choices = MotorFunction.DYSARTHRIA_CHOICES),
                }

    def clean(self):
        cleaneddata = self.cleaned_data

        wheelchair_use = cleaneddata.get('wheelchair_use', None)
        wheelchair_usage_age = cleaneddata.get('wheelchair_usage_age', None)
        print "MotorFunctionForm clean: wheelchair_use '%s' wheelchair_usage_age '%s'" % (wheelchair_use, wheelchair_usage_age)

        if (wheelchair_use == "intermittent" or wheelchair_use == "permanent") and not wheelchair_usage_age:
            # see https://docs.djangoproject.com/en/1.2/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other
            self._errors["wheelchair_usage_age"] = self.error_class(["Please specify the age at start of wheelchair use"])
            self.fields["wheelchair_usage_age"].required=True

        return cleaneddata


class SurgeryForm(forms.ModelForm):
    cardiac_implant = forms.CharField(label="cardiac implant", widget=RadioSelect(choices=Surgery.CARDIAC_IMPLANT_CHOICES), required=False)
    cataract = forms.CharField(label="cataract surgery", widget=RadioSelect(choices=Surgery.UYN_CHOICES), required=False)

    class Meta:
        model = Surgery
        widgets = { 'cataract_diagnosis': RadioSelect( choices = (('0', 'No'), ('1','Yes')) ) }

class GeneralMedicalFactorsForm(forms.ModelForm):
    diabetes = forms.CharField(label="Diabetes", widget=RadioSelect(choices=GeneralMedicalFactors.DIABETES_CHOICES), required=False)
    pneumonia = forms.CharField(label="Pneumonia", widget=RadioSelect(choices=GeneralMedicalFactors.YESNO_CHOICES), required=False)
    cancer = forms.CharField(label="Has the patient been diagnosed with cancer or a tumour", widget=RadioSelect(choices=GeneralMedicalFactors.YESNO_CHOICES), required=False, help_text='Please tick the check box if the patient has been diagnosed with or identifies as having any of the following')
    cancertype = forms.ModelMultipleChoiceField(label="if yes, please choose from the following options", queryset=base.CancerTypeChoices.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
    cognitive_impairment = forms.CharField(label="Cognitive impairment", widget=RadioSelect(choices=GeneralMedicalFactors.COGNITIVE_CHOICES), required=False)
    medicalert = forms.CharField(label="Does the patient wear a Medicalert bracelet", widget=RadioSelect(choices=GeneralMedicalFactors.UYN_CHOICES), required=False)
    physiotherapy = forms.CharField(label="Has the patient received any of the following: Physiotherapy", widget=RadioSelect(choices=GeneralMedicalFactors.UYN_CHOICES), required=False)
    psychologicalcounseling = forms.CharField(label="Emotional & psychological counseling", widget=RadioSelect(choices=GeneralMedicalFactors.UYN_CHOICES), required=False)
    speechtherapy = forms.CharField(label="Speech therapy", widget=RadioSelect(choices=GeneralMedicalFactors.UYN_CHOICES), required=False)
    occupationaltherapy = forms.CharField(label="Occupational therapy", widget=RadioSelect(choices=GeneralMedicalFactors.UYN_CHOICES), required=False)
    vocationaltraining = forms.CharField(label="Vocational rehabilitation", widget=RadioSelect(choices=GeneralMedicalFactors.UYN_CHOICES), required=False)

    class Meta:
        model = GeneralMedicalFactors
        widgets = { 'cancer': Select( choices = (('0', 'No'), ('1','Yes')) ) }


class ConsentForm(forms.ModelForm):
    q1 = forms.CharField(widget=RadioSelect(choices=Consent.YES_NO_CHOICES), required=False, label='Do we have your permission to store your personal & clinical data in the Australasian National Myotonic Dystrophy Registry and to transfer it (in a form identifiable only by a code) to the global TREAT-NMD registry in which it may be used for research and for the planning of clinical trials?')
    q2 = forms.CharField(widget=RadioSelect(choices=Consent.YES_NO_CHOICES), required=False, label='Do we have your permission to obtain your Myotonic Dystrophy genetic test result from the relevant testing laboratory to store this information with your clinical and personal information in the Australasian National Myotonic  Dystrophy Registry and to transfer it (in a form identifiable only by a code) to the global TREAT-NMD registry where it may be used for research and for the planning of clinical trials?')
    q3 = forms.CharField(widget=RadioSelect(choices=Consent.YES_NO_CHOICES), required=False, label='If we receive information on TREAT-NMD projects or other information related to your disease which might be relevant to you, would you like to be informed about this?')
    q4 = forms.CharField(widget=RadioSelect(choices=Consent.YES_NO_CHOICES), required=False, label='If your doctor receives information about a clinical trial which you might be eligible for, would you like to be informed about this?')
    q5 = forms.CharField(widget=RadioSelect(choices=Consent.YES_NO_CHOICES), required=False, label='So that we can keep the registry up to date, we will need to update your records once a year. Do you agree to receive follow-up forms once a year which you will be asked to complete in order to register any changes in your medical condition or contact details?')
    q6 = forms.CharField(widget=RadioSelect(choices=Consent.YES_NO_CHOICES), required=False, label='To improve the quality of the family history data on the Registry, we propose to link your record to any other affected family member or relative on the Registry. The link will only show your Unique identification number and your relationship to the affected relative. Do you agree to have your record linked to any other affected relatives on the Registry?')
    q7 = forms.CharField(widget=RadioSelect(choices=Consent.YES_NO_CHOICES), required=False, label='If there are any major changes in your data (for example change of address or changes in your medical condition, such as loss of ability to walk unassisted) that occur in the period between updates, are you willing to inform us?')

    class Meta:
        model = Consent


class FatigueForm(forms.ModelForm):
    fatigue = forms.CharField(label='Fatigue', widget=RadioSelect(choices=Fatigue.FATIGUE_CHOICES), required=False, help_text="Does fatigue or daytime sleepiness currently have a negative effect on the patient's normal daily activities")
    sitting_reading = forms.CharField(label='sitting and reading', widget=RadioSelect(choices=Fatigue.DOZING_CHOICES), required=False)
    watching_tv = forms.CharField(label='watching TV', widget=RadioSelect(choices=Fatigue.DOZING_CHOICES), required=False)
    sitting_inactive_public = forms.CharField(label='sitting, inactive, in a public place', widget=RadioSelect(choices=Fatigue.DOZING_CHOICES), required=False)
    passenger_car = forms.CharField(label='as a passenger in a car for an hour without a break', widget=RadioSelect(choices=Fatigue.DOZING_CHOICES), required=False)
    lying_down_afternoon = forms.CharField(label='lying down to rest in the afternoon when circumstances permit', widget=RadioSelect(choices=Fatigue.DOZING_CHOICES), required=False)
    sitting_talking = forms.CharField(label='sitting and talking to someone', widget=RadioSelect(choices=Fatigue.DOZING_CHOICES), required=False)
    sitting_quietly_lunch = forms.CharField(label='sitting quietly after lunch without alcohol', widget=RadioSelect(choices=Fatigue.DOZING_CHOICES), required=False)
    in_car = forms.CharField(label='in a car, while stopped for a few minutes in traffic', widget=RadioSelect(choices=Fatigue.DOZING_CHOICES), required=False)


class FatigueMedicationForm(forms.ModelForm):
    drug = forms.CharField(label='Drug', required=False, help_text="Specify each drug with its International Nonproprietary Name (INN)")
    status = forms.CharField(label='Status', widget=RadioSelect(choices=FatigueMedication.STATUS_CHOICES), required=False)

    class Meta:
        model = FatigueMedication


class MuscleForm(forms.ModelForm):
    myotonia = forms.CharField(label="Does myotonia currently have a negative effect on the patient's daily activities", widget=RadioSelect(choices=Muscle.MYOTONIA_CHOICES), required=False)

    flexor_digitorum_profundis = forms.CharField(label="Flexor digitorum profundis", widget=RadioSelect(choices=Muscle.MRC_CHOICES), required=False, help_text=Muscle.MRC_HELP_TEXT)
    tibialis_anterior = forms.CharField(label="Tibialis anterior", widget=RadioSelect(choices=Muscle.MRC_CHOICES), required=False)
    neck_flexion = forms.CharField(label="Neck flexion", widget=RadioSelect(choices=Muscle.MRC_CHOICES), required=False)
    iliopsoas = forms.CharField(label="iliopsoas", widget=RadioSelect(choices=Muscle.MRC_CHOICES), required=False)
    face = forms.CharField(label="Facial weakness", widget=RadioSelect(choices=Muscle.UYN_CHOICES), required=False)
    early_weakness = forms.CharField(label="Was there any evidence of hypotonia or weakness within the first four weeks", widget=RadioSelect(choices=Muscle.UYN_CHOICES), required=False)

    class Meta:
        model = Muscle


class FeedingFunctionForm(forms.ModelForm):
    dysphagia = forms.CharField(label='Dysphagia', required=False, help_text="Does the patient have difficulty swallowing", widget=RadioSelect(choices=FeedingFunction.UYN_CHOICES))
    gastric_nasal_tube = forms.CharField(label='Gastric nasal tube', required=False, help_text="Does the patient need nutritional supplementation via nasogastric or nasojejunal tube, or gastrostomy", widget=RadioSelect(choices=FeedingFunction.UYN_CHOICES))

    class Meta:
        model = FeedingFunction


class SocioeconomicFactorsForm(forms.ModelForm):
    occupation = forms.CharField(label='Occupation', required=False, widget=RadioSelect(choices=SocioeconomicFactors.OCCUPATION_CHOICES))
    employment_effect = forms.CharField(label="Has Myotonic dystrophy affected the patient's employment", required=False, widget=RadioSelect(choices=SocioeconomicFactors.EFFECT_CHOICES))

    class Meta:
        model = SocioeconomicFactors
