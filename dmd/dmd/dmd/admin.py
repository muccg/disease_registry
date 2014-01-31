import os

from django.contrib import admin

from admin_views.admin import AdminViews

from admin_forms import *
from models import *

from registry.groups.models import User as RegistryUser
from registry import groups
from registry.utils import get_static_url, get_working_groups

import reversion

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
                kwargs["queryset"] = Patient.objects.filter(working_group__in=get_working_groups(user))

        return super(FamilyMemberInline, self).formfield_for_foreignkey(db_field, request, **kwargs)


class NotesInline(admin.TabularInline):
    model = Notes


class DiagnosisAdmin(AdminViews, reversion.VersionAdmin):
    app_url = os.environ.get("SCRIPT_NAME", "")
    
    admin_views = (
        ('NMD Report Australia', '%s/%s' % (app_url, 'explorer/2/download?params={%22jurisdiction%22:%22Western%20Australia%22}') ),
        ('NMD Report New Zealand', '%s/%s' % (app_url, 'explorer/2/download?params={%22jurisdiction%22:%22New%20Zealand%22}') ),
        ('Genetic Report', '%s/%s' % (app_url, 'explorer/3/download') ),
    )

    app_url = os.environ.get("SCRIPT_NAME", "")
    
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
            return Diagnosis.objects.filter(patient__working_group__in=get_working_groups(user)).filter(patient__active=True)
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