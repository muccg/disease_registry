from django.contrib import admin
from admin_forms import *
from models import *


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
    #raw_id_fields = ("registry_patient",)
    extra = 3


class NotesInline(admin.TabularInline):
    model = Notes


class DiagnosisAdmin(admin.ModelAdmin):
    actions = None
    form = DiagnosisForm
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

    #FJ added 'working group' field
    list_display = ['patient_name', 'patient_working_group']

    def patient_name(self, obj):
        return ("%s") % (obj.patient, )

    def patient_working_group(self, obj):
        return ("%s") % (obj.patient.working_group, )

    patient_name.short_description = 'Name'
    patient_working_group.short_description = 'Working Group'

    class Media:
        from ccg.utils.webhelpers import url

        css = {
            "screen": [url("/static/css/diagnosis_admin.css")]
        }

    def queryset(self, request):
        import groups.models

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

admin.site.register(Diagnosis, DiagnosisAdmin)
