from django.http import HttpResponse
from django.views.generic.base import View

from django.db.models import Q

from registry.genetic.models import Variation

class GeneticReport(View):
    def get(self, request):
        varations = Variation.objects.get_containing('protein_variation', ['X', '*'])
        
        return HttpResponse(varations)