from django.conf.urls import patterns, url
import views

urlpatterns = patterns("",
    url(r"^cdes/patient/(\d+)", views.patient_cdes, name="patient"),
)
