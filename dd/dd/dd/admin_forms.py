from django import forms
from models import *
from registry.forms.widgets import ComboWidget, LiveComboWidget, StaticWidget, FVCPercentageWidget, PercentageWidget
from registry.forms.date import DateWidget

from django.forms import Select
from django.forms.models import modelformset_factory, inlineformset_factory
from django.forms.widgets import RadioSelect

class DDMedicalHistoryForm(forms.ModelForm):
        def __init__(self, *args, **kwargs):
            super(DDMedicalHistoryForm, self).__init__(*args, **kwargs)

        class Meta:
            model = DDMedicalHistoryRecord
            widgets = {
                    "other" : forms.Textarea(attrs={"cols":60, "rows":3}),
            }

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
