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


class RespiratoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RespiratoryForm, self).__init__(*args, **kwargs)

        # This is ugly, but required to avoid clobbering the help text and
        # custom verbose name, which is what happens if you just override the
        # field by setting a property on the class the way the Django
        # documentation suggests.
        self.fields["fvc"].widget = FVCPercentageWidget()
        self.fields["fvc_date"].widget=LubricatedDateWidget(popup=True, today=True, years=-5)

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
