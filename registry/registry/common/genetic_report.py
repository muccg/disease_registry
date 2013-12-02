from django.http import HttpResponse
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.db.models import Q

from registry.genetic.models import Variation

class GeneticReport(View):
    
    @method_decorator(login_required)
    def get(self, request):
        varations = Variation.objects.get_containing('protein_variation', ['X', '*'])
        
        return HttpResponse(varations)