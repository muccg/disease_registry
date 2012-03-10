from django import forms
from ccg.utils.webhelpers import url
from models import *
from registry.forms.widgets import ComboWidget, LiveComboWidget, LubricatedDateWidget, StaticWidget, FVCPercentageWidget, PercentageWidget

from django.forms import Select
from django.forms.widgets import RadioSelect

class DiagnosisForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DiagnosisForm, self).__init__(*args, **kwargs)

        # make the patient field static if not a new diagnosis
        # otherwise limit choices of patients to working group if not superuser
        if "instance" in kwargs:
            self.fields["patient"] = forms.ModelChoiceField(Patient.objects.all(), widget=StaticWidget(text=unicode(kwargs["instance"])))
        else:
            import groups.models
            user = groups.models.User.objects.get(user=self.user)
            if self.user.is_superuser:
                self.fields["patient"] = forms.ModelChoiceField(Patient.objects.all())
            else:
                self.fields["patient"] = forms.ModelChoiceField(Patient.objects.filter(working_group=user.working_group).filter(active=True))

    class Meta:
        model = Diagnosis
        # Trac 16 Item 45, use Radio buttons for diagnosis
        #widgets = { 'diagnosis': RadioSelect( choices = (('DM1', 'DM1'), ('DM2', 'DM2'), ('O','Other')) ) }
        widgets = { 'diagnosis': RadioSelect( choices = Diagnosis.DIAGNOSIS_CHOICES ) }

class FamilyMemberForm(forms.ModelForm):
    OPTIONS = [
        "Parent",
        "Sibling",
        "Grandparent",
        "Uncle/Aunt",
        "Cousin",
        "Child",
    ]
    registry_patient = forms.ModelChoiceField(queryset=Patient.objects.all(), label="Patient record within the registry (optional)", required=False, widget=LiveComboWidget(attrs={"minchars": 1}, backend=url("/admin/patients/patient/search/")))
    relationship = forms.CharField(label="Relationship", widget=ComboWidget(options=OPTIONS))

    class Meta:
        model = FamilyMember

from datetime import date
def calculateage(birthday):
        today = date.today()
        y = today.year - birthday.year
        if today.month < birthday.month or today.month == birthday.month and today.day < birthday.day:
            y -= 1
        return y

def calculatefvcci(dateofbirth, height, weight, sex):

    if not dateofbirth or not height or not weight or not sex: return ('','')

    male = female = False
    if sex == 'M': male = True
    elif sex == 'F': female = True
    age = calculateage(dateofbirth)


    #if male and less than or equal to 7 years of age then do not predict
    if male and age <= 7: return ("","")

    #If male and between 8 and  19 years of age
    #      then FVC Eqn: -0.2584-0.20415*AGE+0.010133*AGE^2+0.00018642*HEIGHT_CM^2
    #and        CI Eqn: (0.00018642 - 0.00015695)*HEIGHT_CM^2

    if male and 8 <= age <=19:
        fvc = -0.2584 - (0.20415 * age) + (0.010133 * (age**2)) + (0.00018642 * (height**2))
        ci = (0.00018642 - 0.00015695) * height**2
        return (fvc, ci)

    #If male and 20 years or over
    #then Eqn: -0.1933+0.00064*AGE-0.000269*AGE^2+0.00018642*HEIGHT_CM^2
    #and CI Eqn: (0.00018642 - 0.00015695)*HEIGHT_CM^2

    if male and 20 <= age:
        fvc = -0.1933 + (0.00064 * age) - (0.000269 * (age**2)) + (0.00018642 * (height**2))
        ci = (0.00018642 - 0.00015695)* (height**2)
        return (fvc, ci)


    #If female and less than or equal to 7 years of age then do not predict
    if female and age <= 7: return ("","")


    #If female and between and between 8 and 17 years of age then
    #FVC Eqn: -1.2082+0.05916*AGE+0.00014815*HEIGHT_CM^2 and
    #CI (0.00014815 - 0.00012198)*HEIGHT_CM^2
    if female and 8 <= age <= 17:
        fvc = -1.2082 + (0.05916 * age) + (0.00014815 * (height**2))
        ci = (0.00014815 - 0.00012198) * (height**2)
        return (fvc, ci)

    #If female and 18 years or over then
    #FVC Eqn: -0.3560+0.01870*AGE-0.000382*AGE^2+0.00014815*HEIGHT_CM^2
    #And CI Eqn: (0.00014815 - 0.00012198)*HEIGHT_CM^2
    if female and 18 <= age:
        fvc = -0.3560 + (0.01870 * age) - (0.000382 * (age**2)) + (0.00014815 * (height**2))
        ci = (0.00014815 - 0.00012198) * (height**2)
        return (fvc, ci)

    # for cases not handled
    return ("","")

