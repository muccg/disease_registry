from django import forms
from models import *
from registry.forms.widgets import ComboWidget, LiveComboWidget, StaticWidget, FVCPercentageWidget, PercentageWidget
from registry.forms.date import DateWidget

from django.forms import Select
from django.forms.models import modelformset_factory, inlineformset_factory
from django.forms.widgets import RadioSelect

class ClinicalDataForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClinicalDataForm, self).__init__(*args, **kwargs)
    
    class Meta:
        model = DDClinicalData
        widgets = {
            'edss_evaluation_type': forms.RadioSelect()
        }

class DDMedicalHistoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DDMedicalHistoryForm, self).__init__(*args, **kwargs)

    class Meta:
        model = DDMedicalHistoryRecord
        widgets = {
                "other" : forms.Textarea(attrs={"cols":30, "rows":4}),
        }

class DDDiagnosisForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DDDiagnosisForm, self).__init__(*args, **kwargs)
        
        if "instance" in kwargs:
            self.fields["patient"] = forms.ModelChoiceField(Patient.objects.all(), widget=StaticWidget(text=unicode(kwargs["instance"])))
        else:
            import registry.groups.models
            user = registry.groups.models.User.objects.get(user=self.user)
            if self.user.is_superuser:
                self.fields["patient"] = forms.ModelChoiceField(Patient.objects.all())
            else:
                self.fields["patient"] = forms.ModelChoiceField(Patient.objects.filter(working_group=user.working_group).filter(active=True))

LabDataFormset = inlineformset_factory(LabData, LabDataRecord, extra=0, can_delete=False)
class DDLabDataForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        print 'ddlabdataform inited'
        super(DDLabDataForm, self).__init__(*args, **kwargs)
        self.labdatarecord_formset = LabDataFormset(instance = self.instance, data = self.data or None, prefix = self.prefix)
    def is_valid(self):
        return (super(DDLabDataForm, self).is_valid() and self.labdatarecord_formset.is_valid() )

    def save(self, commit = True):
        assert commit == True
        res = super(DDLabDataForm, self).save(commit=commit)
        self.labdararecord_formset.save()
        return res


class TreatmentCourseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TreatmentCourseForm, self).__init__(*args, **kwargs)

    class Meta:
        CHOICES = [
            ('S','Standard'),
            ('O','Other')
        ]

        model = TreatmentCourse
        widgets = {
            'dose_other': forms.Textarea(attrs={"cols": 35, "rows": 5}),
            'notes': forms.Textarea(attrs={"cols": 35, "rows": 5}),
            'dose_type': forms.RadioSelect(choices=CHOICES)
        }