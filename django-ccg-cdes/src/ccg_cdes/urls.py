from django.conf.urls import patterns, url
import views

urlpatterns = patterns("",
    url(r"^patient/(\d+)$", views.patient_cdes),
)
