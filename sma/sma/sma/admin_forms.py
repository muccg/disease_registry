from django import forms
from django.core.urlresolvers import reverse_lazy
from models import *
from registry.forms.widgets import ComboWidget, LiveComboWidget, StaticWidget, PercentageWidget
from registry.forms.date import DateWidget

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
    registry_patient = forms.ModelChoiceField(queryset=Patient.objects.all(), label="Patient record within the registry (optional)", required=False, widget=LiveComboWidget(attrs={"minchars": 1}, backend=reverse_lazy("admin:patient_search", args=("",))))
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
        self.fields["fvc_date"].widget=DateWidget(popup=True, today=True, years=-5)

    class Meta:
        model = Respiratory
