# vim: set fileencoding=UTF-8:
from django import forms
from models import *
from registry.forms.widgets import ComboWidget, LiveComboWidget, StaticWidget, PercentageWidget
from registry.forms.date import DateWidget

from registry.utils import stripspaces

# This is a straight copy of fshd.admin_forms at the moment. It would probably
# be sensible to refactor this à la the models at some point.


class DiagnosisForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DiagnosisForm, self).__init__(*args, **kwargs)
        # make the patient field static if not a new diagnosis
        if "instance" in kwargs:
            self.fields["patient"] = forms.ModelChoiceField(Patient.objects.all(), widget=StaticWidget(text=unicode(kwargs["instance"])))

    class Meta:
        model = Diagnosis


class RespiratoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RespiratoryForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Respiratory


class HeartForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(HeartForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Heart


class GeneticTestDetailsForm(forms.ModelForm):
    pass

# FJ added for uniqueness check family_name, given_names, working_group
class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient

    # Added to ensure unique (familyname, givennames, workinggroup)
    # Does not need a unique constraint on the DB

    def clean(self):
        cleaneddata = self.cleaned_data

        # Trac #62 : key error when no data
        fname = cleaneddata.get('family_name')
        gname = cleaneddata.get('given_names')
        workinggroup = cleaneddata.get('working_group')
        if not fname or not gname or not workinggroup:
            raise forms.ValidationError('Missing either family name, given names or working group')

        familyname = stripspaces(cleaneddata['family_name']).upper()
        givennames = stripspaces(cleaneddata['given_names'])

        # show the names the way we'll store them
        cleaneddata['family_name'] = familyname
        cleaneddata['given_names'] = givennames

        if self.instance:
            id = self.instance.pk
        else:
            id = None

        patients = Patient.objects.filter(family_name__iexact=familyname, given_names__iexact=givennames, working_group=workinggroup)
        exists = False
        if len(patients) > 0:
            if id == None: # creating a new patient and existing on ein the DB already
                exists = True
            elif id != patients[0].pk: # modifying an existing patient, check if there is another patient with same names but different pk
                exists = True
        if exists:
            raise forms.ValidationError('There is already a patient with the same family and given names in this working group: "%s %s %s".' % (familyname, givennames, workinggroup))
        return cleaneddata
