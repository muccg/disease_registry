from django import forms
from ccg.utils.webhelpers import url
from models import *
from ccg.django.registryforms.widgets import ComboWidget, LiveComboWidget, LubricatedDateWidget, StaticWidget, PercentageWidget


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
        self.fields["fvc"].widget = PercentageWidget()
        self.fields["fvc_date"].widget=LubricatedDateWidget(popup=True, today=True, years=-5)

    class Meta:
        model = Respiratory
