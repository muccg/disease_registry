from django.contrib import admin
from admin_forms import *
from models import *
from registry.groups.models import User as RegistryUser
from registry import groups
from registry.utils import get_static_url

class MotorFunctionInline(admin.StackedInline):
    model = MotorFunction


class SteroidsInline(admin.StackedInline):
    model = Steroids


class SurgeryInline(admin.StackedInline):
    model = Surgery


class HeartMedicationInline(admin.TabularInline):
    model = HeartMedication
    extra = 3


class HeartInline(admin.StackedInline):
    form = HeartForm
    model = Heart


class RespiratoryInline(admin.StackedInline):
    form = RespiratoryForm
    model = Respiratory


class ClinicalTrialsInline(admin.TabularInline):
    model = ClinicalTrials
    extra = 3


class OtherRegistriesInline(admin.TabularInline):
    model = OtherRegistries
    extra = 3


class FamilyMemberInline(admin.TabularInline):
    form = FamilyMemberForm
    model = FamilyMember
    # doesn't look like it's doing anything
    # raw_id_fields = ("registry_patient",)
    extra = 3

    def formfield_for_foreignkey(self, db_field, request, **kwargs):

        # if not a super user then restrict the patients that show up in the family inline patient dropdown
        if not request.user.is_superuser:
            user = RegistryUser.objects.get(user=request.user)

            if db_field.name == "registry_patient":
                kwargs["queryset"] = Patient.objects.filter(working_group=user.working_group)

        return super(FamilyMemberInline, self).formfield_for_foreignkey(db_field, request, **kwargs)


class NotesInline(admin.TabularInline):
    model = Notes


class OrphaThesaurusAdmin(admin.ModelAdmin):
    form = OrphaDisabilityThesaurusForm

    class Media:
        js = ("http://code.jquery.com/jquery-1.9.1.min.js", "js/CascadeDropdownBox.js")


class DiagnosisAdmin(admin.ModelAdmin):
    actions = None
    form = DiagnosisForm
    fieldsets = (
        (None, {
            'fields': ('patient', 'diagnosis', 'muscle_biopsy')
        }),
        ('Phenotype', {
            'fields': ('phenotype_hpo', 'phenotype_orpha', 'orpha_disability_thesaurus')
        }),
    )
    inlines = [
        MotorFunctionInline,
        SteroidsInline,
        SurgeryInline,
        HeartInline,
        HeartMedicationInline,
        RespiratoryInline,
        FamilyMemberInline,
        ClinicalTrialsInline,
        OtherRegistriesInline,
        NotesInline,
    ]
    search_fields = ["patient__family_name", "patient__given_names"]

    # FJ added 'working group' field
    # Trac#32 added 'process_graph'
    list_display = ['patient_name', 'patient_working_group', 'progress_graph']

    def patient_name(self, obj):
        return ("%s") % (obj.patient,)

    def patient_working_group(self, obj):
        return ("%s") % (obj.patient.working_group,)

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

admin.site.register(Diagnosis, DiagnosisAdmin)
admin.site.register(PhenotypeHpo)
admin.site.register(PhenotypeOrpha)
admin.site.register(OrphaDisabilityThesaurus)
admin.site.register(PhenotypeOrphaDisability)
admin.site.register(PhenotypeOrphaDisabilityType)
admin.site.register(PhenotypeOrphaSeverity)
admin.site.register(PhenotypeOrphaFrequency)
admin.site.register(PhenotypeOrphaThesaurus)