from django.contrib import admin
from admin_forms import *
from models import *
from registry.utils import get_static_url
from registry import groups

class MotorFunctionInline(admin.StackedInline):
    model = MotorFunction
    form = MotorFunctionForm

class ClinicalFeaturesInline(admin.StackedInline):
    model = ClinicalFeatures
    form = ClinicalFeaturesForm

class RespiratoryInline(admin.StackedInline):
    form = RespiratoryForm
    model = Respiratory

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
    #change_form_template = "templates/admin/fshd/diagnosis.html"
    form = DiagnosisForm
    inlines = [
        GeneticTestDetailsInline,
        ClinicalFeaturesInline,
        MotorFunctionInline,
        RespiratoryInline,
        FamilyMemberInline,
        EthnicOriginInline,
        OtherRegistriesInline,
        NotesInline,
        ConsentInline, # do not display the consent form in the Registry, but needs to be validated and saved
    ]
    search_fields = ["patient__family_name", "patient__given_names"]
    fields = ('patient', 'age_at_clinical_diagnosis', 'age_at_molecular_diagnosis')
    list_display = ['patient_name', 'patient_working_group', 'progress_graph']
    save_on_top = True

    def patient_name(self, obj):
        return ("%s") % (obj.patient, )

    def patient_working_group(self, obj):
        return ("%s") % (obj.patient.working_group, )

    patient_name.short_description = 'Name'
    patient_working_group.short_description = 'Working Group'

    class Media:
        css = {
            "screen": [get_static_url("css/diagnosis_admin.css")]
        }

    def queryset(self, request):
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

    def progress_graph(self, obj):
        return obj.progress_graph()

    progress_graph.allow_tags = True
    progress_graph.short_description = "Diagnosis Entry Progress"


# Defined but not used here: this needs to be available for genetic.admin.
class DiagnosticCategoryInline(admin.StackedInline):
    max_num = 1
    model = DiagnosticCategory

    # Ordinarily I'd use a custom form template here rather than hooking
    # entirely in via JavaScript, but Mango issue #29 prevents that at present.
    class Media:
        js = [get_static_url("fshd/diagnostic-category.js")]


admin.site.register(Diagnosis, DiagnosisAdmin)


