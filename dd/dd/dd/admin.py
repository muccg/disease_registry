from django.contrib import admin
from dd.dd.models import *
from admin_forms import *
from registry.utils import get_static_url
from registry import groups

class DDMedicalHistoryAdminInline(admin.TabularInline):
    model = DDMedicalHistoryRecord
    extra = 1
    form = DDMedicalHistoryForm

class MedicalHistoryAdmin(admin.ModelAdmin):
    inlines = [DDMedicalHistoryAdminInline]

class DDLabDataRecordInline(admin.TabularInline):
    model = DDLabDataRecord

class DDLabDataInline(admin.TabularInline):
    model = DDLabData
    excludes = ('patient',)

class DDLabDataAdmin(admin.ModelAdmin):
    inlines = [DDLabDataRecordInline]

class TreatmentCourseInline(admin.TabularInline):
    model = TreatmentCourse

class TreatmentInline(admin.TabularInline):
    model = Treatment

class TreatmentAdmin(admin.ModelAdmin):
    inlines = [TreatmentCourseInline]

class DDTreatmentOverviewAdmin(admin.ModelAdmin):
    model = DDTreatmentOverview
    inlines = [TreatmentCourseInline]

class DDTreatmentOverviewInline(admin.StackedInline):
    model = DDTreatmentOverview

class DDClinicalDataInline(admin.TabularInline):
    model = DDClinicalData


class DDMRIDataInline(admin.TabularInline):
    model = DDMRIData

class DDMRIDataRecordInline(admin.TabularInline):
    model = DDMRIDataRecord

class DDMRIDataAdmin(admin.ModelAdmin):
    inlines = [DDMRIDataRecordInline]

class DDDiagnosisAdmin(admin.ModelAdmin):
    form = DDDiagnosisForm
    
    inlines = [
               DDMedicalHistoryAdminInline,
               DDClinicalDataInline,
               DDLabDataInline,
               DDTreatmentOverviewInline,
               DDMRIDataInline,
               #DDMRIDataRecordInline,
              ]


    search_fields = ["patient__family_name", "patient__given_names"]
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
            return DDDiagnosis.objects.all()

        user = groups.models.User.objects.get(user=request.user)

        if self.has_change_permission(request):
            return DDDiagnosis.objects.filter(patient__working_group=user.working_group).filter(patient__active=True)
        else:
            return DDDiagnosis.objects.none()

    def get_form(self, request, obj=None, **kwargs):
        """
        We provide our own get_form so we can access the user object
        and narrow choice fields in the form by user rights
        """
        form = super(DDDiagnosisAdmin, self).get_form(request, obj, **kwargs)
        form.user = request.user
        return form

    def progress_graph(self, obj):
        return obj.progress_graph()

    progress_graph.allow_tags = True
    progress_graph.short_description = "Diagnosis Entry Progress"
    
#admin.site.register(MedicalHistoryItem)
#admin.site.register(MedicalHistoryGrouping)
admin.site.register(MedicalHistory, MedicalHistoryAdmin)
#admin.site.register(DDMedicalHistoryRecord)
admin.site.register(DDLabData, DDLabDataAdmin)
admin.site.register(Treatment, TreatmentAdmin)
admin.site.register(DDTreatmentOverview, DDTreatmentOverviewAdmin)
admin.site.register(DDDiagnosis, DDDiagnosisAdmin)
admin.site.register(DDClinicalData)
admin.site.register(DDMRIData, DDMRIDataAdmin)
admin.site.register(Patient)
#admin.site.register(DDLabDataRecord)

