from django.contrib import admin
from ccg.utils.webhelpers import url
from admin_forms import *
from models import *
from base import CancerTypeChoices


class MotorFunctionInline(admin.StackedInline):
    model = MotorFunction
    form = MotorFunctionForm

class SurgeryInline(admin.StackedInline):
    model = Surgery
    form = SurgeryForm # FJ Trac 16 item 25, change checkbox to drop down with Yes, No

class RespiratoryInline(admin.StackedInline):
    form = RespiratoryForm
    model = Respiratory

class FeedingFunctionInline(admin.StackedInline):
    form = FeedingFunctionForm
    model = FeedingFunction

class ClinicalTrialsInline(admin.TabularInline):
    model = ClinicalTrials
    extra = 3

class HeartMedicationInline(admin.TabularInline):
    model = HeartMedication
    extra = 3

class HeartInline(admin.StackedInline):
    form = HeartForm
    model = Heart

class MuscleMedicationInline(admin.TabularInline):
    model = MuscleMedication
    extra = 3

class MuscleInline(admin.StackedInline):
    form = MuscleForm
    model = Muscle

class FatigueInline(admin.StackedInline):
    form = FatigueForm
    model = Fatigue

class FatigueMedicationInline(admin.TabularInline):
    form = FatigueMedicationForm
    model = FatigueMedication
    extra = 3

class SocioeconomicFactorsInline(admin.StackedInline):
    form = SocioeconomicFactorsForm
    model = SocioeconomicFactors

class GeneralMedicalFactorsInline(admin.StackedInline):
    form = GeneralMedicalFactorsForm   # can't get it to work, choices ignored
    model = GeneralMedicalFactors
    # TRAC #35, cancertype is displayed at the end of the form if 'fields' not specified, bummer
    fields = ('diabetes', 'diabetesage', 'pneumonia', 'pneumoniaage', 'pneumoniainfections', 'cancer', 'cancertype',
              'cancerothers', 'cancerorgan', 'liver', 'miscarriage', 'gor', 'gall_bladder', 'infection', 'sexual_dysfunction',
              'constipation', 'cholesterol', 'cognitive_impairment', 'psychological', 'anxiety', 'depression', 'apathy',
              'weight', 'height', 'endocrine', 'obgyn', 'medicalert', 'physiotherapy', 'psychologicalcounseling', 'speechtherapy',
              'occupationaltherapy', 'vocationaltraining')

class GeneticTestDetailsInline(admin.StackedInline):
    form = GeneticTestDetailsForm
    model = GeneticTestDetails

class EthnicOriginInline(admin.StackedInline):
    model = EthnicOrigin

class OtherRegistriesInline(admin.TabularInline):
    model = OtherRegistries
    extra = 3

class FamilyMemberInline(admin.TabularInline):
    form = FamilyMemberForm
    model = FamilyMember
    raw_id_fields = ("registry_patient",)
    extra = 3

class NotesInline(admin.TabularInline):
    model = Notes

class ConsentInline(admin.StackedInline):
    form = ConsentForm
    model = Consent

class DiagnosisAdmin(admin.ModelAdmin):
    actions = None
    #change_form_template = "templates/admin/dm1/diagnosis.html"
    form = DiagnosisForm
    inlines = [
        GeneticTestDetailsInline, # moved at the top of the form,Trac #16, Item 59
        MotorFunctionInline,
        MuscleInline,
        MuscleMedicationInline,
        SurgeryInline,
        HeartInline,
        HeartMedicationInline,
        RespiratoryInline,
        FeedingFunctionInline,
        FatigueInline,
        FatigueMedicationInline,
        SocioeconomicFactorsInline,
        GeneralMedicalFactorsInline,
        #GeneticTestDetailsInline, # moved at the top of the form,Trac #16, Item 59
        FamilyMemberInline,
        EthnicOriginInline,
        ClinicalTrialsInline,
        OtherRegistriesInline,
        NotesInline,
        ConsentInline, # do not display the consent form in the Registry, but needs to be validated and saved
    ]
    search_fields = ["patient__family_name", "patient__given_names"]
    # Trac #16 Item 10
    fields = ('patient', 'diagnosis', 'affectedstatus', 'first_symptom', 'first_suspected_by', 'age_at_clinical_diagnosis', 'age_at_molecular_diagnosis')
    # Trac #16 Item 10 end

    save_on_top = True

    class Media:
        css = {
            "screen": [url("/static/css/diagnosis_admin.css")]
        }

    def queryset(self, request):
        import registry.groups.models

        if request.user.is_superuser:
            return Diagnosis.objects.all()

        user = groups.models.User.objects.get(user=request.user)

        if self.has_change_permission(request):
            return Diagnosis.objects.filter(patient__working_group=user.working_group).filter(patient__active=True)
        else:
            return Diagnosis.objects.none()

    def get_form(self, request, obj=None, **kwargs):
        """
        We provide our own get_form so we can access the user object
        and narrow choice fields in the form by user rights
        """
        form = super(DiagnosisAdmin, self).get_form(request, obj, **kwargs)
        form.user = request.user
        return form


# Defined but not used here: this needs to be available for genetic.admin.
class DiagnosticCategoryInline(admin.StackedInline):
    max_num = 1
    model = DiagnosticCategory

    # Ordinarily I'd use a custom form template here rather than hooking
    # entirely in via JavaScript, but Mango issue #29 prevents that at present.
    class Media:
        js = [url("/static/dm1/diagnostic-category.js")]


admin.site.register(Diagnosis, DiagnosisAdmin)

# Trac 16 item 9, change in the DM1 Registry Admin
# FJ added to limit the sex choices to Male/Female and remove Intersex
# Could not do it in dm1/Patient, some relationships point directly to the patients/models.Patient
#class PatientAdmin(admin.ModelAdmin):
#    form = PatientForm

#admin.site.register(Patient, PatientAdmin)

#Trac #35
class CancerTypeChoicesAdmin(admin.ModelAdmin):
    search_fields = ["description"]

admin.site.register(CancerTypeChoices, CancerTypeChoicesAdmin)