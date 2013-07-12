from django.conf.urls import *
from views import clinical, index, personal, thanks


urlpatterns = patterns("",
    (r"^clinical", clinical),
    (r"^personal", personal),
    (r"^thanks", thanks),
    (r"^(?P<country>\w{2})/index", index),
    (r"^(?P<country>\w{2})[/]*$", index),
)
