from django.conf.urls.defaults import *
from views import clinical, index, personal, thanks


urlpatterns = patterns("",
    (r"^clinical", clinical),
    (r"^personal", personal),
    (r"^thanks", thanks),
    (r"^index", index),
    (r"^[/]*$", index),
)
