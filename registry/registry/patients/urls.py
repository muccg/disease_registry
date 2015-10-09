from django.conf.urls import *
from django.contrib import admin

from PatientStatsView import PatientStatsView

urlpatterns = patterns('',
    (r'^stats$', PatientStatsView.as_view())
)
