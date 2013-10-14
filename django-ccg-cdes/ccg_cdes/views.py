from django.forms import Form
from models import CommonDataElement
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings

def patient_cdes(request, patient_id):
    owner_model_func = settings.CDE_MODEL_MAP["P"]
    owner_model = owner_model_func()

    class CDEForm(Form):
        pass

    for cde in CommonDataElement.objects.all().filter(owner='P'):
        cde_field = cde.create_field(owner_model)
        field_name = "cde_" + cde_field.name
        setattr(CDEForm, field_name, cde_field)


    if request.method == "POST":
        form = CDEForm(request.POST)
        if form.is_valid():
            # process data
            return HttpResponseRedirect('/cdes/patient/%s' % patient_id)
    else:
        form = CDEForm()

    return render(request, 'cde.html', {'form':   form,
                                        'owner':  'patient',
                                        'owner_id': patient_id})







