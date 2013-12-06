from django.conf.urls import patterns, url
import views

from genetic_report import GeneticReport

urlpatterns = patterns("",
    url(r"^patient/", views.patient_report),
    url(r"^genetic/", GeneticReport.as_view())
)