class RespiratoryForm(forms.ModelForm):
    #predictedfvc = forms.DecimalField(label='Predicted FVC', required=False, min_value=0, max_value=100, max_digits=5, decimal_places=2, widget = FVCPercentageWidget(attrs={'readonly': 'readonly'}))
    #predictedfvc = forms.DecimalField(label='Predicted FVC', required=False, min_value=0, max_value=100, max_digits=5, decimal_places=2, widget = FVCPercentageWidget())
    #fvc = forms.DecimalField(label='Measured FVC', required=False, min_value=0, max_value=100, max_digits=5, decimal_places=2, widget = FVCPercentageWidget(attrs={'size':'6', 'maxlength': '6'}))
    #fvc = forms.DecimalField(label='Measured FVC', required=False, min_value=0, max_value=100, max_digits=5, decimal_places=2)
    predictedfvc = forms.DecimalField(label='Predicted FVC', required=False, min_value=0, max_value=100, max_digits=5, decimal_places=2,
                        widget = PercentageWidget(attrs={'readonly': 'readonly', 'size': '6'}), help_text="forced vital capacity (FVC, expressed as % of normal, predicted by height, age and sex according to NHANES III formulae for Caucasians).")
    ci = forms.DecimalField(label='Confidence interval', required=False, min_value=0, max_value=100, max_digits=5, decimal_places=2,
                        widget = forms.TextInput(attrs={'readonly': 'readonly', 'size': '6'}))

    def __init__(self, *args, **kwargs):
        super(RespiratoryForm, self).__init__(*args, **kwargs)

        # This is ugly, but required to avoid clobbering the help text and
        # custom verbose name, which is what happens if you just override the
        # field by setting a property on the class the way the Django
        # documentation suggests.
        #self.fields["fvc"].widget = FVCPercentageWidget()
        self.fields["fvc_date"].widget=LubricatedDateWidget(popup=True, today=True, years=-5)

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

    class Meta:
        model = Respiratory

class HeartForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(HeartForm, self).__init__(*args, **kwargs)

        # This is ugly, but required to avoid clobbering the help text and
        # custom verbose name, which is what happens if you just override the
        # field by setting a property on the class the way the Django
        # documentation suggests.
        self.fields["echocardiogram_lvef"].widget = PercentageWidget()
        self.fields["ecg_examination_date"].widget=LubricatedDateWidget(popup=True, today=True, years=-20)
        self.fields["echocardiogram_lvef_date"].widget=LubricatedDateWidget(popup=True, today=True, years=-5)

    class Meta:
        model = Heart


class GeneticTestDetailsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GeneticTestDetailsForm, self).__init__(*args, **kwargs)
        self.fields["test_date"].widget=LubricatedDateWidget(popup=True, today=True, years=-5, required=self.fields["test_date"].required)

    # the following code doesn't display the wodget properly, hence the code above
    #class Meta:
    #    model = GeneticTestDetails
    #    test_date = forms.DateField(label="Test Date", widget=LubricatedDateWidget(popup=True, today=True, years=-20, required=False))

#FJ added to change the checkbox to a select
class MotorFunctionForm(forms.ModelForm):
    class Meta:
        model = MotorFunction
        #FJ Trac 16 item 15 & 18, change checkbox to drop down with Yes, No
        # Trac 16 Item 44, use Radio buttons for Yes, No
        widgets = { 'walk': RadioSelect( choices = (('0', 'No'), ('1','Yes')) ),    # , attrs={'class':'radiochoices'} ),
                    'sit': RadioSelect( choices = (('0', 'No'), ('1','Yes')) )
                   }

#FJ added to change the checkbox to a select
class SurgeryForm(forms.ModelForm):
    class Meta:
        model = Surgery
        #FJ Trac 16 item 25, change checkbox to drop down with Yes, No
        widgets = { 'cataract_diagnosis': RadioSelect( choices = (('0', 'No'), ('1','Yes')) ) }

# cannot get this form to work, it looks like it is not called by Django, cannot override the choices here
class GeneralMedicalFactorsForm(forms.ModelForm):
    class Meta:
        model = GeneralMedicalFactors
        widgets = { 'cancer': Select( choices = (('0', 'No'), ('1','Yes')) ) }

'''
# Could not register this form, already done in pateints/admin.py
#FJ added to limit the sex choices to Male/Female and remove Intersex
# Could not do it in dm1/Patient, some relationships point directly to the patients/models.Patient
# need to add this form in admin.py
class PatientForm(forms.ModelForm):
    class Meta:
        SEX_CHOICES = ( ("M", "Male"), ("F", "Female") )
        model = Patient
        #FJ Trac 16 item 9, change in the DM1 Registry Admin
        #widgets = { 'sex': Select( choices = (("M", "Male"), ("F", "Female")) ) }
        sex = models.CharField(max_length=1, choices=SEX_CHOICES)
'''
