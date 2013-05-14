from django import forms
from models import *
from registry.forms.widgets import ComboWidget, LiveComboWidget, StaticWidget, FVCPercentageWidget, PercentageWidget
from registry.forms.date import DateWidget

from django.forms import Select
from django.forms.models import modelformset_factory, inlineformset_factory
from registry.forms.widgets import NoDotsRadioSelect

class ClinicalDataForm(forms.ModelForm):
    class Meta:
        model = DDClinicalData
        widgets = {
            'edss_evaluation_type': NoDotsRadioSelect()
        }

class MedicalHistoryForm(forms.ModelForm):
    class Meta:
        model = MedicalHistory
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

    class Media:
        js = ("js/min_extra.js",)

class TreatmentCourseForm(forms.ModelForm):
    class Meta:
        model = TreatmentCourse
        widgets = {
            'dose_other': forms.Textarea(attrs={"cols": 35, "rows": 5}),
            'notes': forms.Textarea(attrs={"cols": 35, "rows": 5}),
            'dose_type': NoDotsRadioSelect()
        }

class MRIDataForm(forms.ModelForm):
    """
    This form is for the inline MRIData admin. It allows uploading a
    single image file through the image_file field. image_file is
    mapped to a MRIFile object which refers to MRIData.
    """
    class Meta:
        model = MRIData
        widgets = {
                "location" : forms.Textarea(attrs={"cols":30, "rows":3}),
        }

    def __init__(self, instance=None, *args, **kwargs):
        kwargs["instance"] = instance
        super(MRIDataForm, self).__init__(*args, **kwargs)

        # Initialize image_field field with last object in the
        # instance images set.
        if instance:
            images = instance.images.all()
            if len(images) > 0:
                image = images[len(images) - 1].image
                self.fields["image_file"].initial = image

    def save(self, commit=True):
        instance = super(MRIDataForm, self).save(commit)
        instance.save()

        if "image_file" in self.cleaned_data:
            image = self.cleaned_data["image_file"]
            if image:
                # If an image file is uploaded, add it on to the end
                # of the images set.
                mri = MRIFile(data=instance, image=image)
                mri.save()
            elif image is False:
                # User selected "Clear" => delete the last object in
                # the instance images set.
                images = instance.images.all()
                if len(images) > 0:
                    images[len(images) - 1].delete()

        return instance

    image_file = forms.FileField(required=False)
