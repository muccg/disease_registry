# vim: set fileencoding=UTF-8:
from django import forms
from django.utils.webhelpers import url
from models import *
from registry.forms.widgets import ComboWidget, LiveComboWidget, LubricatedDateWidget, StaticWidget, PercentageWidget

from utils.stripspaces import stripspaces

# This is a straight copy of dm1.admin_forms at the moment. It would probably
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

        # This is ugly, but required to avoid clobbering the help text and
        # custom verbose name, which is what happens if you just override the
        # field by setting a property on the class the way the Django
        # documentation suggests.
        self.fields["fvc"].widget = PercentageWidget()
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
    test_date = forms.DateField(label="Test Date", widget=LubricatedDateWidget(popup=True, today=True, years=-20))

# FJ added for uniqueness check family_name, given_names, working_group
class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient

    # Added to ensure unique (familyname, givennames, workinggroup)
    # Does not need a unique constraint on the DB

    def clean(self):
        cleaneddata = self.cleaned_data
        #print "PatientForm self %s" % dir(self)
        #print "cleaneddata: %s" % cleaneddata
        #print "instance %s" % self.instance.pk

        familyname = stripspaces(cleaneddata['family_name']).upper()
        givennames = stripspaces(cleaneddata['given_names'])
        workinggroup = cleaneddata['working_group']

        # show the names the way we'll store them
        cleaneddata['family_name'] = familyname
        cleaneddata['given_names'] = givennames

        #print "familyname: %s givennames %s workinggroup %s" % (familyname, givennames, workinggroup)

        if self.instance:
            id = self.instance.pk
        else:
            id = None

        patients = Patient.objects.filter(family_name__iexact=familyname, given_names__iexact=givennames, working_group=workinggroup)
        #print "Patients: %s" % patients

        exists = False
        if len(patients) > 0:
            if id == None: # creating a new patient and existing on ein the DB already
                exists = True
            elif id != patients[0].pk: # modifying an existing patient, check if there is another patient with same names but different pk
                exists = True
        if exists:
            raise forms.ValidationError('There is already a patient with the same family and given names in this working group: "%s %s %s".' % (familyname, givennames, workinggroup))
        return cleaneddata
