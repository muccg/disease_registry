from django.contrib import admin

from models import *

class EmailTemplateAdmin(admin.ModelAdmin):
    model = EmailTemplate
    list_display = ['name', 'target']

admin.site.register(EmailTemplate, EmailTemplateAdmin)