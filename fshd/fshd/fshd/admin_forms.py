from django import forms
from django.core.urlresolvers import reverse_lazy
from models import *
from registry.forms.widgets import ComboWidget, LiveComboWidget, StaticWidget, FVCPercentageWidget, PercentageWidget
from registry.forms.date import DateWidget

from django.forms import Select
from registry.forms.widgets import NoDotsRadioSelect as RadioSelect

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

class MotorFunctionForm(forms.ModelForm):
    best_function = forms.CharField(widget=RadioSelect(choices=base.MotorFunction.MOTOR_FUNCTION_CHOICES), required=False, label="What is the best motor function level the patient has achieved",
                        help_text="<b>Walking:</b> walking with or without help (orthoses or assistive device or human assistance), inside or outdoors<br/><b>Sitting independently</b>: able to maintain a sitting position on a chair or a wheelchair without support of upper limbs or leaning against the back of the chair")

    class Meta:
        model = MotorFunction
        widgets = { 'wheelchair_use': RadioSelect(choices = MotorFunction.WHEELCHAIR_USE_CHOICES),}

    def clean(self):
        cleaneddata = self.cleaned_data

        wheelchair_use = cleaneddata.get('wheelchair_use', None)
        wheelchair_usage_age = cleaneddata.get('wheelchair_usage_age', None)
        print "MotorFunctionForm clean: wheelchair_use '%s' wheelchair_usage_age '%s'" % (wheelchair_use, wheelchair_usage_age)

        if (wheelchair_use == "intermittent" or wheelchair_use == "permanent") and not wheelchair_usage_age:
            # see https://docs.djangoproject.com/en/1.2/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other
            self._errors["wheelchair_usage_age"] = self.error_class(["Please specify the age at start of wheelchair use"])
            self.fields["wheelchair_usage_age"].required=True

        return cleaneddata

class FamilyMemberForm(forms.ModelForm):
    
    relationship = forms.CharField(label="Relationship", widget=ComboWidget(options=base.FamilyMember.RELATIONSHIP_CHOICES))

    class Meta:
        model = FamilyMember


class RespiratoryForm(forms.ModelForm):
    non_invasive_ventilation = forms.CharField(label="Non invasive ventilation", widget=RadioSelect(choices=Respiratory.VENTILATION_CHOICES), required=False, help_text="Mechanical ventilation with nasal or bucal mask")
    invasive_ventilation = forms.CharField(label="Invasive ventilation", widget=RadioSelect(choices=Respiratory.VENTILATION_CHOICES), required=False, help_text="Mechanical ventilation with tracheostomy")

    def __init__(self, *args, **kwargs):
        super(RespiratoryForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Respiratory

class GeneticTestDetailsForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(GeneticTestDetailsForm, self).__init__(*args, **kwargs)
        self.fields["test_date"].widget=DateWidget(popup=True, today=True, years=-5, required=self.fields["test_date"].required)

    # the following code doesn't display the wodget properly, hence the code above
    class Meta:
        model = GeneticTestDetails

    def clean(self):
        cleaneddata = self.cleaned_data

        details = cleaneddata.get('details', None)
        test_date = cleaneddata.get('test_date', None)

        if details == 'Y' and not test_date:
            # see https://docs.djangoproject.com/en/1.2/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other
            self._errors["test_date"] = self.error_class(["Please enter the Genetic Test Date"])
            self.fields["test_date"].required=True
        return cleaneddata

class ClinicalFeaturesForm(forms.ModelForm):
    pass

class ConsentForm(forms.ModelForm):
    q1 = forms.CharField(widget=RadioSelect(choices=Consent.YES_NO_CHOICES), required=False, label='Do we have your permission to store your personal & clinical data in the Australasian National Facioscapulohumeral Muscular Dystrophy Registry and to transfer it (in a form identifiable only by a code) to the global TREAT-NMD registry in which it may be used for research and for the planning of clinical trials?')
    q2 = forms.CharField(widget=RadioSelect(choices=Consent.YES_NO_CHOICES), required=False, label='Do we have your permission to obtain your Facioscapulohumeral Muscular Dystrophy genetic test result from the relevant testing laboratory to store this information with your clinical and personal information in the Australasian National Myotonic  Dystrophy Registry and to transfer it (in a form identifiable only by a code) to the global TREAT-NMD registry where it may be used for research and for the planning of clinical trials?')
    q3 = forms.CharField(widget=RadioSelect(choices=Consent.YES_NO_CHOICES), required=False, label='If we receive information on TREAT-NMD projects or other information related to your disease which might be relevant to you, would you like to be informed about this?')
    q4 = forms.CharField(widget=RadioSelect(choices=Consent.YES_NO_CHOICES), required=False, label='If your doctor receives information about a clinical trial which you might be eligible for, would you like to be informed about this?')
    q5 = forms.CharField(widget=RadioSelect(choices=Consent.YES_NO_CHOICES), required=False, label='So that we can keep the registry up to date, we will need to update your records once a year. Do you agree to receive follow-up forms once a year which you will be asked to complete in order to register any changes in your medical condition or contact details?')
    q6 = forms.CharField(widget=RadioSelect(choices=Consent.YES_NO_CHOICES), required=False, label='To improve the quality of the family history data on the Registry, we propose to link your record to any other affected family member or relative on the Registry. The link will only show your Unique identification number and your relationship to the affected relative. Do you agree to have your record linked to any other affected relatives on the Registry?')
    q7 = forms.CharField(widget=RadioSelect(choices=Consent.YES_NO_CHOICES), required=False, label='If there are any major changes in your data (for example change of address or changes in your medical condition, such as loss of ability to walk unassisted) that occur in the period between updates, are you willing to inform us?')

    class Meta:
        model = Consent

