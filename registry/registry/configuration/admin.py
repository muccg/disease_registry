from django.contrib import admin

from models import *

class EmailTemplateAdmin(admin.ModelAdmin):
    model = EmailTemplate

admin.site.register(EmailTemplate, EmailTemplateAdmin)
admin.site.register(Module)