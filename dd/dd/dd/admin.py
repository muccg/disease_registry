from django.contrib import admin
from dd.dd.models import *
from admin_forms import *
from registry.utils import get_static_url
from registry import groups

class ClinicalDataAdmin(admin.ModelAdmin):
    model = DDClinicalData
    form = ClinicalDataForm

class DDMedicalHistoryAdminInline(admin.TabularInline):
    model = DDMedicalHistoryRecord
    extra = 1
    form = DDMedicalHistoryForm

class MedicalHistoryAdmin(admin.ModelAdmin):
    inlines = [DDMedicalHistoryAdminInline]

class LabDataInline(admin.TabularInline):
    model = LabData
    excludes = ('patient',)

class LabDataAdmin(admin.ModelAdmin):
    model = LabData

class TreatmentCourseInline(admin.TabularInline):
    model = TreatmentCourse
    form = TreatmentCourseForm

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

class MRIFileInline(admin.TabularInline):
    model = MRIFile
    extra = 0

class MRIDataInline(admin.StackedInline):
    model = MRIData
    inlines = [MRIFileInline]
    fields = ("diagnosis", "date", "location",
              ("brain", "cervical", "thoracic"),
              "report_file", "image_file")
    form = MRIDataForm
    extra = 1

class MRIDataAdmin(admin.ModelAdmin):
    inlines = [MRIFileInline]

    fields = ("diagnosis", "date", "location",
              ("brain", "cervical", "thoracic"),
              "report_file")

class DDDiagnosisAdmin(admin.ModelAdmin):
    form = DDDiagnosisForm

    inlines = [
               DDMedicalHistoryAdminInline,
               DDClinicalDataInline,
               LabDataInline,
               DDTreatmentOverviewInline,
               MRIDataInline,
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
        form = super(DDDiagnosisAdmin, self).get_form(request, obj, **kwargs)
        form.user = request.user
        return form

    def progress_graph(self, obj):
        return obj.progress_graph()

    progress_graph.allow_tags = True
    progress_graph.short_description = "Diagnosis Entry Progress"

class MedicalHistoryDiseaseAdmin(admin.ModelAdmin):
    list_display = ['disease',]

admin.site.register(MedicalHistory, MedicalHistoryAdmin)
admin.site.register(LabData, LabDataAdmin)
admin.site.register(Treatment, TreatmentAdmin)
admin.site.register(DDTreatmentOverview, DDTreatmentOverviewAdmin)
admin.site.register(Diagnosis, DDDiagnosisAdmin)
admin.site.register(DDClinicalData, ClinicalDataAdmin)
admin.site.register(MRIData, MRIDataAdmin)
admin.site.register(MedicalHistoryDisease, MedicalHistoryDiseaseAdmin)
admin.site.register(EdssRating)
