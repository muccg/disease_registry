from django.conf.urls.defaults import patterns
from django.contrib import admin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseBadRequest
from django.core import urlresolvers
from django.conf import settings
import json, datetime

from admin_forms import *
from models import *


class CountryAdmin(admin.ModelAdmin):
    search_fields = ["name"]


class DoctorAdmin(admin.ModelAdmin):
    search_fields = ["family_name", "given_names"]


class PatientDoctorAdmin(admin.TabularInline):
    fields = ["relationship", "doctor"]
    form = PatientDoctorForm
    model = PatientDoctor


class PatientAdmin(admin.ModelAdmin):
    form = PatientForm
    inlines = [PatientDoctorAdmin]
    search_fields = ["family_name", "given_names"]
    list_display = ['__unicode__', 'progress_graph', 'moleculardata_entered', 'freshness', 'working_group', 'last_updated']

    def create_fieldset(self, superuser=False):
        """Function to dynamically create the fieldset, adding 'active' field if user is a superuser"""

        consent = ("Consent", {
            "fields":
            ("consent",
             )})

        personal_details = ("Personal Details", {})

        personal_details_fields = ["working_group",
                                   "family_name",
                                   "given_names",
                                   "date_of_birth",
                                   "sex",
                                   "address",
                                   "suburb",
                                   "state",
                                   "postcode",
                                   "home_phone",
                                   "mobile_phone",
                                   "work_phone",
                                   "email"
                                   ]

        # fix for Trac #3, the field is now always displayed, but readonly for not superuser users, see get_readonly_fields below
        personal_details_fields.append("active")
        
        personal_details[1]["fields"] = tuple(personal_details_fields)

        next_of_kin = ("Next of Kin", {
            "fields":
            ("next_of_kin_family_name",
             "next_of_kin_given_names",
             "next_of_kin_address",
             "next_of_kin_suburb",
             "next_of_kin_state",
             "next_of_kin_postcode",                
             "next_of_kin_home_phone",
             "next_of_kin_mobile_phone",
             "next_of_kin_work_phone",
             "next_of_kin_email",
             )})

        fieldset = (consent, personal_details, next_of_kin,)
        return fieldset

    def get_fieldsets(self, request, obj=None): 
        return self.create_fieldset(request.user.is_superuser)

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        else:
            #return ['active'] # NB this seems to run into a mango bug that prevents Add Patient being used by non-superuser
            return []        

    def formfield_for_dbfield(self, dbfield, *args, **kwargs):
        from registry.groups.models import User, WorkingGroup

        request = kwargs.get('request')
        user = request.user
        # Restrict normal users to their own working group.
        if dbfield.name == "working_group" and not user.is_superuser:
            user = User.objects.get(user=user) # get the user's associated objects
            workinggroupid = user.working_group.id
            kwargs["queryset"] = WorkingGroup.objects.filter(id = workinggroupid)

        return super(PatientAdmin, self).formfield_for_dbfield(dbfield, *args, **kwargs)

    def get_urls(self):
        urls = super(PatientAdmin, self).get_urls()
        local_urls = patterns("",
            (r"search/(.*)$", self.admin_site.admin_view(self.search))
        )
        return local_urls + urls

    def queryset(self, request):
        import registry.groups.models

        if request.user.is_superuser:
            return Patient.objects.all()

        user = registry.groups.models.User.objects.get(user=request.user)
        return Patient.objects.filter(working_group=user.working_group).filter(active=True)

    def search(self, request, term):
        # We have to do this against the result of self.queryset() to avoid
        # leaking patient details across working groups.
        queryset = self.queryset(request)

        try:
            # Check if the search term is numeric, in which case it's a record
            # ID.
            patient = queryset.get(id=int(term))
            response = [[patient.id, unicode(patient), unicode(patient.date_of_birth)]]
        except ValueError:
            # Guess not.
            patients = queryset.filter(Q(family_name__icontains=term) | Q(given_names__icontains=term)).order_by("family_name", "given_names")
            response = [[patient.id, unicode(patient), unicode(patient.date_of_birth)] for patient in patients]
        except Patient.DoesNotExist:
            response = []

        return HttpResponse(json.dumps(response), mimetype="application/json")


    def progress_graph(self, obj):
        if not hasattr(obj, 'diagnosis'):
            return ''

        graph_html = '<a href="%s">' % urlresolvers.reverse('admin:%s_diagnosis_change' % settings.INSTALL_NAME, args=(obj.id,))
        graph_html += '<img title="%s" src="http://chart.apis.google.com/chart' % obj.diagnosis.incomplete_sections()
        graph_html += '?chf=bg,s,FFFFFF00&chs=200x15&cht=bhs&chco=4D89F9,C6D9FD&chd=t:%d|100&chbh=5"/>' % obj.diagnosis.percentage_complete()
        graph_html += '</a>'
        return graph_html
    progress_graph.allow_tags = True
    progress_graph.short_description = "Diagnosis Entry Progress"

    def moleculardata_entered(self, obj):
        if not hasattr(obj, 'moleculardata') or not hasattr(obj.moleculardata, 'variation_set') or not obj.moleculardata.variation_set.all():
            return ''

        imagefile = 'tick.png'

        genetic_url = '<a href="%s">' % urlresolvers.reverse('admin:genetic_moleculardata_change', args=(obj.id,))
        genetic_url += '<img src="%s"/>' % url("/static/images/" + imagefile)
        genetic_url += '</a>'
        return genetic_url

    moleculardata_entered.allow_tags = True
    moleculardata_entered.short_description = "Genetic Data"


    def freshness(self, obj):
        """Used to show how recently the diagnosis was updated"""
        if not hasattr(obj, 'diagnosis'):
            return ''

        delta = datetime.datetime.now() - obj.diagnosis.updated
        age = delta.days

        if age > 365:
            imagefile = 'cross.png'
        else:
            imagefile = 'tick.png'

        return '<img src="%s"/>' % url("/static/images/" + imagefile)
        
    freshness.allow_tags = True
    freshness.short_description = "Currency (updated in the last 365 days)"

    def last_updated(self, obj):
        if not hasattr(obj, 'diagnosis'):
            return ''
        delta = datetime.datetime.now() - obj.diagnosis.updated
        age = delta.days

        if age == 0:
            return 'today'
        if age == 1:
            return 'yesterday'
        else:
            return '%s days ago' % age

    last_updated.allow_tags = True
    last_updated.short_description = "Last updated"

class StateAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]
    search_fields = ["name"]


admin.site.register(Country, CountryAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(State, StateAdmin)


admin.site.disable_action('delete_selected')
