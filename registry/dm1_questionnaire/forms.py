from django import forms
from django.forms.models import inlineformset_factory
from registry.forms.widgets import LubricatedDateWidget
import models

from django.forms import Select

from models import Patient as Dm1Patient
from patients.models import Patient as RegistryPatient

from utils.stripspaces import stripspaces

class ConsentForm(forms.Form):
    consent = forms.BooleanField(required=True)


class DiagnosisForm(forms.ModelForm):
    class Meta:
        exclude = ("patient",)
        model = models.Diagnosis


class MotorFunctionForm(forms.ModelForm):
    class Meta:
        exclude = ("diagnosis",)
        model = models.MotorFunction
        #FJ Trac 16 item 15, change checkbox to drop down with Yes, No
        widgets = { 'walk': Select( choices = (('0', 'No'), ('1','Yes')) ) }

class SurgeryForm(forms.ModelForm):
    class Meta:
        exclude = ("diagnosis",)
        model = models.Surgery


class HeartForm(forms.ModelForm):
    class Meta:
        exclude = ("diagnosis",)
        model = models.Heart


class HeartMedicationForm(forms.ModelForm):
    class Meta:
        exclude = ("diagnosis",)
        model = models.HeartMedication


class RespiratoryForm(forms.ModelForm):
    class Meta:
        exclude = ("diagnosis",)
        model = models.Respiratory


class MuscleForm(forms.ModelForm):
    class Meta:
        exclude = ("diagnosis",)
        model = models.Muscle


class MuscleMedicationForm(forms.ModelForm):
    class Meta:
        exclude = ("diagnosis",)
        model = models.MuscleMedication


class FeedingFunctionForm(forms.ModelForm):
    class Meta:
        exclude = ("diagnosis",)
        model = models.FeedingFunction


class FatigueForm(forms.ModelForm):
    class Meta:
        exclude = ("diagnosis",)
        model = models.Fatigue


class FatigueMedicationForm(forms.ModelForm):
    class Meta:
        exclude = ("diagnosis",)
        model = models.FatigueMedication


class SocioeconomicFactorsForm(forms.ModelForm):
    class Meta:
        exclude = ("diagnosis",)
        model = models.SocioeconomicFactors


class GeneralMedicalFactorsForm(forms.ModelForm):
    class Meta:
        exclude = ("diagnosis",)
        model = models.GeneralMedicalFactors


class GeneticTestDetailsForm(forms.ModelForm):
    class Meta:
        exclude = ("diagnosis",)
        model = models.GeneticTestDetails
        widgets = {
            "test_date": LubricatedDateWidget(years=-10),
        }


class EthnicOriginForm(forms.ModelForm):
    class Meta:
        exclude = ("diagnosis",)
        model = models.EthnicOrigin


class ClinicalTrialsForm(forms.ModelForm):
    class Meta:
        exclude = ("diagnosis",)
        model = models.ClinicalTrials


class PatientForm(forms.ModelForm):
    email = forms.EmailField(required=True)

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
    