from django.contrib import admin

from models import *

class EmailTemplateAdmin(admin.ModelAdmin):
    model = EmailTemplate
    list_display = ['name', 'target']

class ConsentFormAdmin(admin.ModelAdmin):
    model = ConsentForm
    list_display = ['country']

admin.site.register(EmailTemplate, EmailTemplateAdmin)
admin.site.register(ConsentForm, ConsentFormAdmin)