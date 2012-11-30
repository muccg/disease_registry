from django import forms
from ccg.utils.webhelpers import url
from models import *
from registry.forms.widgets import ComboWidget, LubricatedDateWidget

from registry.utils.stripspaces import stripspaces

class PatientDoctorForm(forms.ModelForm):
    OPTIONS = [
        "Primary Care",
        "Paediatric Neurologist",
        "Neurologist",
        "Geneticist",
        "Specialist",
    ]
    relationship = forms.CharField(label="Relationship", widget=ComboWidget(options=OPTIONS))

    class Meta:
        model = PatientDoctor


class PatientForm(forms.ModelForm):
    ADDRESS_ATTRS = {
        "rows": 3,
        "cols": 30,
    }

    consent = forms.BooleanField(required=True, help_text="Consent must be given for the patient to be entered on the registry", label="Consent given")
    date_of_birth = forms.DateField(widget=LubricatedDateWidget(format="%d %B %Y", popup=True, years=-30))
    address = forms.CharField(widget=forms.Textarea(attrs=ADDRESS_ATTRS))
    next_of_kin_address = forms.CharField(widget=forms.Textarea(attrs=ADDRESS_ATTRS))

    class Media:
        js = [url("/static/js/patient.js")]

    class Meta:
        model = Patient

    # Added to ensure unique (familyname, givennames, workinggroup)
    # Does not need a unique constraint on the DB

    def clean(self):
        cleaneddata = self.cleaned_data
        #print "PatientForm self %s" % dir(self)
        print "cleaneddata: %s" % cleaneddata
        #print "instance %s" % self.instance.pk

        family_name = cleaneddata.get('family_name')
        if family_name:
            familyname = stripspaces(family_name).upper()

        givennames = cleaneddata.get('given_names')
        if givennames:
            givennames = stripspaces(givennames)

        # working_group can be None, which is annoying for the db query below
        # so working_group should be required, but how do we make it required in the model?
        # working_group = models.ForeignKey(groups.models.WorkingGroup)
        workinggroup = cleaneddata.get('working_group')
        if not workinggroup:
            raise forms.ValidationError('The working group is required.')
        #print "familyname: %s givennames %s workinggroup %s" % (familyname, givennames, workinggroup)

        if self.instance:
            id = self.instance.pk
        else:
            id = None
        print "PatientForm.clean: familyname: %s, givennames: %s, workinggroup: %s" % (familyname, givennames, workinggroup)
        patients = Patient.objects.filter(family_name__iexact=familyname, given_names__iexact=givennames, working_group=workinggroup)
        #print "Patients: %s" % patients

        exists = False
        if len(patients) > 0:
            if id == None: # creating a new patient and existing one in the DB already
                exists = True
            elif id != patients[0].pk: # modifying an existing patient, check if there is another patient with same names but different pk
                exists = True
        if exists:
            raise forms.ValidationError('There is already a patient with the same family and given names in this working group: "%s %s %s".' % (familyname, givennames, workinggroup))
        return cleaneddata
