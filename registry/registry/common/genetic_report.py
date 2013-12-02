from django.http import HttpResponse
from django.views.generic.base import View

class GeneticReport(View):
    def get(self, request):
        return HttpResponse('result')